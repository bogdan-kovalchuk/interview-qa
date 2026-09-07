---
id: emb-cppoop-0012
title: "When is inheritance appropriate in embedded and when is it not?"
description: "Appropriate for one-level interfaces with few types and a stable contract; avoid deep hierarchies and tight ROM budgets"
track: embedded
section: cpp-classes-and-oop
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

**Appropriate**: one level of depth (base interface + concrete implementations), few types (2–5), stable interface.

<span class="warn">Avoid</span>: deep hierarchies (3+ levels) -> fragile coupling; frequent interface changes cascade through the tree; tight ROM budget where vtable overhead matters.

Rule: one level of abstraction – inheritance; everything else – composition.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
