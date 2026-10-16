---
id: emb-patterns-0042
title: "What should a candidate be able to do on embedded code pattern questions?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: holzmann-power-of-ten
    title: "The Power of Ten – Rules for Developing Safety Critical Code (G. J. Holzmann, NASA/JPL)"
    url: https://spinroot.com/gerard/pdf/P10.pdf
  - source_id: linux-circular-buffers
    title: "Circular Buffers (Linux kernel documentation)"
    url: https://www.kernel.org/doc/html/latest/core-api/circular-buffers.html
---

## Short answer

**Write an FSM (finite state machine) in both forms – switch and table; explain the trade-offs; build a power-of-two ring buffer and know why a shared `count` causes a race; perform bit operations via unsigned mask-and-shift.**

Plus: consistent return codes with every result checked, `volatile` for registers (but not as synchronization with an ISR), guard clauses for null/range.[^iso-c-n1570]

Rule: for every pattern have answers for "when to apply", "is it ISR-safe (interrupt service routine safe)" and "why no heap".

## Detailed explanation

TODO
