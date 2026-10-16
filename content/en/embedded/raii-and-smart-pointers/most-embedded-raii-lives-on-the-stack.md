---
id: emb-raii-0014
title: "Does RAII require heap allocation?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cppcg-r5
    title: "C++ Core Guidelines: R.5 – Prefer scoped objects, don’t heap-allocate unnecessarily"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r5-prefer-scoped-objects-dont-heap-allocate-unnecessarily
  - source_id: cpp-draft-thread-lock-guard
    title: "C++ working draft: Class template lock_guard ([thread.lock.guard])"
    url: https://eel.is/c++draft/thread.lock.guard
  - source_id: cpp-draft-stmt-jump-general
    title: "C++ working draft: Jump statements, general ([stmt.jump.general])"
    url: https://eel.is/c++draft/stmt.jump.general
  - source_id: cpp-draft-basic-start-term
    title: "C++ working draft: Termination ([basic.start.term])"
    url: https://eel.is/c++draft/basic.start.term
---

## Short answer

**No – RAII does not require the heap.**

An RAII object can be a local variable, a class member or a global object, so it needs no separate allocation: a scoped object adds no alloc/dealloc beyond what its enclosing scope already has.[^cppcg-r5] Typical embedded RAII – lock guards and scope handles – wraps resources that exist independently (a mutex, an interrupt mask), and `std::lock_guard` by specification stores only a reference to the mutex.[^cpp-draft-thread-lock-guard]

Rule: a stack-allocated guard is the most common and fully heap-free RAII.

## Detailed explanation

TODO
