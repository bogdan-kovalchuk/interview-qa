---
id: emb-cppoop-0028
title: "Що таке static member класу і де він живе?"
description: "Static member – спільний для всіх екземплярів; існує в одному примірнику, а не в кожному об'єкті."
track: embedded
section: cpp-classes-and-oop
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
class Counter {
  static uint32_t count_; // одна на клас
};
```

**Static member – спільний для всіх екземплярів; існує в одному примірнику, а не в кожному об'єкті.**

Він живе у `.data`/`.bss` (не в об'єкті), тож не збільшує `sizeof` екземпляра. Потребує визначення поза класом (до C++17) або `inline static`.

Правило: static member – для даних/лічильників рівня класу, а не окремого об'єкта.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
