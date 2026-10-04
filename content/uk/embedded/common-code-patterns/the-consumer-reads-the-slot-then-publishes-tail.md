---
id: emb-patterns-0009
title: "Як працює `rb_get` consumer-а в SPSC ring buffer?"
description: "Consumer читає елемент за tail, а потім оновлює tail, щоб звільнити слот."
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
    applicability: "Описує порожній стан, читання елемента consumer-ом, звільнення tail після читання та acquire/release порядок; приклад Linux не гарантує переносність на MCU/ISR."
---

## Question code

```c
static inline bool rb_get(ringbuf_t *rb, uint8_t *b) {
  if (rb->head == rb->tail) return false; // empty
  *b = rb->buf[rb->tail];
  rb->tail = (rb->tail + 1) & RB_MASK;
  return true;
}
```

## Short answer

**Consumer читає дані, потім оновлює `tail` останнім.**

`head == tail` означає порожньо. Спершу читаємо слот `tail`, тоді просуваємо `tail`, щоб повідомити producer-у, що місце звільнене. Потрібні платформні гарантії atomicity та memory ordering.[^linux-circular-buffers]

Producer володіє `head`, consumer – `tail`; збережи цей порядок і не звільняй слот до завершення читання.[^linux-circular-buffers]

## Detailed explanation

Consumer спочатку порівнює опублікований `head` зі своїм `tail`. Якщо значення рівні, за домовленістю буфер порожній і функція повертає `false`. Інакше consumer читає значення з `buf[tail]`, копіює його у вихідний параметр, а потім просуває `tail`. Це оновлення повідомляє producer-у, що слот уже можна повторно використовувати.[^linux-circular-buffers]

Порядок читання, а потім публікації `tail` захищає слот від перезапису під час читання. Як і для producer-а, порядок рядків сам по собі не обов’язково створює міжконтекстну синхронізацію. Документація Linux описує acquire-load producer-ового `head` перед читанням елемента та release-store `tail` після завершення читання. Для конкретної MCU й ISR потрібно окремо встановити, що читання та запис індексів атомарні й compiler не переставить доступи всупереч потрібному протоколу.[^linux-circular-buffers]

У цьому шаблоні один consumer має одноосібно оновлювати `tail`. Якщо кілька контекстів викликають `rb_get`, їх потрібно серіалізувати або застосувати іншу чергу; інакше вони можуть прочитати той самий слот. Вихідний вказівник теж має бути дійсним, а caller має враховувати `false`, не використовуючи застаріле значення вихідної змінної.

**Типові помилки:**

- Просунути `tail` до копіювання даних і дозволити producer-у перезаписати слот.
- Вважати читання `head` і запис `tail` синхронізацією без гарантій платформи.
- Забути перевірити результат функції та спожити вихід, коли буфер порожній.

Отже, `tail` є індексом наступного елемента для читання, а його оновлення завершує читання попереднього слота.[^linux-circular-buffers]

## Sources
<!-- generated from frontmatter -->
