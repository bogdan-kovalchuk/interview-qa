---
id: emb-patterns-0008
title: "Як працює `rb_put` producer-а в SPSC ring buffer?"
description: "Producer спершу записує елемент у вільний слот, а потім публікує його оновленням head."
track: embedded
section: common-code-patterns
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
  - source_id: linux-circular-buffers
    title: "Linux kernel documentation: Circular Buffers"
    url: https://docs.kernel.org/core-api/circular-buffers.html
    accessed: 2026-10-04
    kind: official
    version: current
    applicability: "Пояснює SPSC, публікацію head після запису елемента, release/acquire ordering та обмеження повного/порожнього буфера; приклади Linux не є готовою ISR реалізацією для MCU."
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

## Sources
<!-- generated from frontmatter -->
