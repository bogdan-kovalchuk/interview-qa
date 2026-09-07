---
id: emb-tmplcx-0033
title: "Why is a constexpr table in Flash better than computing the table at startup?"
description: "A constexpr table wastes neither boot time nor RAM because the ready constant lives in .rodata."
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

**It wastes neither boot time nor RAM – the ready constant lives in `.rodata`.**

A startup loop that computes a CRC (cyclic redundancy check) or other lookup table adds delay before `main()` and often keeps the table in RAM. `constexpr` moves this to build time, leaving RAM free.

Rule: compute immutable derived data at compile time, not in startup code.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
