---
id: emb-tmplcx-0015
title: "What strategies are there against template code bloat?"
description: "Thin wrapper over void pointer, limiting instantiations, extern template, non-template base, and LTO."
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

**Thin wrapper over `void*`; limiting the number of instantiations; `extern template`; extracting T-independent code into a non-template base; LTO (link-time optimization).**

The idea: keep only a thin type-safe layer in the template, and the shared implementation – outside the template (via `void*` + `sizeof(T)` or a base class).

Rule: factor out everything that does not depend on `T` into non-template code.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
