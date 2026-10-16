---
id: emb-tmplcx-0024
title: "Trap: why can `Uart<USART1>` and `Uart<USART2>` inflate Flash?"
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

<span class="warn">Each instantiation per peripheral can produce nearly identical code – only the base address constant differs.</span>

On small MCUs (microcontroller unit) this adds up quickly if you do the same with `Uart<...>`, `Spi<...>`, `I2c<...>` for many peripherals.

Mitigation: a non-template `UartImpl` with base address as a ctor parameter plus a thin template wrapper with a `constexpr` address; confirm the savings with the linker map.[^embeddedinterviewlab]

## Detailed explanation

TODO
