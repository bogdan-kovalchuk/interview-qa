---
id: emb-cppfound-0021
title: "What is a double pointer (`int **pp`) and why is it needed?"
description: "A pointer to a pointer, used to modify the caller's pointer, build 2D arrays, or advance a parse cursor."
track: embedded
section: c-in-embedded
level: junior
type: concept
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

## Short answer

**Double pointer** – a pointer that stores the address of another pointer.

Why:
1. **Modify the caller's pointer**: `void alloc(int **pp){ *pp = malloc(n); }` – without `**` the caller would not see the new address;
2. **2D arrays via arrays of pointers**;
3. Advancing a parse cursor: `void parse(char **p){ (*p)++; }`;

Reading the type: `int **pp` – "pointer to pointer to int"; `*pp` -> a pointer, `**pp` -> an int value.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
