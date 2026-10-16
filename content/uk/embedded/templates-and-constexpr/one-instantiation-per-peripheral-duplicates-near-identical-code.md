---
id: emb-tmplcx-0024
title: "Trap: чому `Uart<USART1>` і `Uart<USART2>` можуть роздути Flash?"
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

<span class="warn">Кожна інстанціація per-периферію може дати майже ідентичний код – різниться лише константа base address.</span>

На малих MCU (microcontroller unit) це швидко накопичується, якщо так само зробити `Uart<...>`, `Spi<...>`, `I2c<...>` для багатьох периферій.

Захист: non-template `UartImpl` з base address як параметром ctor + тонка шаблонна обгортка з `constexpr` адресою; економію підтверджуй linker map.[^embeddedinterviewlab]

## Detailed explanation

TODO
