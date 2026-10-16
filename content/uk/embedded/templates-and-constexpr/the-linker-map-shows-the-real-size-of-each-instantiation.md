---
id: emb-tmplcx-0025
title: "Чому варто перевіряти linker map після додавання template-важкого коду?"
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

**Map-файл показує реальний розмір кожної інстанціації – єдиний спосіб побачити прихований bloat.**

Однакові на вигляд драйвери можуть дублювати кілобайти; map виявляє, що `Uart<USART1>` і `Uart<USART2>` – це дві майже однакові копії.

Правило: після template-heavy змін дивись `.map` і виноси type-independent логіку з шаблону.[^embeddedinterviewlab]

## Detailed explanation

TODO
