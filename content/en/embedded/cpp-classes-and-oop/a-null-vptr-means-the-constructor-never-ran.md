---
id: emb-cppoop-0026
title: "Trap: you see a null vptr in a global object. What is the cause?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
  - source_id: cpp-draft-basic-start-static
    title: "C++ working draft: Static initialization ([basic.start.static])"
    url: https://eel.is/c++draft/basic.start.static
  - source_id: cpp-draft-basic-start-dynamic
    title: "C++ working draft: Dynamic initialization of non-block variables ([basic.start.dynamic])"
    url: https://eel.is/c++draft/basic.start.dynamic
  - source_id: itanium-abi-ctor-vptr
    title: "Itanium C++ ABI: Virtual tables During Object Construction"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#vtable-ctor-general
---

## Short answer

<span class="warn">The most common cause is that startup did not run the constructors of global objects listed in `.init_array`.</span>[^arm-cpp-abi] An object that needs dynamic initialization is otherwise only zero-initialized, and the vptr of a polymorphic object is normally set by its constructor,[^cpp-draft-basic-start-static][^itanium-abi-ctor-vptr] so the first virtual call goes through a null vptr – undefined behavior, in practice usually a fault. Protection: make sure startup walks `.init_array` before `main()`; a null vptr also appears when an object is used before its constructor has run.

## Detailed explanation

TODO
