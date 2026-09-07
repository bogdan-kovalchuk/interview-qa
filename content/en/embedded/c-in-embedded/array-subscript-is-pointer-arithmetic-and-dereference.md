---
id: emb-cppfound-0031
title: "How are `arr[i]` and `*(arr+i)` related in standard C?"
description: "The C standard defines arr[i] as (arr+i), making indexing pointer arithmetic plus dereference and even allowing 2[arr]."
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

Per the C standard (§6.5.2.1): **`arr[i]` is defined as `*(arr+i)`**. This is not syntactic sugar – it is the exact definition of the subscript operator.

Consequences:
- `arr[2] == *(arr+2) == *(2+arr) == 2[arr]` – all equivalent;
- Indexing is simply pointer arithmetic + dereference;
- Negative indices (`arr[-1]`) are formally allowed if the pointer is already offset and the result points within the array.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
