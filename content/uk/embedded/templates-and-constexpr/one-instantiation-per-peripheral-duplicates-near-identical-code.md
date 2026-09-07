---
id: emb-tmplcx-0024
title: "Trap: чому `Uart<USART1>` і `Uart<USART2>` можуть роздути Flash?"
description: "Кожна інстанціація per-периферію може дати майже ідентичний код – різниться лише константа base address."
track: embedded
section: templates-and-constexpr
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
---

## Short answer

<span class="warn">Кожна інстанціація per-периферію може дати майже ідентичний код – різниться лише константа base address.</span>

На малих MCU (microcontroller unit) це швидко накопичується, якщо так само зробити `Uart<...>`, `Spi<...>`, `I2c<...>` для багатьох периферій.

Захист: non-template `UartImpl` з base address як параметром ctor + тонка шаблонна обгортка з `constexpr` адресою; економію підтверджуй linker map.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
