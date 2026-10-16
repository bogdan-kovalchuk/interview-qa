---
id: emb-cppoop-0019
title: "What is polymorphism through a `Sensor*` array for?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-conv-ptr
    title: "C++ working draft: Pointer conversions ([conv.ptr])"
    url: https://eel.is/c++draft/conv.ptr
  - source_id: cpp-draft-expr-call
    title: "C++ working draft: Function call ([expr.call])"
    url: https://eel.is/c++draft/expr.call
  - source_id: cpp-draft-class-virtual
    title: "C++ working draft: Virtual functions ([class.virtual])"
    url: https://eel.is/c++draft/class.virtual
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
---

## Short answer

**A heterogeneous collection: different concrete types behind a common interface in one array/container.**

```cpp
Sensor* arr[] = { &temp, &pressure, &humid };
for (auto s : arr) s->read();
```

A call through a base pointer runs the final overrider for the dynamic type of the object,[^cpp-draft-expr-call] and this is typically implemented with a vptr and a vtable.[^itanium-cxx-abi]

Rule: when you need to hold different types together and call them uniformly, virtual is the classic choice, though not the only one (tagged unions or a table of function pointers are others).

## Detailed explanation

TODO
