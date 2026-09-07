---
id: emb-tmplcx-0030
title: "Trap: why is collapsing all types to `uint32_t` to reduce bloat a trade-off?"
description: "Fewer instantiations reduce Flash usage, but uint32t wastes RAM on small values."
track: embedded
section: templates-and-constexpr
level: junior
type: pitfall
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

<span class="warn">Fewer instantiations (less Flash), but `uint32_t` wastes RAM on small values.</span>

If a buffer could have been `uint8_t` and you made it `uint32_t` for a single instantiation, you save ROM but quadruple the RAM buffer.

Mitigation: balance the number of instantiations (Flash) against the type width (RAM) for the specific MCU.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
