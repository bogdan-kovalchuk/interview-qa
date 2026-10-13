---
id: emb-tmplcx-0003
title: "What does a class template for a fixed-size buffer look like?"
description: "Type and size are template parameters; the array is part of the object, with no dynamic memory."
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
  - source_id: cpp-draft-temp-arg-nontype
    title: "C++ working draft: Constant template arguments ([temp.arg.nontype])"
    url: https://eel.is/c++draft/temp.arg.nontype
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Requires an argument for a non-type (constant) template parameter to satisfy the rules for a constexpr variable with static storage, i.e. to be a constant expression; says nothing about object placement."
  - source_id: cpp-draft-basic-stc-auto
    title: "C++ working draft: [basic.stc.auto]"
    url: https://eel.is/c++draft/basic.stc.auto
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Defines automatic storage duration for block-scope variables; says nothing about how the stack is implemented on a given platform."
  - source_id: cpp-draft-basic-stc-static
    title: "C++ working draft: Static storage duration ([basic.stc.static])"
    url: https://eel.is/c++draft/basic.stc.static
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Defines static storage duration for namespace-scope variables; says nothing about the memory segment on a target board."
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

## Sources

<!-- generated from frontmatter -->
