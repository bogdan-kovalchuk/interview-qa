---
id: emb-raii-0023
title: "Why should a custom deleter be stateless?"
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
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
---

## Short answer

**A stateless deleter type (a lambda without capture or an empty functor) may occupy no space in `unique_ptr` thanks to empty base optimization.**

A capturing lambda carries state and has nonzero size, so it increases `unique_ptr`.[^cpp-draft-intro-object] A function pointer deleter has no class state, but its value must still be stored next to the pointer, so the size usually becomes two pointers.[^cpp-draft-unique-ptr-single]

Rule: a deleter without runtime state -> `unique_ptr` can stay the size of a raw pointer; a function pointer deleter is simple but not size-free.[^itanium-cxx-abi]

## Detailed explanation

TODO
