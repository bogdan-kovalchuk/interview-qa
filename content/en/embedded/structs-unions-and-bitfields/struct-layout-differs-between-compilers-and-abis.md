---
id: emb-structs-0053
title: "Trap: can you rely on C struct layout across different compilers without checking?"
description: "ABI, alignment, packing pragmas, and bit-field rules can differ across compilers."
track: embedded
section: structs-unions-and-bitfields
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

<span class="warn">No: ABI, alignment, packing pragmas, and bit-field rules can differ.</span>

Even identical source can have different offsets or size on another architecture. For a host tool plus MCU firmware this is a frequent bug: the PC tool writes a binary file per its struct layout, the firmware reads it per a different one.

Mitigation: describe external binary formats in bytes, not in C structs. Add version, length, endian, and static/runtime checks.[^embeddedinterviewlab]

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
