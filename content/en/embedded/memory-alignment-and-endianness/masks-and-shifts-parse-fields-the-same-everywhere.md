---
id: emb-align-0036
title: "Why are masks and shifts on a `uint32_t` more portable than unions or bitfields for parsing fields?"
description: "Arithmetic shifts and masks produce the same result regardless of endianness and compiler."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 4
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

**Shifts and masks on the same unsigned value extract the same logical bits.**

For `uint32_t reg`, `(reg >> 4) & 0x7` extracts bits 4–6 of the numeric value itself; the result does not depend on how its bytes are laid out in memory.

First decode bytes according to the format, then use shifts and masks; C leaves bitfield allocation and packing to the implementation.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
