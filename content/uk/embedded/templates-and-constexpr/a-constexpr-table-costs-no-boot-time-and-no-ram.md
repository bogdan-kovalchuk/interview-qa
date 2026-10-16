---
id: emb-tmplcx-0033
title: "Чому constexpr-таблиця у Flash краща за обчислення таблиці при старті?"
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

**Вона не марнує boot time й RAM – готова константа лежить у `.rodata`.**

Startup-цикл, що рахує CRC (cyclic redundancy check) або іншу lookup-таблицю, додає затримку до `main()` і часто тримає таблицю в RAM. `constexpr` переносить це у build time, лишаючи RAM вільною.

Правило: незмінні похідні дані обчислюй на компіляції, а не в startup-коді.[^embeddedinterviewlab]

## Detailed explanation

TODO
