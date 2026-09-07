---
id: emb-raii-0021
title: "Чому вкладені ресурси звільняються у зворотному порядку автоматично?"
description: "Деструктори локальних об'єктів викликаються у порядку, ЗВОРОТНОМУ до конструювання."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 2
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

**Деструктори локальних об'єктів викликаються у порядку, ЗВОРОТНОМУ до конструювання.**

Якщо взяв clock, потім SPI, потім CS – звільнення піде CS -> SPI -> clock, що зазвичай і є правильним порядком teardown. Вручну це легко переплутати.

Правило: оголошуй RAII-guard'и у порядку залежностей; reverse-destruction подбає про коректний teardown.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
