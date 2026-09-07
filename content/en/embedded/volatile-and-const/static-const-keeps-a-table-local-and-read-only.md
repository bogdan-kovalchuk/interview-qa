---
id: emb-volconst-0056
title: "What does `static const` mean for a table inside a C file?"
description: "static limits linkage to this translation unit and const makes the data read-only through this identifier."
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

**`static` limits linkage to this translation unit, and `const` makes the data read-only through this identifier.**

For an embedded lookup table this is often the ideal form: the symbol is not exported, the data can reside in `.rodata`/Flash, and the compiler can optimize accesses within the file.

Rule: declare file-private immutable tables as `static const` unless they must be part of the external ABI.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
