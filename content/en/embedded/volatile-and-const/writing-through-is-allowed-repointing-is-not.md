---
id: emb-volconst-0022
title: "What compiles here: `int * const p`?"
description: "p = 3 compiles but p = &y does not; const is to the right of so the pointer is protected, not the data."
track: embedded
section: volatile-and-const
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

## Question code

```c
int x = 1, y = 2;
int * const p = &x;
*p = 3;
p = &y;
```

## Short answer

**`*p = 3` compiles, `p = &y` does not compile.**

`int * const p` means const pointer to int. The address stored in `p` is immutable, but the object `x` itself is mutable.

Rule: if `const` is to the right of `*`, the pointer is protected; if to the left of `*`, the data is protected.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
