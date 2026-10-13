---
id: emb-tmplcx-0001
title: "What is a function template and why is it better than a macro?"
description: "A function template is one type-safe definition for any type that supports the operations it uses."
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
  - source_id: cpp-draft-cpp-replace
    title: "C++ working draft: Replacement of macros ([cpp.replace])"
    url: https://eel.is/c++draft/cpp.replace
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "A macro replaces the parameter with the argument's preprocessing token sequence, not its value; the # (stringizing) and ## (token pasting) operators are defined in this section. Does not describe any particular preprocessor."
  - source_id: cpp-draft-expr-call
    title: "C++ working draft: Function call ([expr.call])"
    url: https://eel.is/c++draft/expr.call
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "When a function is called, each parameter is initialized from its corresponding argument, so the argument's value is copied into the parameter. This section does not settle the order of argument evaluation."
  - source_id: cpp-draft-temp-deduct-call
    title: "C++ working draft: Deducing template arguments from a function call ([temp.deduct.call])"
    url: https://eel.is/c++draft/temp.deduct.call
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "If arguments give different deduced types for the same T, deduction fails; the standard's example shows `error: conflicting deductions for T`. Does not describe any particular compiler's message."
---

## Question code

```cpp
template<typename T>
T clamp(T v, T lo, T hi) {
  return v < lo ? lo : (v > hi ? hi : v);
}
```

## Short answer

**One definition that works for any type that supports the operations its body uses, with full type checking.**

Unlike a macro, which only substitutes argument text,[^cpp-draft-cpp-replace] a function template evaluates each argument exactly once, without double evaluation.[^cpp-draft-expr-call] If the arguments give different deduced types for T, the call is rejected.[^cpp-draft-temp-deduct-call]

Rule: a function template is usually the better choice over a function-like macro, but macros remain necessary for stringizing (`#`) and token pasting (`##`).[^cpp-draft-cpp-replace][^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
