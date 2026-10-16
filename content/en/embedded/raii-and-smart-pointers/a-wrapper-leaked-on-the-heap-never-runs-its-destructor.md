---
id: emb-raii-0029
title: "Trap: what happens to the resource if a wrapper object is created on the heap and never deleted?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-basic-stc-dynamic
    title: "C++ working draft: [basic.stc.dynamic.general]"
    url: https://eel.is/c++draft/basic.stc.dynamic.general
  - source_id: cpp-draft-unique-ptr-dtor
    title: "C++ working draft: [unique.ptr.single.dtor]"
    url: https://eel.is/c++draft/unique.ptr.single.dtor
  - source_id: cpp-core-guidelines-r5
    title: "C++ Core Guidelines, R.5: Prefer scoped objects, don’t heap-allocate unnecessarily"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r5-prefer-scoped-objects-dont-heap-allocate-unnecessarily
---

## Short answer

<span class="warn">The destructor is never called -> the resource is never freed (leak), despite this being an RAII class.</span>[^cpp-draft-basic-stc-dynamic]

An object created with `new` is destroyed only by a delete-expression, so `new LockGuard(...)` without delete is the same forgotten unlock.

Defense: keep RAII objects on the stack, as the C++ Core Guidelines recommend (R.5),[^cpp-core-guidelines-r5] or under `unique_ptr`, which calls its deleter (by default delete) in its destructor.[^cpp-draft-unique-ptr-dtor]

## Detailed explanation

TODO
