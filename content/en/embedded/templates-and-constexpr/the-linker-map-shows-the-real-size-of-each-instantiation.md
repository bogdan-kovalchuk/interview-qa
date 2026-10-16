---
id: emb-tmplcx-0025
title: "Why should you check the linker map after adding template-heavy code?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

**The map file shows the real size of each instantiation – the only way to spot hidden bloat.**

Drivers that look identical can duplicate kilobytes; the map reveals that `Uart<USART1>` and `Uart<USART2>` are two nearly identical copies.

Rule: after template-heavy changes, check the `.map` and move type-independent logic out of the template.[^embeddedinterviewlab]

## Detailed explanation

TODO
