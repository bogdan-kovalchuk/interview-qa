---
id: emb-dtypes-0070
title: "What does `sizeof(struct { char a; char b; int c; })` return on a typical 32-bit ABI with 4-byte int alignment?"
description: "Under the stated ABI, two padding bytes align int and the struct size is eight bytes."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
anki:
  export: true
sources:
  - source_id: gnu-c-struct-layout
    title: "GNU C Introduction and Reference Manual: Structure Layout"
    url: https://www.gnu.org/software/c-intro-and-ref/manual/html_node/Structure-Layout.html
    accessed: 2026-10-04
    kind: book
    version: "current"
    applicability: "Illustrates common struct alignment and padding; exact layout depends on the implementation and ABI."
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
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

Under the stated ABI, the result is **8 bytes**: `a` and `b` have offsets 0 and 1, two padding bytes align `c` at offset 4, and there is no trailing padding.[^gnu-c-struct-layout] Reordering to `char`, `int`, `char` gives 12 bytes on the same typical ABI because padding appears before and after `int`.[^gnu-c-struct-layout]

C does not guarantee this layout on every system: size and alignment depend on ABI, packing options, and attributes. Ordering fields by decreasing alignment often reduces padding, but verify offsets and `sizeof` with the target compiler.[^iso-c-n1570][^gnu-c-struct-layout]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
