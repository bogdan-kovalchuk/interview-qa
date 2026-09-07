---
id: emb-patterns-0008
title: "What does `rb_put` (the producer) look like in a lock-free ring buffer?"
description: "Producer writes data into the slot and then updates head last to publish it."
track: embedded
section: common-code-patterns
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
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

**Producer writes data, then updates `head` last.**

First compute `next` with the mask; if `next == tail` the buffer is full and nothing is written. Writing into `buf` before updating `head` guarantees the consumer does not see a half-written slot.

Rule: only the producer touches `head` – that is what makes it lock-free.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
