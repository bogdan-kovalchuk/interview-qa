---
id: emb-tmplcx-0011
title: "Що таке CRTP і навіщо він у шаблонах?"
description: "CRTP (curiously recurring template pattern): base – шаблон, параметризований похідним: class Derived : public Base."
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
template<typename D>
class SensorBase {
public:
  int read_filtered() {
    int raw = static_cast<D*>(this)->read_raw();
    return (raw + last_) / 2;
  }
};
```

## Short answer

**CRTP (curiously recurring template pattern): base – шаблон, параметризований похідним: `class Derived : public Base`.**

Base викликає методи похідного через `static_cast<D*>(this)`, що резолвиться на етапі компіляції – поліморфізм без vtable.

Правило: CRTP дає «віртуальну» структуру без virtual dispatch; після оптимізації це часто без додаткового runtime-оверхеду.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
