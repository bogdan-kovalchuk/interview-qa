---
id: emb-cppoop-0010
title: "Trap: why is a dependency between globals in different `.cpp` files dangerous?"
description: "The C++ standard does not define construction order of globals across translation units, leading to the static initialization order fiasco."
track: embedded
section: cpp-classes-and-oop
level: junior
type: pitfall
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
  - source_id: cpp-draft-basic-start-dynamic
    title: "C++ working draft: Dynamic initialization of non-block variables ([basic.start.dynamic])"
    url: https://eel.is/c++draft/basic.start.dynamic
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Defines the order of dynamic initialization: within one translation unit it follows the order of definitions; for variables defined in different translation units there is no ordering (indeterminately sequenced when no other threads exist). Inline variables and template specializations follow other rules (partially-ordered, unordered). Says nothing about the order of calls in a particular startup code."
  - source_id: cpp-draft-basic-start-static
    title: "C++ working draft: Static initialization ([basic.start.static])"
    url: https://eel.is/c++draft/basic.start.static
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "States that a variable with static storage duration is either constant-initialized or zero-initialized, and that all static initialization strongly happens before any dynamic initialization."
  - source_id: cpp-draft-basic-life
    title: "C++ working draft: Object lifetime ([basic.life])"
    url: https://eel.is/c++draft/basic.life
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "States that an object's lifetime begins when its initialization is complete, and that accessing a non-static member or calling a non-static member function through a pointer or glvalue before the lifetime starts is undefined behavior. Does not describe what the program will actually see in memory."
  - source_id: cpp-draft-stmt-dcl
    title: "C++ working draft: Declaration statement ([stmt.dcl])"
    url: https://eel.is/c++draft/stmt.dcl
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "States that dynamic initialization of a block variable with static storage duration is performed the first time control passes through its declaration; concurrent entry waits for completion; recursive entry is undefined behavior."
  - source_id: cpp-draft-dcl-constinit
    title: "C++ working draft: The constinit specifier ([dcl.constinit])"
    url: https://eel.is/c++draft/dcl.constinit
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "States that a constinit variable that would have dynamic initialization makes the program ill-formed, so constinit guarantees initialization during static initialization. This is C++20; earlier standards have no such specifier."
  - source_id: gcc-cxx-init-priority
    title: "GCC: C++ Attributes, init_priority"
    url: https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Attributes.html#index-init_005fpriority
    accessed: 2026-10-06
    kind: official
    version: "current"
    applicability: "States that in standard C++ initialization order within one translation unit follows the order of definitions while nothing is guaranteed across translation units; the init_priority attribute is a GNU C++ extension for controlling the order, and some targets reject it with an error."
  - source_id: gcc-cxx-threadsafe-statics
    title: "GCC: C++ Dialect Options, -fno-threadsafe-statics"
    url: https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html#index-fthreadsafe-statics
    accessed: 2026-10-06
    kind: official
    version: "current"
    applicability: "States that -fno-threadsafe-statics removes the extra code for thread-safe initialization of local statics defined by the C++ ABI and slightly reduces code size when thread safety is not needed. Gives no exact byte saving."
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "In the Top-level static object construction section: the ABI does not specify a way to control the order in which translation units are initialized. This is the Arm ABI; other targets may have their own rules."
---

## Short answer

<span class="warn">The C++ standard does not define the construction order of globals across translation units</span> (static initialization order fiasco): only the order within one translation unit is guaranteed.[^cpp-draft-basic-start-dynamic][^gcc-cxx-init-priority]

If a global from `a.cpp` uses a global from `b.cpp` in its constructor, the latter may not yet be constructed, and accessing an object before its lifetime has begun is undefined behavior.[^cpp-draft-basic-life]

Protection: avoid cross-module global dependencies; use a function-local static (lazy init the first time control passes through its declaration),[^cpp-draft-stmt-dcl] `constinit` objects (C++20)[^cpp-draft-dcl-constinit] or an explicit init sequence.

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
