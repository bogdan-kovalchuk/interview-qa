---
id: emb-cppstl-0029
title: "Why is `enum class` better than a plain `enum` for statuses?"
description: "enum class is scoped and strongly typed so it does not implicitly convert to int or pollute the namespace."
track: embedded
section: cpp-embedded-constraints-and-stl
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

## Short answer

**Scoped and strongly typed: it does not implicitly convert to `int` and does not pollute the namespace.**

`Status::Ok` cannot be confused with another enum, and `if (status)` does not accidentally compile. This catches an entire class of comparison/conversion bugs.

Rule: for error codes and statuses use `enum class`, not a bare `enum`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
