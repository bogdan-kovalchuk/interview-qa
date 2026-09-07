---
id: emb-cppfound-0026
title: "What is the difference between `const int *p` and `int * const p`?"
description: "const int p makes the pointed-to data constant; int const p makes the pointer itself constant; read right to left."
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

`const int *p` (or `int const *p`) – **a pointer to a constant int**:
- `*p = 5` – forbidden (the data is protected);
- `p = &y` – allowed (the address can be changed).

`int * const p` – **a constant pointer to int**:
- `*p = 5` – allowed;
- `p = &y` – forbidden (the address is fixed).

`const int * const p` – both the data and the address are immutable. Rule: read right to left.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
