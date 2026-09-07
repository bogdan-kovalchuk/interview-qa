---
id: emb-dtypes-0093
title: "Where is `extern const uint8_t image_data[]` stored when defined in a linker script?"
description: "The array lives in Flash, and the linker script assigns its address via a dedicated section symbol."
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

In Flash, in the `.rodata` section or a special section defined in the linker script.

`extern const` without an initializer in C code is only a declaration. The linker script defines the symbol `image_data` with an address in Flash:
`image_data = LOADADDR(.flash_resources);`

Typical use: binary resources (images, certificates, tables) embedded into firmware via `KEEP(*(.flash_data))` or `objcopy -I binary`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
