---
id: emb-dtypes-0008
title: "Which memory section: `uint32_t error_count;` (global) and `uint32_t sensor_count = 5;` (global)?"
description: "An uninitialized global goes to .bss; one initialized with a non-zero value goes to .data."
track: embedded
section: data-types-and-memory-layout
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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

`uint32_t error_count;` -> **.bss**: uninitialized global, zeroed at boot, takes no Flash.

`uint32_t sensor_count = 5;` -> **.data**: initialized global, the value `5` is stored in Flash and copied to RAM at load.

Both live for the entire program runtime.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
