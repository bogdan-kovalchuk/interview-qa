---
id: emb-dtypes-0087
title: "What is `size_t`, and why is it better than `int` for sizes and indices?"
description: "sizet is unsigned and always wide enough for any object on the platform, unlike int."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

**`size_t`** is an implementation-defined unsigned integer type large enough to represent the size of any object supported by the implementation; it is not necessarily `uint32_t` or `uint64_t`. `sizeof` produces `size_t`, as do `strlen` and `malloc` in their standard library declarations. Use a matching type for lengths and indices, while remembering that unsigned values cannot be negative and comparisons with `int` can trigger conversions.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
