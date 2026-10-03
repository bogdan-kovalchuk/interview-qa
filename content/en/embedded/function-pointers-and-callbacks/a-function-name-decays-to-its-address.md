---
id: emb-fnptr-0007
title: "What does this code print?"
description: "The code prints 42 because the function name implicitly decays to a function pointer."
track: embedded
section: function-pointers-and-callbacks
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
int add1(int x) { return x + 1; }
int (*op)(int) = add1;
printf("%d", op(41));
```

## Short answer

Prints `42` if the snippet is surrounded by the required declarations and `printf` is available.

In this assignment, the function name `add1` is converted to a pointer to function, so `op = add1` is equivalent to `op = &add1`. The call `op(41)` calls the function through the pointer; in C, both `op(41)` and `(*op)(41)` are permitted forms.[^iso-c-n1570]


## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
