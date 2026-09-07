---
id: emb-tmplcx-0022
title: "Templates versus macros: what are the key differences?"
description: "Templates offer full type checking and constexpr evaluation; macros are text substitution with double evaluation."
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

**Templates: full type checking, arguments evaluated once, debuggable, constexpr evaluation. Macros: text, double evaluation, only preprocessor output.**

Cost: templates risk code bloat (a copy per instantiation) and slower builds; macros are fast and portable to C89 but unsafe.

Rule: in C++ choose templates for type safety; keep macros for what templates cannot do (`#`/`##`, conditional compilation).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
