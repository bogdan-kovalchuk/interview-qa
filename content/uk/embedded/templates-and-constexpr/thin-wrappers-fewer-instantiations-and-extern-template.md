---
id: emb-tmplcx-0015
title: "Які є стратегії боротьби з template code bloat?"
description: "Thin wrapper над void; обмеження кількості інстанціацій; extern template; винесення T-незалежного коду у non-template base; LTO (link-time optimization)."
track: embedded
section: templates-and-constexpr
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
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

**Thin wrapper над `void*`; обмеження кількості інстанціацій; `extern template`; винесення T-незалежного коду у non-template base; LTO (link-time optimization).**

Ідея: тримати в шаблоні лише тонкий типобезпечний шар, а спільну реалізацію – поза шаблоном (через `void*` + `sizeof(T)` або базовий клас).

Правило: factor out усе, що не залежить від `T`, у non-template код.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
