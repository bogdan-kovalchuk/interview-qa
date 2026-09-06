---
id: emb-raii-0015
title: "Як конструювати об'єкт без `malloc` у заздалегідь виділеному буфері?"
description: "Placement new будує об'єкт у наданій пам'яті без алокації."
track: embedded
section: raii-and-smart-pointers
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
alignas(T) std::byte storage[sizeof(T)];
T* obj = new (storage) T(args); // placement new
obj->~T(); // явний виклик dtor
```

**Placement new будує об'єкт у наданій пам'яті без алокації.**

Памʼять може бути static-масивом чи memory pool і має мати правильний alignment. Деструктор треба викликати явно (`obj->~T()`), бо `delete` тут не застосовний.

Правило: placement new + явний dtor = динамічне конструювання без heap.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
