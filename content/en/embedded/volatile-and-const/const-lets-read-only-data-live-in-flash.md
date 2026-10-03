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
updated: 2026-10-04
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: gnu-ld-linker-scripts
    title: "GNU ld manual: Linker Scripts"
    url: https://sourceware.org/binutils/docs/ld.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Explains that linker scripts map sections into memory and can place read-only data in ROM; does not guarantee this behavior for other linkers or configurations."
---

## Short answer

**`const` makes data unmodifiable through that lvalue; the toolchain and linker script decide whether it lives in Flash**.

In a common embedded setup, the linker script may place read-only data in Flash/ROM and copy mutable initialized data from Flash to RAM at startup. This depends on the system; C does not guarantee it.[^gnu-ld-linker-scripts]

Declaring immutable tables, strings and descriptors `const` gives read-only access and may save RAM. Check the map file: the declaration alone promises neither `.rodata` nor Flash placement.[^iso-c-n1570] [^gnu-ld-linker-scripts]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
