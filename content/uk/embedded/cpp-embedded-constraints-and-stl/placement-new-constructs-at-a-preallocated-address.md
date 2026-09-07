---
id: emb-cppstl-0007
title: "Як збудувати об'єкт без `new` через placement new?"
description: "Placement new конструює об'єкт за наперед виділеною адресою, без heap."
track: embedded
section: cpp-embedded-constraints-and-stl
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
alignas(Sensor) static uint8_t buf[sizeof(Sensor)];
Sensor* s = new (buf) Sensor(config);
// потім вручну: s->~Sensor();
```

## Short answer

**Placement new конструює об'єкт за наперед виділеною адресою, без heap.**

Памʼять – static-буфер чи memory-mapped регіон. `delete` тут не застосовний: деструктор треба викликати явно (`s->~Sensor()`).

Правило: placement new + явний dtor = динамічне конструювання без купи.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
