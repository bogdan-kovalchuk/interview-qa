---
id: emb-tmplcx-0008
title: "Why is a `constexpr` variable better than a `#define` constant?"
description: "A constexpr variable has type and scope, making it type-safe unlike textual substitution."
track: embedded
section: templates-and-constexpr
level: junior
type: concept
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
constexpr int MAX_SENSORS = 16;
// vs  #define MAX_SENSORS 16
```

## Short answer

**It has type and scope – type-safe, unlike textual substitution.**

A `constexpr` variable is initialized at compile time, visible to the debugger, respects namespace and participates in type checking. `#define` is just text with no type.

Rule: integer compile-time constants in C++ are `constexpr`, not `#define`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
