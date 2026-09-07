---
id: emb-tmplcx-0012
title: "What are the advantages of CRTP over virtual dispatch?"
description: "No mandatory vptr, no indirect call, and easier WCET analysis compared to virtual dispatch."
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

**No mandatory vptr (virtual pointer), no indirect call, and easier WCET (worst-case execution time) analysis.**

After optimization the generated assembly often reduces to a direct call; the interface is checked at compile time (missing method = compile error). The vptr size depends on the ABI (application binary interface) and pointer width.

Rule: CRTP – for sensors in ISR (interrupt service routine) and tight control loops; virtual – when runtime polymorphism is needed (plugins, dynamic driver loading).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
