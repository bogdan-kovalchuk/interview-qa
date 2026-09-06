---
id: emb-cppoop-0016
title: "Що таке pure virtual функція і abstract клас?"
description: "= 0 робить функцію pure virtual; клас з нею стає abstract і його не можна інстанціювати."
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
class Sensor {
public:
  virtual int16_t read() = 0;
  virtual ~Sensor() = default;
};
```

**`= 0` робить функцію pure virtual; клас з нею стає abstract і його не можна інстанціювати.**

Abstract клас задає інтерфейс (контракт), який зобов'язані реалізувати похідні. Polymorphic derived objects матимуть vptr/vtable; сам abstract base object створити не можна.

Правило: abstract base – це C++-спосіб описати інтерфейс драйвера/HAL (hardware abstraction layer).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
