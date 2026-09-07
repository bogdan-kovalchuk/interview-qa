---
id: emb-tmplcx-0013
title: "Trap: чому не можна казати «templates не мають вартості»?"
description: "Templates можуть мати нульову runtime-вартість, але мають реальну вартість у Flash і часі компіляції."
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

<span class="warn">Templates можуть мати нульову runtime-вартість, але мають реальну вартість у Flash і часі компіляції.</span>

Кожна унікальна інстанціація може згенерувати власну копію коду у Flash; білд сповільнюється через інстанціацію + перевірку типів.

Захист: на інтерв'ю кажи «zero runtime cost не означає zero flash cost», і перевіряй linker map.[^embeddedinterviewlab]

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
