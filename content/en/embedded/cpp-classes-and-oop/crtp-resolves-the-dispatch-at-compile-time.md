---
id: emb-cppoop-0020
title: "What is CRTP and which problem does it solve?"
track: embedded
section: cpp-classes-and-oop
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
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
---

## Question code

```cpp
template <typename D>
class SensorBase {
public:
  int16_t read() {
    return static_cast<D*>(this)->read_impl();
  }
};
```

## Short answer

**Curiously Recurring Template Pattern – compile-time polymorphism** via `static_cast` to the derived type.

The derived class inherits `SensorBase<Derived>`, and `read()` calls `read_impl()` as an ordinary (non-virtual) function, so no vptr or vtable is needed for it.[^itanium-cxx-abi] The optimizer may inline such a call, but without optimization (`-O0`) GCC does not inline functions.[^gcc-optimize-options] The `static_cast` is valid only when the object really has type `Derived`, otherwise it is undefined behavior.[^cpp-draft-expr-static-cast]

Rule: CRTP removes the dispatch cost (vptr, indirect call), but does not guarantee zero overhead overall.

## Detailed explanation

TODO
