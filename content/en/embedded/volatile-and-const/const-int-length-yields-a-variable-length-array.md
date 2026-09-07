---
id: emb-volconst-0043
title: "What happens to this code in C?"
description: "At block scope in C99+, this can be a VLA rather than a compile-time fixed array."
track: embedded
section: volatile-and-const
level: junior
type: mechanism
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

## Question code

```c
const int n = 8;
int a[n];
```

## Short answer

At block scope in C99+, this can be a VLA (variable length array), not necessarily a compile-time fixed array.

`const int n` does not make `n` an integer constant expression in C the way many expect after C++. On embedded targets, this matters because a VLA allocates stack memory at runtime and is often banned by coding standards.

Protection: for compile-time sizes in C, use `#define N 8`, `enum { N = 8 }`, or static assertions depending on the standard.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
