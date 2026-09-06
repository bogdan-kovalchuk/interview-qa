---
id: emb-cppoop-0019
title: "Навіщо потрібен поліморфізм через `Sensor*` масив?"
description: "Гетерогенна колекція: різні конкретні типи за спільним інтерфейсом в одному масиві/контейнері."
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

**Гетерогенна колекція: різні конкретні типи за спільним інтерфейсом в одному масиві/контейнері.** 

```c
Sensor* arr[] = { &temp, &pressure, &humid };
for (auto s : arr) s->read();
```

Виклик через base-вказівник обирає реалізацію в runtime по vtable.

Правило: коли треба тримати РІЗНІ типи разом і викликати уніфіковано – це головний кейс для virtual.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
