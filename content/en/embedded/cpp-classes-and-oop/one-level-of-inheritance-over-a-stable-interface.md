---
id: emb-cppoop-0012
title: "When is inheritance appropriate in embedded and when is it not?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cppcg-c120
    title: "C++ Core Guidelines: C.120 – Use class hierarchies to represent concepts with inherent hierarchical structure (only)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c120-use-class-hierarchies-to-represent-concepts-with-inherent-hierarchical-structure-only
  - source_id: cppcg-c121
    title: "C++ Core Guidelines: C.121 – If a base class is used as an interface, make it a pure abstract class"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c121-if-a-base-class-is-used-as-an-interface-make-it-a-pure-abstract-class
  - source_id: cppcg-c122
    title: "C++ Core Guidelines: C.122 – Use abstract classes as interfaces when complete separation of interface and implementation is needed"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c122-use-abstract-classes-as-interfaces-when-complete-separation-of-interface-and-implementation-is-needed
  - source_id: cppcg-c129
    title: "C++ Core Guidelines: C.129 – When designing a class hierarchy, distinguish between implementation inheritance and interface inheritance"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c129-when-designing-a-class-hierarchy-distinguish-between-implementation-inheritance-and-interface-inheritance
  - source_id: itanium-abi-vtable-components
    title: "Itanium C++ ABI: Virtual Table Components and Order"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#vtable-components
---

## Short answer

**Appropriate**: one level (an interface base plus a few implementations) with a stable interface, when different types are used through one base, e.g. drivers behind a common `Device`.[^cppcg-c120][^cppcg-c122] <span class="warn">Avoid</span> deep hierarchies and bases carrying data: a change to such a base affects every derived class,[^cppcg-c129] and every polymorphic class adds a vtable while every object adds a vptr.[^itanium-abi-vtable-components] Counts like "2–5 types" or "3+ levels" are only rules of thumb; types known at compile time can use composition.

Rule: inheritance for the interface, everything else composition.[^cppcg-c120]

## Detailed explanation

TODO
