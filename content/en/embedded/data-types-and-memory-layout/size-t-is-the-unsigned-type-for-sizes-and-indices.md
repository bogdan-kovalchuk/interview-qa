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
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

**size_t** – an unsigned type large enough to represent the size of any object in memory (on 32-bit = `uint32_t`, on 64-bit = `uint64_t`); defined in `<stddef.h>`.

Advantages:

- cannot be negative (logical for a size);
- correct size for the platform;
- avoids sign-comparison warnings.

`sizeof`, `strlen`, `malloc` use and return `size_t`, whereas `int` can be 16-bit (insufficient for large objects).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
