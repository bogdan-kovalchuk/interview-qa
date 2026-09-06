---
id: emb-cppoop-0020
title: "Що таке CRTP і яку проблему він вирішує?"
description: "Curiously Recurring Template Pattern – поліморфізм на етапі компіляції через static_cast до похідного типу."
track: embedded
section: cpp-classes-and-oop
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
template <typename D>
class SensorBase {
public:
  int16_t read() {
    return static_cast<D*>(this)->read_impl();
  }
};
```

**Curiously Recurring Template Pattern – поліморфізм на етапі компіляції** через `static_cast` до похідного типу.

Похідний клас успадковує `SensorBase<Derived>`. Компілятор інлайнить `read_impl()` крізь cast -> той самий код, що й прямий виклик: без vtable, vptr і indirect call.

Правило: CRTP дає «віртуальну» структуру коду з нульовим runtime-оверхедом.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
