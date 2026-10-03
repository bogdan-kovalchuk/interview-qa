---
id: emb-volconst-0019
title: "How do you read the declaration `const int *p`?"
description: "p is a pointer to const int; the pointer can be reassigned but writing through it is not allowed."
track: embedded
section: volatile-and-const
level: junior
type: concept
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

**`p` is a pointer to const `int`**.

`p` can be redirected to another `int`, but `*p = 5` is not allowed. Important: the object itself is not necessarily physically immutable; it is just read-only through this pointer.

Rule: read from the variable name right and left: `p` is pointer to const int.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
