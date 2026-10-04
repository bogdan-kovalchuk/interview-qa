---
id: emb-patterns-0008
title: "How does the producer's `rb_put` work in an SPSC ring buffer?"
description: "The producer first writes an item into a free slot, then publishes it by updating head."
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
    applicability: "Explains SPSC, publishing head after writing an item, release/acquire ordering, and full/empty constraints; Linux examples are not a ready-made MCU ISR implementation."
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

Separate ownership of `head` does not remove atomicity and memory-ordering requirements; platform guarantees are still needed.[^linux-circular-buffers]

## Detailed explanation

TODO

## Sources
<!-- generated from frontmatter -->
