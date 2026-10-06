---
id: emb-cppoop-0001
title: "What does \"zero-overhead abstraction\" mean for a C++ class?"
description: "A non-virtual class compiles to the same code as a C struct with free functions when the optimizer sees the method bodies."
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
  - source_id: cpp-draft-expr-prim-this
    title: "C++ working draft: [expr.prim.this] The keyword this"
    url: https://eel.is/c++draft/expr.prim.this
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Confirms that `this` is a pointer to the object for which a non-static member function is invoked; does not define how the ABI passes it."
  - source_id: cpp-draft-class-prop
    title: "C++ working draft: [class.prop] Properties of classes"
    url: https://eel.is/c++draft/class.prop
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Defines standard-layout classes (no virtual functions or virtual bases, same access control for non-static data members, standard-layout members and bases, and further conditions) and notes that such classes are useful for communicating with code in other languages; promises nothing about machine code."
  - source_id: cpp-draft-intro-abstract
    title: "C++ working draft: [intro.abstract] Abstract machine"
    url: https://eel.is/c++draft/intro.abstract
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Confirms that an implementation need not copy the structure of the abstract machine, only its observable behavior; this is what permits a compiler to inline methods. It does not guarantee that it will."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Defines a dynamic class (with virtual functions or virtual bases) as one that requires a virtual table pointer, so a class without them has none. This is an ABI, not the language standard: other ABIs can differ in detail."
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Documents that without optimization GCC does not expand functions inline (-fno-inline is the default), that -finline-small-functions is enabled at -O2, -O3 and -Os, and that -flto lets functions be inlined across object files; the actual heuristic decisions depend on the code."
  - source_id: cpp-core-guidelines
    title: "C++ Core Guidelines: In.aims"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#ss-aims
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "States the zero-overhead principle: what you don't use you don't pay for, and a properly used abstraction performs at least as well as hand-written lower-level code. It is a design principle, not a guarantee for every compiler and piece of code."
---

## Short answer

**A non-virtual class can compile to the same machine code as a C struct with free functions, provided the optimizer sees the method bodies.**

A non-static member function receives an implicit `this`;[^cpp-draft-expr-prim-this] in typical ABIs a class without `virtual` has no vptr/vtable,[^itanium-cxx-abi] and simple methods are usually inlined. At `-O0` or across separate translation units (without LTO), the call may remain a regular call.[^gcc-optimize-options]

Rule: encapsulation via a class in embedded is usually free in a release build, as long as there are no virtual functions or extra state.[^cpp-core-guidelines]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
