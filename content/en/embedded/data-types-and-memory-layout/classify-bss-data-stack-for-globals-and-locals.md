---
id: emb-dtypes-0028
title: "Where do these live in `.bss`, `.data`, and the stack: `int g1; int g2 = 5; void f(){int l=3;}`?"
description: "The uninitialized global goes to .bss, the initialized one to .data, and the function-local variable to the stack."
track: embedded
section: data-types-and-memory-layout
level: junior
type: mechanism
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
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

`int g1;` -> **.bss** (zeroed at boot, value 0, takes no Flash).

`int g2 = 5;` -> **.data** (value 5 in Flash, copied to RAM at startup).

`int l = 3;` in a function -> **stack** (local, initialized by an instruction on function call, not zeroed automatically, but there is an explicit initializer here).

Function `f()` -> `.text` (Flash).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
