---
id: emb-cppoop-0010
title: "Trap: why is a dependency between globals in different `.cpp` files dangerous?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-basic-start-dynamic
    title: "C++ working draft: Dynamic initialization of non-block variables ([basic.start.dynamic])"
    url: https://eel.is/c++draft/basic.start.dynamic
  - source_id: cpp-draft-basic-start-static
    title: "C++ working draft: Static initialization ([basic.start.static])"
    url: https://eel.is/c++draft/basic.start.static
  - source_id: cpp-draft-basic-life
    title: "C++ working draft: Object lifetime ([basic.life])"
    url: https://eel.is/c++draft/basic.life
  - source_id: cpp-draft-stmt-dcl
    title: "C++ working draft: Declaration statement ([stmt.dcl])"
    url: https://eel.is/c++draft/stmt.dcl
  - source_id: cpp-draft-dcl-constinit
    title: "C++ working draft: The constinit specifier ([dcl.constinit])"
    url: https://eel.is/c++draft/dcl.constinit
  - source_id: gcc-cxx-init-priority
    title: "GCC: C++ Attributes, init_priority"
    url: https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Attributes.html#index-init_005fpriority
  - source_id: gcc-cxx-threadsafe-statics
    title: "GCC: C++ Dialect Options, -fno-threadsafe-statics"
    url: https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html#index-fthreadsafe-statics
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
---

## Short answer

<span class="warn">The C++ standard does not define the construction order of globals across translation units</span> (static initialization order fiasco): only the order within one translation unit is guaranteed.[^cpp-draft-basic-start-dynamic][^gcc-cxx-init-priority]

If a global from `a.cpp` uses a global from `b.cpp` in its constructor, the latter may not yet be constructed, and accessing an object before its lifetime has begun is undefined behavior.[^cpp-draft-basic-life]

Protection: avoid cross-module global dependencies; use a function-local static (lazy init the first time control passes through its declaration),[^cpp-draft-stmt-dcl] `constinit` objects (C++20)[^cpp-draft-dcl-constinit] or an explicit init sequence.

## Detailed explanation

TODO
