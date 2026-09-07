---
id: emb-cppfound-0033
title: "What is `ptrdiff_t` and why is it needed?"
description: "A signed integer type from stddef.h for pointer differences, sized to the platform width and printed with %td."
track: embedded
section: c-in-embedded
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

**ptrdiff_t** – a signed integer type for storing the result of subtracting two pointers. Defined in `<stddef.h>`.

Size: matches the platform width (32-bit -> 4B, 64-bit -> 8B).

Why: `p - q` gives the number of elements between the pointers. The result is signed (can be negative); storing it in `int` may be insufficient on 64-bit.

Format specifier: `%td` for `printf`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
