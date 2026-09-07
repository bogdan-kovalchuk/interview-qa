---
id: emb-cppfound-0088
title: "What is printed?"
description: "Why relational comparison of pointers to different objects is undefined in C."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
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
int a=1,b=2;
int *p=&a,*q=&b;
printf("%d", p<q);
```

## Short answer

<span class="warn">Undefined behavior per the C standard</span>. Relational comparison (`<`, `>`) of pointers from different objects is not defined by the standard.

In practice (most platforms, flat memory): the result depends on variable placement in memory (stack order is compiler-dependent). Not portable;

Allowed: `p == q`, `p != q` – equality comparison between any pointers. Relational comparisons – only within a single array.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
