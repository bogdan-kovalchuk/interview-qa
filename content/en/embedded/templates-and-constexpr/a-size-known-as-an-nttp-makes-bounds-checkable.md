---
id: emb-tmplcx-0029
title: "How does constexpr give compile-time bounds checking?"
description: "When the size is an NTTP, indices and bounds can be checked with staticassert at compile time."
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

## Short answer

**When the size is an NTTP, indices and bounds can be checked with `static_assert` at compile time.**

For example, `get<I>()` with `static_assert(I < N, "out of range")` turns an out-of-bounds access into a compile error instead of a runtime bug.

Rule: move bounds checking into compile time wherever the index or size is statically known.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
