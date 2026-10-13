---
id: emb-tmplcx-0011
title: "What is CRTP and what is it for in templates?"
description: "CRTP is a pattern where a base class template is parameterized by the derived class: class Derived : public Base<Derived>."
track: embedded
section: templates-and-constexpr
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-13; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: cpp-draft-expr-static-cast
    title: "C++ working draft: Static cast ([expr.static.cast])"
    url: https://eel.is/c++draft/expr.static.cast
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says a pointer to a base that is a subobject of a D object can be converted by static_cast to a pointer to D; if the base is not a subobject of D, the behavior is undefined."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Defines a dynamic class as one that needs a virtual table pointer because it or its bases have virtual member functions or virtual base classes; a class without them has no vptr. This is the ABI, not the language standard; other ABIs can differ in detail."
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says implicit instantiation of a class template specialization instantiates its declarations, but member function definitions are instantiated only when their definition is needed. Says nothing about code size."
---

## Question code

```cpp
template<typename D>
class SensorBase {
public:
  int read_filtered() {
    int raw = static_cast<D*>(this)->read_raw();
    return (raw + last_) / 2;
  }
private:
  int last_ = 0;
};
```

## Short answer

**CRTP (curiously recurring template pattern): the base is a template parameterized by the derived class: `class Derived : public Base<Derived>`.**

The base calls the derived class's member through `static_cast<D*>(this)`; such a downcast is valid only when the base is a subobject of a real `D`.[^cpp-draft-expr-static-cast] A class without virtual functions has no vptr.[^itanium-cxx-abi] So there is no vtable for it, and `D` is known at compile time.

Rule: CRTP gives static polymorphism without virtual dispatch, but does not fit when the type is chosen at run time.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
