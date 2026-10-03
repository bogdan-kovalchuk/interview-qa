---
id: emb-structs-0038
title: "Trap: what is wrong with this definition?"
description: "The struct contains itself by value, so its size would be infinite."
track: embedded
section: structs-unions-and-bitfields
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
struct Node {
    int value;
    struct Node next;
};
```

## Short answer

<span class="warn">The struct contains itself by value, so its size would be infinite.</span>

The compiler cannot complete the layout: to know the size of `Node`, it needs the size of `next`, which is again `Node`. The allowed variant is a pointer: `struct Node *next;`.

Defence: for recursive data structures use a pointer or an index into a pool, not a nested object of the same type.[^iso-c-n1570]

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
