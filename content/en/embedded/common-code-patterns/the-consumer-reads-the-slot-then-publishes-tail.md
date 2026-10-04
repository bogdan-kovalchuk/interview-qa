---
id: emb-patterns-0009
title: "How does the consumer's `rb_get` work in an SPSC ring buffer?"
description: "The consumer reads the item at tail, then updates tail to release the slot."
track: embedded
section: common-code-patterns
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: linux-circular-buffers
    title: "Linux kernel documentation: Circular Buffers"
    url: https://docs.kernel.org/core-api/circular-buffers.html
    accessed: 2026-10-04
    kind: official
    version: current
    applicability: "Describes the empty state, consumer read, releasing tail after reading, and acquire/release ordering; the Linux example does not guarantee portability to an MCU/ISR."
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

**Consumer reads data, then updates `tail` last.**

`head == tail` means empty. First read the `tail` slot, then advance `tail` to tell the producer the slot is free. Platform guarantees for atomicity and memory ordering are required.[^linux-circular-buffers]

The producer owns `head`, and the consumer owns `tail`; preserve that ownership and do not release a slot before reading is complete.[^linux-circular-buffers]

## Detailed explanation

TODO

## Sources
<!-- generated from frontmatter -->
