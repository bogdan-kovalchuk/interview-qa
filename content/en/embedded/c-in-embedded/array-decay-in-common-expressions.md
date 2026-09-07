---
id: emb-cppfound-0009
title: "What is array decay and in which contexts does it occur?"
description: "Array decay is the automatic conversion of an array to a pointer to its first element in most expressions, causing the function to lose the array size information."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Origin of the question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Array decay** is the automatic conversion of an array to a pointer to its first element.

It occurs in most expressions:
- when passed to a function: `f(arr)` -> the function receives `int*`;
- in arithmetic: `arr+1` -> `int*`;
- on assignment: `int *p = arr`.

Consequence: the function <span class="warn">loses information about the size</span> of the array. The type becomes `int*`, not `int[N]`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
