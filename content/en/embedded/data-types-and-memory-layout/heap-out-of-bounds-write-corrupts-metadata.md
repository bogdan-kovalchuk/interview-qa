---
id: emb-dtypes-0075
title: "What happens? `int *p = (int*)malloc(10*sizeof(int)); p[10] = 0;`"
description: "`malloc(10*sizeof(int))` allocates only `p[0]..p[9]`, so `p[10]` writes past the allocated heap block."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 1
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
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

TODO

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
