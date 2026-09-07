---
id: emb-tmplcx-0027
title: "How is `static_assert` used with templates?"
description: "Compile-time checking of type and size invariants with a clear message."
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

## Short answer

**Compile-time checking of type and size invariants with a clear message.**

For example, in the default branch of `if constexpr`: `static_assert(always_false<P>, "Unsupported platform")` catches an unsupported type at compile time. Also `static_assert(N > 0, "...")` validates an NTTP.

Rule: `static_assert` is the primary tool for turning incorrect template usage into a clear error.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
