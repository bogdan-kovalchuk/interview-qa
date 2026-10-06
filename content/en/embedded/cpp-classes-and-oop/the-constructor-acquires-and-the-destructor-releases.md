---
id: emb-cppoop-0007
title: "What is RAII in terms of constructors and destructors?"
description: "RAII ties resource lifetime to object lifetime: the constructor acquires the resource, the destructor releases it when the object is destroyed, for a local object on scope exit."
track: embedded
section: cpp-classes-and-oop
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-06; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines when a destructor is invoked implicitly: for an automatic object on block exit, for a static object at program termination; says nothing about specific hardware resources."
  - source_id: cpp-draft-except-ctor
    title: "C++ working draft: Stack unwinding ([except.ctor])"
    url: https://eel.is/c++draft/except.ctor
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Describes destruction of automatic objects in reverse order when an exception is thrown, and that an exception from a constructor runs destructors for already initialized subobjects; does not apply when exceptions are disabled by the compiler."
  - source_id: cpp-draft-support-start-term
    title: "C++ working draft: Start and termination ([support.start.term])"
    url: https://eel.is/c++draft/support.start.term
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that std::abort terminates the program without running destructors and that std::exit does not destroy automatic objects; freestanding implementations may not provide these functions."
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: wrap a resource with paired acquire/release in an object that acquires in the constructor and releases in the destructor; its examples are files, mutexes and memory, not hardware peripherals."
  - source_id: cppcg-c21-special-members
    title: "C++ Core Guidelines: C.21 – If you define or =delete any copy, move, or destructor function, define or =delete them all"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c21-if-you-define-or-delete-any-copy-move-or-destructor-function-define-or-delete-them-all
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: a declared destructor calls for a deliberate decision about copying and moving; explains how such declarations affect the implicit functions."
---

## Short answer

**RAII (Resource Acquisition Is Initialization): the constructor acquires/configures the resource, the destructor automatically releases it when the object is destroyed – for a local object, on scope exit.**[^cpp-draft-class-dtor][^cppcg-r1-raii] For example: the ctor enables a clock and configures the peripheral, the dtor disables the clock or frees a DMA (direct memory access) channel. The compiler itself calls the dtor on every path out of the block, including an exception, so forgetting deinitialization is harder.[^cpp-draft-except-ctor] But `abort()` runs no destructors, and for static objects they run only on normal program termination.[^cpp-draft-support-start-term]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
