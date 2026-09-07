---
id: emb-tmplcx-0001
title: "What is a function template and why is it better than a macro?"
description: "A function template is one type-safe definition that works for any type."
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
template<typename T>
T clamp(T v, T lo, T hi) {
  return v < lo ? lo : (v > hi ? hi : v);
}
```

## Short answer

**One definition that works for any type, with full type checking.**

Unlike a macro: type safety, arguments are evaluated exactly once (no double evaluation), full debugging, proper error messages, overload resolution.

Rule: a function template is the modern replacement for a function-like macro.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
