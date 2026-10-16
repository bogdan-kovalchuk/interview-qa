---
id: emb-volconst-0060
title: "Why should `volatile` not be put on every variable just in case?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

<span class="warn">Excessive `volatile` degrades optimization and can mask an incorrect synchronization model.</span>

For volatile-qualified objects, the compiler must account for volatile accesses under its implementation's rules, which can limit some optimizations. The cost depends on the compiler and target; volatile does not define general ordering for non-volatile data and does not fix race conditions or atomicity problems.

Rule: use `volatile` as a precise contract for hardware/ISR/DMA observable state, not as a general anti-optimization incantation.[^iso-c-n1570]

## Detailed explanation

TODO
