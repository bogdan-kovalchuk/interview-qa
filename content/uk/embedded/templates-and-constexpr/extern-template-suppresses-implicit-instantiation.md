---
id: emb-tmplcx-0016
title: "Що робить `extern template`?"
description: "Забороняє неявну інстанціацію шаблону в кожному translation unit."
track: embedded
section: templates-and-constexpr
level: junior
type: mechanism
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

## Question code

```cpp
extern template class Buffer<uint8_t>;
```

## Short answer

**Забороняє неявну інстанціацію шаблону в кожному translation unit.**

Інстанціація відбувається явно в одному `.cpp`, а решта TU лише посилаються на неї – це прибирає дублювання однакового коду по об'єктних файлах.

Правило: `extern template` + одна явна інстанціація = одна копія коду замість багатьох.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
