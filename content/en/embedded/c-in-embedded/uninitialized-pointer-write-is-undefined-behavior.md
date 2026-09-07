---
id: emb-cppfound-0003
title: "Trap: what happens?"
description: "An uninitialized pointer is a wild pointer holding a garbage address, so writing through it is undefined behavior that can corrupt memory or trigger a HardFault on Cortex-M; always initialize pointers."
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
int *p;
*p = 5;
```

## Short answer

`p` is a <span class="warn">wild pointer</span>: an uninitialized pointer holds a garbage address (a random value from the stack).

Writing `*p = 5` -> undefined behavior: it may overwrite a random memory region, another variable, or cause a <span class="warn">HardFault</span> on Cortex-M (if the address is outside RAM).

Protection: always initialize pointers: `int *p = NULL;` or immediately `int *p = &x;`[^embeddedinterviewlab]

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
