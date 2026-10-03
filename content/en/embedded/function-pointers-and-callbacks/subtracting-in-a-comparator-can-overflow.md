---
id: emb-fnptr-0033
title: "Trap: what is wrong with this `qsort` comparator?"
description: "Subtraction can overflow int, which is undefined behaviour for signed overflow."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: pitfall
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
int cmp(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}
```

## Short answer

<span class="warn">Subtracting two `int` values can overflow the result; signed overflow is undefined behaviour in C.</span>

If one element is `INT_MIN` and the other is `INT_MAX`, the mathematical difference is not representable in `int`; the C standard defines signed overflow as undefined behaviour. The comparator must return ordering, not necessarily an arithmetic difference.[^iso-c-n1570]

Protection: use `return (x > y) - (x < y);` after reading `x` and `y`.[^iso-c-n1570]

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
