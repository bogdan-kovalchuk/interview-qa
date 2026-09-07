---
id: emb-cppfound-0095
title: "What is printed?"
description: "Why a pointer to const cannot write while still observing direct changes to a non-const object."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 4
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

## Question code

```c
int x=5;
const int *p=&x;
x=10;
printf("%d",*p);
```

## Short answer

`10`.

`const int *p = &x` – a pointer to const int: it prevents modifying `*p` (through this pointer). But `x` is not const, so changing `x = 10` through the direct name is legal.

`*p` reads the value of `x` = 10. `const` protects against writing through `p`, but does not make `x` immutable – this is an important distinction: `const int *p` vs `const int x`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
