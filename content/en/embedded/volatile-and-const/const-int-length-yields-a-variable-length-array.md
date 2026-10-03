---
id: emb-volconst-0043
title: "What happens to this code in C?"
description: "At block scope in C, this can be a VLA if the implementation supports VLAs; it is not necessarily a compile-time fixed array."
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
const int n = 8;
int a[n];
```

## Short answer

At block scope in C, this can be a VLA (variable length array) if the implementation supports VLAs; it is not necessarily a compile-time fixed array.[^iso-c-n1570]

`const int n` does not make `n` an integer constant expression in C the way many expect after C++. A VLA has a runtime-determined size; the standard does not require stack allocation, and embedded compilers may omit or prohibit VLAs.

Protection: for a compile-time size in C, use `#define N 8` or `enum { N = 8 }`.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
