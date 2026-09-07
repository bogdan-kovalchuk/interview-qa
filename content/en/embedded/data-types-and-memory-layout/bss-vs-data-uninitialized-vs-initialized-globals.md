---
id: emb-dtypes-0004
title: "What is the `.bss` section and how does it differ from `.data`?"
description: ".bss holds zero-initialized globals with no Flash bytes; .data holds initialized ones copied from Flash."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
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

**.bss** (Block Started by Symbol) is a section for global and static variables without an initializer or with `= 0`.

Unlike `.data`, `.bss` **stores no bytes in Flash** – only the size. Startup code fills it with zeros before `main()`. This saves Flash: instead of storing zeros, the RAM region is simply zeroed.

`.data` requires initialization values in Flash plus copying to RAM.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
