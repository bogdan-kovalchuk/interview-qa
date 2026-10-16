---
id: emb-tmplcx-0030
title: "Trap: чому надмірне зведення всіх типів до `uint32_t` заради меншого bloat – компроміс?"
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

<span class="warn">Менше інстанціацій (менше Flash), але `uint32_t` марнує RAM на дрібних значеннях.</span>

Якщо буфер міг бути `uint8_t`, а ти зробив `uint32_t` заради однієї інстанціації – економиш ROM, але вчетверо роздуваєш RAM-буфер.

Захист: балансуй між кількістю інстанціацій (Flash) і шириною типу (RAM) під конкретний MCU.[^embeddedinterviewlab]

## Detailed explanation

TODO
