---
id: emb-volconst-0023
title: "What compiles here: `const int * const p`?"
description: "Neither p = 3 nor p = &y compiles; both the pointer and the pointed-to data are const-qualified."
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
const int * const p = &x;
*p = 3;
p = &y;
```

## Short answer

**Neither assignment compiles: `*p = 3` and `p = &y`.**

`const int * const p` means const pointer to const int. Through this pointer, neither the pointed-to value nor the pointer value itself can be changed.

Embedded example: a fixed pointer to a read-only lookup table, or to a read-only register if you add `volatile` for hardware.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
