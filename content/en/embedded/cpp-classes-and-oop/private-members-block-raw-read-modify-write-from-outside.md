---
id: emb-cppoop-0030
title: "Why do private members matter for correct register handling?"
description: "Private members prevent external raw read-modify-write that would bypass class invariants"
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

**They prevent external code from performing raw read-modify-write directly**, bypassing class invariants.

If the register pointer is public, anyone can write a wrong mask and break the peripheral state. Private plus access methods centralize and validate every access.

Rule: hide hardware pointers in private, expose only safe methods (`set`/`clear`/`read`).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
