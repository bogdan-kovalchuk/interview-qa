---
id: emb-dtypes-0075
title: "What happens? `int *p = (int*)malloc(10*sizeof(int)); p[10] = 0;`"
description: "malloc(10sizeof(int)) allocates only p[0]..p[9], so p[10] writes past the allocated heap block."
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

<span class="warn">A write outside the array has undefined behavior.</span> `p[10]` is not an element of an array of ten `int` values.[^iso-c-n1570]

`malloc(10 * sizeof(int))` requests space for ten elements, indexed 0 through 9. The C standard does not define what physically follows that object: the write may corrupt other data or fault, but heap metadata corruption is not guaranteed.[^iso-c-n1570]

During development, use available tools such as AddressSanitizer or guard regions to detect the error; their availability depends on the platform and runtime.[^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
