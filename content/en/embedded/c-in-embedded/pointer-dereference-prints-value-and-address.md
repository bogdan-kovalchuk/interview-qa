---
id: emb-cppfound-0002
title: "What does this print?"
description: "Dereferencing a pointer reads the pointed-to value, while the pointer itself holds the address."
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
int x = 42;
int *p = &x;
printf("%d %p", *p, (void*)p);
```

## Short answer

`*p` -> `42` (dereferencing – reads the value of `x`). `p` -> address of variable `x` (for example, `0x2000FFE0` on the Cortex-M stack).

Key point: `p` and `x` are different objects. `p` holds the address, `x` holds the value. Changing `*p = 100` changes `x`, while changing `p = &y` does not change `x`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
