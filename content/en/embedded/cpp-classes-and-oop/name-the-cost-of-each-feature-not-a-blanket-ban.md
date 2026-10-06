---
id: emb-cppoop-0037
title: "What should a candidate say about C++ OOP in embedded?"
description: "OOP in embedded: a class without virtual needs no vptr, virtual adds a vptr (RAM) per object and a vtable per class (usually ROM); CRTP gives compile-time polymorphism; composition is the usual default."
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
  - source_id: cpp-core-guidelines-in-aims
    title: "C++ Core Guidelines: In.aims"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#inaims-aims
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "States the zero-overhead principle: what you don't use, you don't pay for, and a properly used abstraction is no worse than hand-written lower-level code. A design principle, not a guarantee for every compiler and every piece of code."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Defines a dynamic class (with virtual functions or virtual bases) as a class that requires a virtual table pointer; so a class without them has none. Describes the vtable as a per-class table. An ABI, not the language standard; does not define the memory section for the vtable."
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "In the Top-level static object construction section: each translation unit provides a fragment of the constructor vector in an .init_array section, each element being the address of a void(void) function that constructs that TU's global objects; run-time support code iterates the vector in increasing address order; the ABI does not specify the order between TUs. An Arm ABI; other architectures and toolchains can differ."
  - source_id: itanium-abi-atexit
    title: "Itanium C++ ABI: DSO Object Destruction API"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#dso-dtor-runtime-api
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Section 3.3.6.3 says that after constructing a global (or local static) object that will need destruction at exit, a termination function is registered through __cxa_atexit. An ABI, not the language standard; does not name a runtime size."
  - source_id: gcc-fexceptions
    title: "GCC 16.1.0: Code Gen Options, -fexceptions"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Code-Gen-Options.html#index-fexceptions
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "States that -fexceptions enables exception handling and generates extra code needed to propagate exceptions; on some targets GCC generates frame unwind information for all functions, which can produce significant data size overhead although it does not affect execution; it is enabled by default for C++. Gives no concrete sizes."
  - source_id: gcc-fno-rtti
    title: "GCC 16.1.0: C++ Dialect Options, -fno-rtti"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/C_002b_002b-Dialect-Options.html#index-fno-rtti
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "States that -fno-rtti disables generation of information about classes with virtual functions for dynamic_cast and typeid; dynamic_cast remains usable for casts that need no RTTI (to void* or to an unambiguous base); mixing code compiled with -frtti and -fno-rtti may not work (for example a link error). Gives no savings in bytes."
  - source_id: libstdcxx-no-exceptions
    title: "libstdc++ manual: Doing without"
    url: https://gcc.gnu.org/onlinedocs/libstdc++/manual/using_exceptions.html#intro.using.exception.no
    accessed: 2026-10-06
    kind: official
    version: "current"
    applicability: "States that -fno-exceptions breaks exceptions passing through such code; user code with throw, try and catch produces errors in this mode; in libstdc++ the throw sites for most exception classes are replaced with abort(). About libstdc++; other libraries can behave differently."
---

## Short answer

**A candidate should name the cost of each C++ feature rather than ban OOP wholesale.**

A class without `virtual` needs no vptr; `virtual` adds a vptr to every object and a vtable per class;[^itanium-cxx-abi] the first costs RAM, the second usually sits in ROM. CRTP and templates give compile-time polymorphism without a vptr; composition is the usual default. Startup and runtime cost too: walking `.init_array` on Arm,[^arm-cpp-abi] atexit registration of global destructors,[^itanium-abi-atexit] and the consequences of `-fno-exceptions`/`-fno-rtti`.[^gcc-fexceptions][^gcc-fno-rtti]

Rule: name the cost in bytes and cycles, not just the syntax.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
