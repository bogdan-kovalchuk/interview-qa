---
id: emb-cppfound-0066
title: "What does this code print?"
description: "Why pointer arithmetic on a pointer to a standalone object is undefined."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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
    applicability: "Source question and answer; answer not independently verified."
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
int a=1;
int *p=&a;
int *q=&a;
q++;
printf("%d",*q);
```

## Short answer

<span class="warn">Undefined behavior</span>. `q++` -> `q` now points to the address immediately after `a` on the stack – this is not an array element, only a standalone variable. Pointer arithmetic is defined only within an array (or struct under certain conditions). For two separate variables – even if adjacent on the stack – `&a + 1` -> UB; the compiler may place `a` in a register with no memory address -> `*q` reads garbage.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
