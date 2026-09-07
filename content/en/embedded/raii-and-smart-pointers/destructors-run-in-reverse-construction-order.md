---
id: emb-raii-0021
title: "Why are nested resources released in reverse order automatically?"
description: "Destructors of local objects are called in reverse order of construction."
track: embedded
section: raii-and-smart-pointers
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

**Destructors of local objects are called in reverse order of construction.**

If you acquired clock, then SPI, then CS, the release order will be CS -> SPI -> clock, which is usually the correct teardown order. By hand, this is easy to mix up.

Rule: declare RAII guards in dependency order; reverse destruction will take care of correct teardown.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
