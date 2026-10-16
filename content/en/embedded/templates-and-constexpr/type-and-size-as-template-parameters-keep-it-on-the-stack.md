---
id: emb-tmplcx-0003
title: "What does a class template for a fixed-size buffer look like?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-temp-arg-nontype
    title: "C++ working draft: Constant template arguments ([temp.arg.nontype])"
    url: https://eel.is/c++draft/temp.arg.nontype
  - source_id: cpp-draft-basic-stc-auto
    title: "C++ working draft: [basic.stc.auto]"
    url: https://eel.is/c++draft/basic.stc.auto
  - source_id: cpp-draft-basic-stc-static
    title: "C++ working draft: Static storage duration ([basic.stc.static])"
    url: https://eel.is/c++draft/basic.stc.static
---

## Question code

```cpp
template<typename T, size_t N>
class CircularBuffer {
  T buf_[N];
  size_t head_ = 0, tail_ = 0;
};
CircularBuffer<uint8_t, 64> uart_rx;
```

## Short answer

**Type and size are template parameters, so the array `buf_[N]` is part of the object, with no `new` or `malloc`.**

The value of `N` must be a compile-time constant.[^cpp-draft-temp-arg-nontype] Where the object lives depends on its declaration: a local object has automatic storage,[^cpp-draft-basic-stc-auto] while `uart_rx` at namespace scope has static storage.[^cpp-draft-basic-stc-static]

## Detailed explanation

TODO
