---
id: emb-dtypes-0055
title: "`.bss` vs `.data` for: `uint32_t cnt;` and `uint32_t cnt = 0;` (globals)?"
description: "uint32t cnt; lands explicitly in .bss; uint32t cnt = 0; depends on whether the compiler recognizes the zero-init."
track: embedded
section: data-types-and-memory-layout
level: middle
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

`uint32_t cnt;` -> **.bss**: takes no Flash, zeroed by startup code.

`uint32_t cnt = 0;` -> depends on the compiler: may be `.data` (explicit initializer, value 0 in Flash) or `.bss` (compiler recognizes zero-init).

The C standard guarantees both = 0, but Flash/RAM usage may differ. Check: `arm-none-eabi-nm --print-size firmware.elf`. Write `uint32_t cnt;` for explicit `.bss`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
