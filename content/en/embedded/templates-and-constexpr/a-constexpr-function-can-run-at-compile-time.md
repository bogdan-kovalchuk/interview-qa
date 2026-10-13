---
id: emb-tmplcx-0005
title: "What is a constexpr function?"
description: "A function that can be called in a constant expression; there it is evaluated at compile time."
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
    title: "C++ working draft: The constexpr specifier ([dcl.constexpr])"
    url: https://eel.is/c++draft/dcl.constexpr
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Defines that a constexpr function call gives the same result as an equivalent non-constexpr call but may appear in a constant expression, and that a constexpr variable must be constant-initializable; says nothing about where the result is placed."
  - source_id: cpp-draft-basic-start-static
    title: "C++ working draft: Static initialization ([basic.start.static])"
    url: https://eel.is/c++draft/basic.start.static
    accessed: 2026-10-13
    kind: spec
    version: "working draft"
    applicability: "Defines constant initialization of static-storage variables: it is not dynamic initialization and needs no code run at startup; says nothing about the memory segment on a target board."
---

## Short answer

**A function that can be called in a constant expression; in such a context it is evaluated at compile time, elsewhere it is an ordinary call.**

A call to a constexpr function gives the same result as a call to an equivalent non-constexpr function, but it can appear in a constant expression.[^cpp-draft-dcl-constexpr] A constexpr variable must be constant-initializable, so it needs no dynamic initialization at startup.[^cpp-draft-basic-start-static]

Rule: `constexpr` does not guarantee compile-time evaluation of every call; a constant context, such as `static_assert`, is required.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
