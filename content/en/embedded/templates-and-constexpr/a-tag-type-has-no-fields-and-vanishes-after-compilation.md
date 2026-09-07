---
id: emb-tmplcx-0021
title: "Why does `Quantity<Tag>` have no runtime overhead?"
description: "The tag type has no fields; it exists only in the type system and disappears after compilation."
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

**The tag type has no fields – it exists only in the type system and completely disappears after compilation.**

The object contains only `Rep value` (e.g. `int32_t`), so `sizeof(Quantity) == sizeof(int32_t)`. Unit compatibility checking costs zero bytes and zero cycles.

Rule: phantom types give unit safety without any runtime cost.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
