---
id: emb-cppoop-0027
title: "Does a class without any virtual function still pay virtual overhead?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-expr-sizeof
    title: "C++ working draft: [expr.sizeof] Sizeof"
    url: https://eel.is/c++draft/expr.sizeof
  - source_id: iso-tr-18015
    title: "ISO/IEC TR 18015:2006 Technical Report on C++ Performance"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/TR18015.pdf
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
---

## Short answer

**No – a class that neither has nor inherits any virtual function or virtual base has neither a vptr nor a vtable.**[^itanium-cxx-abi] Its object takes as much space as a C struct with the same fields (with possible padding), and a non-virtual method adds nothing to the object.[^iso-tr-18015] The overhead appears with the first virtual function or virtual base: a vptr in every object and a vtable per class. Rule: encapsulate freely; you pay for polymorphism only when you declare `virtual`.

## Detailed explanation

TODO
