---
id: emb-cppfound-0069
title: "Why is a cast used with `void*`, and what are the limitations?"
description: "C and C++ conversion rules and limitations of void pointers."
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

In **C**: assigning `void*` to `T*` (and vice versa) does not require an explicit cast – conversion is implicit. `int *p = malloc(n);` – valid in C. In **C++**: <span class="warn">an explicit cast is required</span>: `int *p = (int*)malloc(n);`. void* limitations:
- Cannot be dereferenced without a cast;
- No pointer arithmetic (C standard);
- Does not preserve type-safety;
Before dereferencing: `*(int*)vp = 42;`. This rule preserves the correct access type.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
