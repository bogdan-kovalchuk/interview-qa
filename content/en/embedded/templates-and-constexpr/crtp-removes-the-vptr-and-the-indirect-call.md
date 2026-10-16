---
id: emb-tmplcx-0012
title: "What are the advantages of CRTP over virtual dispatch?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: cpp-draft-class-virtual
    title: "C++ working draft: Virtual functions ([class.virtual])"
    url: https://eel.is/c++draft/class.virtual
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
  - source_id: cpp-draft-expr-static-cast
    title: "C++ working draft: Static cast ([expr.static.cast])"
    url: https://eel.is/c++draft/expr.static.cast
---

## Short answer

**No mandatory vptr (virtual pointer), no indirect call, and easier WCET (worst-case execution time) analysis.** A class without virtual functions and virtual bases does not need a vptr under the Itanium ABI,[^itanium-cxx-abi] and a non-virtual call is resolved by the static type, so it is a direct call.[^cpp-draft-class-virtual] The vptr size depends on the ABI (application binary interface) and pointer width.

Rule: CRTP – when the type is known at compile time; virtual – when the type is chosen at run time (plugins, dynamic driver loading).

## Detailed explanation

TODO
