---
id: emb-raii-0024
title: "Як виглядає `unique_ptr` з HAL-deinit як function pointer?"
description: "Тип deleter'а – decltype(&HAL_DeInit), передаємо саму функцію."
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
std::unique_ptr<HAL_Type, decltype(&HAL_DeInit)>
  res(&hal_obj, &HAL_DeInit);
// очищення гарантоване при виході зі scope
```

**Тип deleter'а – `decltype(&HAL_DeInit)`, передаємо саму функцію.**

При знищенні `res` викличеться `HAL_DeInit(&hal_obj)`. Function pointer deleter читабельний, але `unique_ptr` зазвичай зберігає і object pointer, і deleter pointer, тобто може бути більшим за raw pointer.

Правило: function pointer deleter простий; stateless lambda/empty functor зазвичай кращі, якщо критичний `sizeof(unique_ptr)`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
