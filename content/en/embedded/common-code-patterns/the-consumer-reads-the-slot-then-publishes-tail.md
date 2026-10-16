---
id: emb-patterns-0009
title: "How does the consumer's `rb_get` work in an SPSC ring buffer?"
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
