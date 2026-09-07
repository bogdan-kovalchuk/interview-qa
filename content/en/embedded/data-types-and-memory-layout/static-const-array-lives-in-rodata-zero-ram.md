---
id: emb-dtypes-0068
title: "Where is this stored inside a function? `static const uint16_t lookup[] = {1, 2, 3};`"
description: "static const places the array in .rodata in Flash, so it costs zero bytes of RAM."
track: embedded
section: data-types-and-memory-layout
level: junior
type: mechanism
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

In the **.rodata** section (Flash). The `static const` combination: `static` -> not on the stack (static storage duration); `const` -> read-only.

Result: data in Flash, **zero RAM cost**.

If it were `static uint16_t lookup[] = {1,2,3};` (without `const`) -> `.data` (RAM + Flash copy at boot).

Rule: for lookup tables, calibration data, string tables - always `static const`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
