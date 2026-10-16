---
id: emb-patterns-0036
title: "What value does `next` get, and why?"
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
    title: "Circular Buffers (The Linux Kernel documentation)"
    url: https://www.kernel.org/doc/html/latest/core-api/circular-buffers.html
---

## Question code

```c
#define RB_SIZE 8
#define RB_MASK (RB_SIZE - 1)
uint16_t head = 7;
uint16_t next = (head + 1) & RB_MASK;
```

## Short answer

**`next == 0`** – wraparound to the start of the buffer.

`(7 + 1) & 7 = 8 & 0b0111 = 0`: the `SIZE-1` mask = `0b0111` keeps only the low three bits, so bit `0b1000` is discarded and the index wraps around without `%` or `if`.[^linux-circular-buffers][^iso-c-n1570]

Rule: this trick works only when `SIZE` is a power of two.

## Detailed explanation

TODO
