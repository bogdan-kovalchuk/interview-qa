---
id: emb-tmplcx-0010
title: "Що таке partial specialization шаблону?"
description: "Спеціалізація за патерном (напр., усі вказівники), а не одним типом."
track: embedded
section: templates-and-constexpr
level: junior
type: mechanism
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
class Buffer<T*> {
  // для всіх вказівникових типів
};
```

**Спеціалізація за патерном (напр., усі вказівники), а не одним типом.**

`Buffer<T*>` застосується до будь-якого `T*`, дозволяючи спільну логіку для цілого сімейства типів.

Правило: partial specialization – коли поведінка спільна для класу типів (вказівники, масиви тощо).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
