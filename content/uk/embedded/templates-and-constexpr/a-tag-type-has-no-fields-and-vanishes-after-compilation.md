---
id: emb-tmplcx-0021
title: "Чому `Quantity<Tag>` не має runtime-оверхеду?"
description: "Tag-тип не має полів – він існує лише в системі типів і повністю зникає після компіляції."
track: embedded
section: templates-and-constexpr
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

**Tag-тип не має полів – він існує лише в системі типів і повністю зникає після компіляції.**

Об'єкт містить лише `Rep value` (напр. `int32_t`), тож `sizeof(Quantity) == sizeof(int32_t)`. Перевірка сумісності одиниць коштує нуль байтів і нуль тактів.

Правило: «phantom types» дають безпеку одиниць без жодної ціни в runtime.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
