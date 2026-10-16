---
id: emb-raii-0024
title: "What does a `unique_ptr` with a HAL deinit function pointer look like?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
  - source_id: cpp-draft-intro-object
    title: "C++ working draft: Object model ([intro.object])"
    url: https://eel.is/c++draft/intro.object
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
