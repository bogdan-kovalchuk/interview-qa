---
id: emb-cppoop-0007
title: "What is RAII in terms of constructors and destructors?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
  - source_id: cpp-draft-except-ctor
    title: "C++ working draft: Stack unwinding ([except.ctor])"
    url: https://eel.is/c++draft/except.ctor
  - source_id: cpp-draft-support-start-term
    title: "C++ working draft: Start and termination ([support.start.term])"
    url: https://eel.is/c++draft/support.start.term
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
  - source_id: cppcg-c21-special-members
    title: "C++ Core Guidelines: C.21 – If you define or =delete any copy, move, or destructor function, define or =delete them all"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c21-if-you-define-or-delete-any-copy-move-or-destructor-function-define-or-delete-them-all
---

## Short answer

**RAII (Resource Acquisition Is Initialization): the constructor acquires/configures the resource, the destructor automatically releases it when the object is destroyed – for a local object, on scope exit.**[^cpp-draft-class-dtor][^cppcg-r1-raii] For example: the ctor enables a clock and configures the peripheral, the dtor disables the clock or frees a DMA (direct memory access) channel. The compiler itself calls the dtor on every path out of the block, including an exception, so forgetting deinitialization is harder.[^cpp-draft-except-ctor] But `abort()` runs no destructors, and for static objects they run only on normal program termination.[^cpp-draft-support-start-term]

## Detailed explanation

TODO
