---
id: emb-dtypes-0037
title: "What is the difference between `uint32_t` and `unsigned int` for portability?"
description: "unsigned int is platform-dependent, while uint32t is always exactly 32 bits on every platform."
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

`unsigned int` – platform-dependent: 2 bytes on 16-bit MCU, 4 bytes on 32-bit.

`uint32_t` – **always exactly 32 bits** on any platform (defined in `<stdint.h>`).

In embedded: register maps, protocols, struct layout -> always `uint32_t`. For sizes and indices -> `size_t`. `unsigned int` is appropriate only when the exact size is not critical.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
