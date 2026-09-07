---
id: emb-tmplcx-0030
title: "Trap: чому надмірне зведення всіх типів до `uint32_t` заради меншого bloat – компроміс?"
description: "Менше інстанціацій (менше Flash), але uint32_t марнує RAM на дрібних значеннях."
track: embedded
section: templates-and-constexpr
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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

<span class="warn">Менше інстанціацій (менше Flash), але `uint32_t` марнує RAM на дрібних значеннях.</span>

Якщо буфер міг бути `uint8_t`, а ти зробив `uint32_t` заради однієї інстанціації – економиш ROM, але вчетверо роздуваєш RAM-буфер.

Захист: балансуй між кількістю інстанціацій (Flash) і шириною типу (RAM) під конкретний MCU.[^embeddedinterviewlab]

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
