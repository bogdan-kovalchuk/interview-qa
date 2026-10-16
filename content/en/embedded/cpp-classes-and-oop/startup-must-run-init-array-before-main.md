---
id: emb-cppoop-0008
title: "Trap: when do global constructors run and what must startup do?"
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
  - source_id: gnu-ld-manual-sections
    title: "GNU ld manual: SECTIONS and input section description"
    url: https://sourceware.org/binutils/docs/ld.html
  - source_id: gcc-int-initialization
    title: "GCC Internals: How Initialization Functions Are Handled"
    url: https://gcc.gnu.org/onlinedocs/gccint/Initialization.html
---

## Short answer

<span class="warn">Constructors of global objects that need dynamic initialization are run by functions listed in the `.init_array` section; run-time support code (on bare metal, your startup code) must walk that array before `main()`.</span>[^arm-cpp-abi] If it does not, such an object stays merely zero-initialized, and the vptr of a polymorphic object is normally set by its constructor.[^cpp-draft-basic-start-static][^itanium-abi-ctor-vptr] The standard itself leaves it implementation-defined whether this initialization happens before the first statement of `main()`.[^cpp-draft-basic-start-dynamic]

Protection: make sure startup iterates `.init_array` before `main()`; this is a common bug when porting C++ to bare metal.

## Detailed explanation

TODO
