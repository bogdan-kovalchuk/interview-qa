---
id: emb-cppfound-0081
title: "Trap: Is this valid in C99?"
description: "Whether a pointer to a C99 compound literal remains valid within its block."
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
int *p = &(int){5};
printf("%d", *p);
```

## Short answer

**Yes, valid** within the same block. `(int){5}` is a compound literal (C99): a temporary object with automatic block storage duration. <span class="warn">But dangling pointer</span> if the block scope is exited: `int *p; { p = &(int){5}; } *p; // UB – the block has ended`. GCC may not warn; safe usage: only within the same scope where the literal is defined.[^embeddedinterviewlab]

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
