---
id: emb-raii-0027
title: "Why is an RAII guard constructor made `explicit`?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-conv-ctor
    title: "C++ working draft: [class.conv.ctor]"
    url: https://eel.is/c++draft/class.conv.ctor
  - source_id: cpp-core-guidelines-c46
    title: "C++ Core Guidelines, C.46: By default, declare single-argument constructors explicit"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c46-by-default-declare-single-argument-constructors-explicit
---

## Short answer

**To forbid implicit conversion from handle to guard.**

`explicit LockGuard(osMutexId_t)` prevents accidentally creating a temporary guard through an implicit conversion (for example, when a mutex is passed to a function that takes a guard by value); such a temporary guard would acquire the lock at the call site.[^cpp-draft-class-conv-ctor]

By default, make single-argument constructors `explicit`; the exception is a type where the implicit conversion is an intended part of its design.[^cpp-core-guidelines-c46]

## Detailed explanation

TODO
