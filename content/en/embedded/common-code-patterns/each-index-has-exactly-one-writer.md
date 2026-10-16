---
id: emb-patterns-0041
title: "Which shared invariant makes an SPSC ring buffer safe without locks?"
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
    title: "Circular Buffers (Linux kernel documentation)"
    url: https://www.kernel.org/doc/html/latest/core-api/circular-buffers.html
---

## Short answer

**Each index has exactly one writer: the producer writes only `head`, the consumer – only `tail`.**

Since there is no shared variable modified by both sides (like `count`), there is no read-modify-write race either.[^linux-circular-buffers] Each side only reads the other's index; that is safe only if the access is atomic and ordered against the buffer data (release/acquire or a barrier), not merely `volatile`.[^iso-c-n1570]

Rule: "one writer per variable" is the basis of lock-free SPSC (single-producer / single-consumer) queues, but only for exactly one producer and one consumer.[^linux-circular-buffers]

## Detailed explanation

TODO
