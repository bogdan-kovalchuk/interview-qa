---
id: emb-raii-0024
title: "What does a `unique_ptr` with a HAL deinit function pointer look like?"
description: "The deleter type is decltype of the HAL deinit function address and the function itself is passed."
track: embedded
section: raii-and-smart-pointers
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
---

## Question code

```cpp
std::unique_ptr<HAL_Type, decltype(&HAL_DeInit)>
  res(&hal_obj, &HAL_DeInit);
// очищення гарантоване при виході зі scope
```

## Short answer

**The deleter type is `decltype(&HAL_DeInit)`, passing the function itself.**

On destruction of `res`, `HAL_DeInit(&hal_obj)` is called. A function pointer deleter is readable, but `unique_ptr` usually stores both the object pointer and the deleter pointer, so it can be larger than a raw pointer.

Rule: a function pointer deleter is simple; a stateless lambda or empty functor is usually better if `sizeof(unique_ptr)` is critical.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
