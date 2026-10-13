---
id: emb-tmplcx-0007
title: "What is the difference between `const` and `constexpr`?"
description: "const means read-only but the value may be computed at runtime; constexpr means usable as a constant expression."
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
  - source_id: cpp-draft-dcl-constexpr
    title: "C++ working draft: The constexpr and consteval specifiers ([dcl.constexpr])"
    url: https://eel.is/c++draft/dcl.constexpr
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says a constexpr object is declared const and must be constant-initializable, so a non-constant initializer is ill-formed. Says nothing about storage placement in Flash or RAM."
  - source_id: cpp-draft-expr-const
    title: "C++ working draft: Constant expressions ([expr.const])"
    url: https://eel.is/c++draft/expr.const
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Defines constant-initializable variables, which are constant-initialized when they have an initializer. Potentially-constant variables are constexpr objects, references, and non-volatile const integral or enumeration types, so a const float is not usable in constant expressions. Says nothing about memory placement."
  - source_id: cpp-draft-basic-start-static
    title: "C++ working draft: Static initialization ([basic.start.static])"
    url: https://eel.is/c++draft/basic.start.static
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Defines constant initialization for static-storage objects and says all other initialization is dynamic. Does not say whether the data lives in Flash or RAM."
  - source_id: cpp-draft-basic-start-dynamic
    title: "C++ working draft: Dynamic initialization of non-block variables ([basic.start.dynamic])"
    url: https://eel.is/c++draft/basic.start.dynamic
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says that for a non-block, non-inline variable with static storage whose dynamic initialization is needed, the implementation decides whether it is sequenced before the first statement of main or deferred."
---

## Short answer

**`const` means "I will not modify it", but the value may be computed at runtime. `constexpr` means "can be a constant expression".**

For embedded, `constexpr` is stronger: an initializer that is not a constant expression is a compile error.[^cpp-draft-dcl-constexpr] A `constexpr` variable with static storage is initialized statically, with no dynamic initialization at startup.[^cpp-draft-expr-const][^cpp-draft-basic-start-static]

Rule: for compile-time constants and tables use `constexpr`, not just `const`.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
