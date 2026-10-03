---
id: emb-volconst-0021
title: "What compiles here: `const int *p`?"
description: "p = &y compiles but p = 3 does not; const is to the left of so the pointed-to data is protected, not the pointer."
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
const int *p = &x;
p = &y;
*p = 3;
```

## Short answer

**`p = &y` compiles, `*p = 3` does not compile.**

`const int *p` means pointer to const int. Const applies to the data pointed to by `p`, not to the pointer itself. So the pointer can be changed, but writing through it is forbidden.

Rule: if `const` is to the left of `*`, the pointed-to data is protected.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
