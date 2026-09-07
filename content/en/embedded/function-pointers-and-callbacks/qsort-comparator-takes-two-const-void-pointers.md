---
id: emb-fnptr-0032
title: "What does a callback for `qsort` look like in C?"
description: "The comparator signature is int cmp(const void a, const void b) returning order."
track: embedded
section: function-pointers-and-callbacks
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

The comparator signature is: `int cmp(const void *a, const void *b)`.

It returns a negative, zero or positive value to say whether the first element is less than, equal to or greater than the second. Inside the callback you must cast `a` and `b` to pointers to the actual element type.

Rule: `qsort` does not know the element type; the function pointer callback gives it type-specific comparison logic.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
