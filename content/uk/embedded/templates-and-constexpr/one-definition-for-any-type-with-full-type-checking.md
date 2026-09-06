---
id: emb-tmplcx-0001
title: "Що таке function template і чим він кращий за макрос?"
description: "Одне визначення, що працює для будь-якого типу – з повним type checking."
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

```cpp
template<typename T>
T clamp(T v, T lo, T hi) {
  return v < lo ? lo : (v > hi ? hi : v);
}
```

**Одне визначення, що працює для будь-якого типу – з повним type checking.**

На відміну від макроса: типобезпека, аргументи обчислюються рівно один раз (немає double evaluation), повноцінний дебаг, нормальні повідомлення про помилки, overload resolution.

Правило: function template – сучасна заміна function-like макроса.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
