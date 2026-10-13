---
id: emb-tmplcx-0004
title: "What is a non-type template parameter (NTTP)?"
description: "A template parameter that is a value, not a type, e.g. size_t N."
track: embedded
section: templates-and-constexpr
level: junior
type: concept
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
  - source_id: cpp-draft-temp-param
    title: "C++ working draft: Template parameters ([temp.param])"
    url: https://eel.is/c++draft/temp.param
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Defines a constant template parameter (a value parameter) as a kind of template parameter; does not list the value types a given compiler accepts."
  - source_id: cpp-draft-temp-arg-nontype
    title: "C++ working draft: Constant template arguments ([temp.arg.nontype])"
    url: https://eel.is/c++draft/temp.arg.nontype
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Requires an argument for a non-type (constant) template parameter to satisfy the rules for a constexpr variable with static storage, i.e. to be a constant expression; says nothing about object placement."
  - source_id: cpp-draft-expr-add
    title: "C++ working draft: Additive operators ([expr.add])"
    url: https://eel.is/c++draft/expr.add
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Defines pointer arithmetic that goes outside an array of n elements (other than one past the last element) as undefined behavior; does not describe compiler diagnostics."
---

## Short answer

**A template parameter that is a value, not a type, e.g. `size_t N`.**[^cpp-draft-temp-param]

In `CircularBuffer<T, N>` the size `N` is an NTTP: its argument must be a constant expression, so the array `buf_[N]` has a size known at compile time.[^cpp-draft-temp-arg-nontype] Rule: an NTTP writes a size or configuration into the type, so `CircularBuffer<uint8_t, 64>` and `CircularBuffer<uint8_t, 128>` are different types.[^iso-cpp-n4861]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
