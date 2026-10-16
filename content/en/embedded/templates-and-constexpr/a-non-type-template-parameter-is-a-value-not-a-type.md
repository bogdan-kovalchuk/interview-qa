---
id: emb-tmplcx-0004
title: "What is a non-type template parameter (NTTP)?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-temp-param
    title: "C++ working draft: Template parameters ([temp.param])"
    url: https://eel.is/c++draft/temp.param
  - source_id: cpp-draft-temp-arg-nontype
    title: "C++ working draft: Constant template arguments ([temp.arg.nontype])"
    url: https://eel.is/c++draft/temp.arg.nontype
  - source_id: cpp-draft-expr-add
    title: "C++ working draft: Additive operators ([expr.add])"
    url: https://eel.is/c++draft/expr.add
---

## Short answer

**A template parameter that is a value, not a type, e.g. `size_t N`.**[^cpp-draft-temp-param]

In `CircularBuffer<T, N>` the size `N` is an NTTP: its argument must be a constant expression, so the array `buf_[N]` has a size known at compile time.[^cpp-draft-temp-arg-nontype] Rule: an NTTP writes a size or configuration into the type, so `CircularBuffer<uint8_t, 64>` and `CircularBuffer<uint8_t, 128>` are different types.[^iso-cpp-n4861]

## Detailed explanation

TODO
