---
id: emb-volconst-0024
title: "Why does `const` matter in embedded beyond write protection?"
description: "const allows placing file-scope or static read-only data into Flash, typically into .rodata, saving RAM."
track: embedded
section: volatile-and-const
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

**`const` allows placing file-scope/static read-only data into Flash, typically into `.rodata`**.

Without `const`, an initialized global array goes into `.data`: the initial bytes are stored in Flash, but at startup they are copied into RAM. On an MCU with 16 KB of RAM, a 1 KB lookup table can be a noticeable loss.

Rule: calibration tables, strings, protocol descriptors, CRC tables and LUTs that do not change should be declared `const`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
