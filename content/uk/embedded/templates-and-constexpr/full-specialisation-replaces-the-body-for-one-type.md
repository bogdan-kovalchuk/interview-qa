---
id: emb-tmplcx-0009
title: "Що таке full specialization шаблону?"
description: "Повністю інша реалізація для конкретного типу."
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
template<> class SpiDriver<STM32F4> {
  // register layout саме для STM32F4
};
```

## Short answer

**Повністю інша реалізація для конкретного типу.**

Дозволяє централізувати платформо-залежний код в одному місці замість розкиданих `#ifdef` по всьому проєкту.

Правило: full specialization – для одного конкретного типу/платформи з унікальним layout.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
