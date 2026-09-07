---
id: emb-cppfound-0096
title: "Trap: what is wrong?"
description: "Why dereferencing an uninitialized double pointer is undefined behavior."
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
int **pp;
*pp = malloc(10*sizeof(int));
```

## Short answer

<span class="warn">Wild pointer – UB.</span> `int **pp;` – an uninitialized double pointer, contains a garbage address.

`*pp = malloc(...)` – dereferences `pp` (UB!) and writes the allocated memory address to an unknown location. This can corrupt any memory region.

Correct:

```c
int *p = NULL;
int **pp = &p;
*pp = malloc(10*sizeof(int));
```

Always initialize pointers before use.[^embeddedinterviewlab]

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
