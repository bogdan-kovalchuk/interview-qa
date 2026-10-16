---
id: emb-patterns-0030
title: "Why can `malloc` be unsuitable for a ring buffer used in an ISR?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

<span class="warn">`malloc` can have variable latency, so its suitability in an ISR depends on the allocator and platform contract.</span>

C does not impose a universal ban on calling `malloc` from an ISR. In a system with a hard timing budget, preallocate the buffer unless the allocator guarantees bounded latency and safe use in that context.[^iso-c-n1570]

A power-of-two size is needed only to optimize index wrapping with a mask, not for every ring buffer.

## Detailed explanation

TODO
