---
id: emb-raii-0013
title: "Trap: what is wrong with \"RAII only works with smart pointers\"?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-stmt-jump-general
    title: "C++ working draft: Jump statements, general ([stmt.jump.general])"
    url: https://eel.is/c++draft/stmt.jump.general
  - source_id: cpp-draft-thread-lock-guard
    title: "C++ working draft: Class template lock_guard ([thread.lock.guard])"
    url: https://eel.is/c++draft/thread.lock.guard
  - source_id: cppcg-r1
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
  - source_id: cppcg-cp20
    title: "C++ Core Guidelines: CP.20 – Use RAII, never plain lock()/unlock()"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp20-use-raii-never-plain-lockunlock
---

## Short answer

<span class="warn">RAII is the principle of tying a resource to an object's lifetime within a scope, not a feature of smart pointers.</span>

The constructor acquires the resource and the destructor releases it: this is how `std::lock_guard`, which holds a mutex for its lifetime,[^cpp-draft-thread-lock-guard] a custom interrupt guard or a scoped peripheral handle work, with no heap pointer at all. A smart pointer is just one application of the idea, for the `new`/`delete` pair.[^cppcg-r1]

Defense: think of RAII as ctor acquires, dtor releases, not as `unique_ptr`.

## Detailed explanation

TODO
