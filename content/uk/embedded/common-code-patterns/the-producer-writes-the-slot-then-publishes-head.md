---
id: emb-patterns-0008
title: "Як працює `rb_put` producer-а в SPSC ring buffer?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: linux-circular-buffers
    title: "Linux kernel documentation: Circular Buffers"
    url: https://docs.kernel.org/core-api/circular-buffers.html
---

## Question code

```c
static inline bool rb_put(ringbuf_t *rb, uint8_t b) {
  uint16_t next = (rb->head + 1) & RB_MASK;
  if (next == rb->tail) return false; // full
  rb->buf[rb->head] = b;
  rb->head = next;
  return true;
}
```

## Short answer

**Producer пише дані, потім оновлює `head` останнім.**

Спершу рахуємо `next` з маскою; якщо `next == tail` – буфер повний, нічого не пишемо. Запис у `buf` до оновлення `head` гарантує, що consumer не побачить недописаний слот.

Окреме володіння `head` не усуває вимог до atomicity та memory ordering; потрібні гарантії платформи.[^linux-circular-buffers]

## Detailed explanation

Producer спершу визначає позицію запису й перевіряє, чи є місце, а тоді записує елемент у вільний слот. Лише після завершення запису він просуває `head`. Таке оновлення індексу публікує слот: consumer, який спостеріг побачений новий `head`, може вважати відповідний елемент готовим. Буфер часто залишає одну комірку порожньою, щоб розрізнити повний і порожній стани за індексами.[^linux-circular-buffers]

Послідовність у вихідному тексті важлива, але на багатоядерній системі або при оптимізаціях compiler-а сама текстова послідовність не обов’язково задає достатній порядок видимості між контекстами. Linux ring-buffer документація використовує release-store для `head`, а consumer – acquire-load, щоб публікація даних передувала спостереженню нового індексу. MCU з ISR має власні гарантії: слід перевірити atomicity читання/запису індексу, правила compiler-а та потрібні бар’єри або критичну секцію.[^linux-circular-buffers]

У наведеному фрагменті припускаються коректний розмір масиву, маска `RB_MASK`, узгоджені типи індексів і єдиний producer. Перевірка `next == tail` консервативно відмовляє у записі, якщо наступне просування `head` зрівнялося б із `tail`; caller має обробити `false`, наприклад порахувати втрату або відкласти дані.

**Типові помилки:**

- Оновити `head` до запису байта й дати consumer-у прочитати старе вмістиме слота.
- Вважати, що один writer автоматично забезпечує atomicity та ordering.
- Ігнорувати повний буфер і мовчки перезаписувати ще не прочитане значення.

Перед використанням перевір, що атомарна операція є безблокувальною, якщо її викликають із ISR; деякі реалізації atomic можуть викликати бібліотечний helper або lock.[^linux-circular-buffers]
