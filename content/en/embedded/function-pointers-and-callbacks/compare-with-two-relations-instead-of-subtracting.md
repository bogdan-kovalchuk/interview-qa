---
id: emb-fnptr-0034
title: "What is a safer way to write a `qsort` comparator for `int`?"
description: "Compare both directions and subtract the Boolean results to avoid signed overflow."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

Like this:

`return (x > y) - (x < y);`

Full fragment: `const int x = *(const int *)a; const int y = *(const int *)b;`. Such a comparator returns `1`, `0` or `-1` without signed overflow.

Rule: a comparator must determine ordering consistently for the same values; qsort uses the result sign to distinguish less, equal, and greater.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
