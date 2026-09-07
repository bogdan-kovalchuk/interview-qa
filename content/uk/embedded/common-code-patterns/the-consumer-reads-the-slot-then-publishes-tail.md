---
id: emb-patterns-0009
title: "Як виглядає `rb_get` (consumer) у lock-free ring buffer?"
description: "Consumer читає дані, потім оновлює tail останнім."
track: embedded
section: common-code-patterns
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
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

`head == tail` означає порожньо. Читаємо слот `tail`, тоді просуваємо `tail` з маскою. `tail` чіпає лише consumer.

Правило: producer володіє `head`, consumer – `tail`; жодна сторона не пише чужий індекс.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
