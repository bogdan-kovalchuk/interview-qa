---
id: emb-tmplcx-0028
title: "Why are templates usually header-only?"
description: "The compiler needs the full definition of a template in every translation unit to instantiate it for specific types."
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

**The compiler needs the full definition of a template in every TU (translation unit) to instantiate it for specific types.**

If the definition is hidden in a `.cpp`, other translation units cannot generate the required instantiation -> linker error. That is why templates go into headers.

Rule: template definitions belong in headers; use `extern template` to control instantiation.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
