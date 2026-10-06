---
id: emb-cppoop-0027
title: "Does a class without any virtual function still pay virtual overhead?"
description: "Without virtual functions and virtual bases a class has neither a vtable nor a vptr and pays no overhead"
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
  - source_id: cpp-draft-expr-sizeof
    title: "C++ working draft: [expr.sizeof] Sizeof"
    url: https://eel.is/c++draft/expr.sizeof
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "States that for a class sizeof is the number of bytes in an object of that class including any padding needed to place such objects in an array, and that the amount and placement of padding is a property of the implementation. Gives no concrete values."
  - source_id: iso-tr-18015
    title: "ISO/IEC TR 18015:2006 Technical Report on C++ Performance"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/TR18015.pdf
    accessed: 2026-10-06
    kind: spec
    version: "TR 18015:2006"
    applicability: "Section 5.3.1 says a class without a virtual function needs as much space as a struct with the same fields (apart from possible padding), a non-virtual function takes no space in the object, and a polymorphic class pays one pointer per object plus a table per class. Section 5.3.6: a virtual base adds overhead compared with an ordinary base (the subobject position is dynamic, typically through a pointer). A 2006 report: sizes depend on the implementation."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Defines a dynamic class (with virtual functions or virtual bases, its own or inherited) as one that requires a virtual table pointer, so a class without them has none. This is an ABI, not the language standard: other ABIs can differ in detail."
---

## Short answer

**No – a class that neither has nor inherits any virtual function or virtual base has neither a vptr nor a vtable.**[^itanium-cxx-abi] Its object takes as much space as a C struct with the same fields (with possible padding), and a non-virtual method adds nothing to the object.[^iso-tr-18015] The overhead appears with the first virtual function or virtual base: a vptr in every object and a vtable per class. Rule: encapsulate freely; you pay for polymorphism only when you declare `virtual`.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
