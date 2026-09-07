---
id: emb-cppfound-0036
title: "How is a 2D array `int arr[3][4]` laid out in memory (row-major)?"
description: "How C stores two-dimensional arrays in row-major order."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
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

A 2D array in C is stored in **row-major order**: rows follow one another in contiguous memory.

`arr[0][0], arr[0][1], arr[0][2], arr[0][3],` `arr[1][0], arr[1][1], arr[1][2], arr[1][3],` `arr[2][0], arr[2][1], arr[2][2], arr[2][3]`

Total: 3×4×4 = 48 bytes. Address formula: `&arr[i][j] = arr + i*4 + j` (in elements). Optimal iteration: row by row (cache-friendly).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
