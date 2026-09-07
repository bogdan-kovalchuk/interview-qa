---
id: emb-cppfound-0004
title: "What is the address-of operator and what does it return?"
description: "The address-of operator returns the memory address of an object as a pointer to its type; it cannot be applied to non-lvalue expressions, register variables, or bit-field members."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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

## Short answer

The `&` operator (address-of) returns the **address of an object** in memory – a value of type "pointer to the object's type".

`int x = 5; int *p = &x;` – `p` now points to `x`.

You cannot take the address of:
- expressions without an lvalue (`&(a+b)` – error);
- `register` variables;
- bit-field members of a structure.

Types: `&int` -> `int*`, `&arr` -> `int(*)[N]` (pointer to array, not to element).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
