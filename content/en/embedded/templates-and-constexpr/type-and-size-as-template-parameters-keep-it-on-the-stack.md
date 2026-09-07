---
id: emb-tmplcx-0003
title: "What does a class template for a fixed-size buffer look like?"
description: "Type and size are template parameters, so the buffer lives on the stack without heap."
track: embedded
section: templates-and-constexpr
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
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

**Type and size are template parameters, so the buffer lives on the stack without heap.**

Size `N` is known at compile time, array `buf_[N]` is embedded in the object. No `malloc`, optimal sizing, no runtime flexibility.

Rule: parameterize containers by type and size – you get a heap-free structure with type safety.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
