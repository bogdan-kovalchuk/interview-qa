---
id: emb-patterns-0008
title: "How does the producer's `rb_put` work in an SPSC ring buffer?"
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

**Producer writes data, then updates `head` last.**

First compute `next` with the mask; if `next == tail` the buffer is full and nothing is written. Writing into `buf` before updating `head` guarantees the consumer does not see a half-written slot.

Separate ownership of `head` does not remove atomicity and memory-ordering requirements; platform guarantees are still needed.[^linux-circular-buffers]

## Detailed explanation

TODO
