---
id: emb-cppfound-0046
title: "Trap: what is wrong?"
description: "Why dereferencing a pointer after free is undefined behavior."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
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
free(ptr);
if(*ptr == 0)
```

## Short answer

<span class="warn">Use-after-free is undefined behavior.</span> After `free(ptr)`, the memory block is returned to the heap manager and may be immediately reused.

Reading `*ptr` -> undefined behavior: it may return 0, the old value, or a new value from another malloc. In real code, it is a source of security vulnerabilities (type confusion, heap exploitation).

Rule: after `free`, always: `ptr = NULL;`; then `if(ptr != NULL && *ptr == 0)` is safe.[^embeddedinterviewlab]

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
