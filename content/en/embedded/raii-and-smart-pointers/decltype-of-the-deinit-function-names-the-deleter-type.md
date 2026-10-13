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
updated: 2026-10-13
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-13; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says unique_ptr stores a pointer and a deleter, and its destructor calls the deleter only for a non-null pointer; release() returns the pointer and sets it to null without calling the deleter. Does not fix the object's size."
  - source_id: cpp-draft-intro-object
    title: "C++ working draft: Object model ([intro.object])"
    url: https://eel.is/c++draft/intro.object
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says a base subobject of a standard-layout class with no non-static data members has zero size, and that otherwise the circumstances of zero size are implementation-defined. Gives no sizeof values."
---

## Question code

```cpp
std::unique_ptr<HAL_Type, decltype(&HAL_DeInit)>
  res(&hal_obj, &HAL_DeInit);
// очищення гарантоване при виході зі scope
```

## Short answer

**The deleter type is `decltype(&HAL_DeInit)`, passing the function itself.**

On destruction of `res`, if the pointer is not `nullptr`, `HAL_DeInit(&hal_obj)` is called. A function pointer deleter is readable, but `unique_ptr` stores both the object pointer and the function pointer, so it takes at least two pointers.[^cpp-draft-unique-ptr-single]

Rule: a function pointer deleter is simple; a stateless lambda or empty functor may add no bytes, so prefer it when `sizeof(unique_ptr)` is critical.[^cpp-draft-intro-object]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
