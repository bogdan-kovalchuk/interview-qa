---
id: emb-tmplcx-0011
title: "What is CRTP and what is it for in templates?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-expr-static-cast
    title: "C++ working draft: Static cast ([expr.static.cast])"
    url: https://eel.is/c++draft/expr.static.cast
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
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
