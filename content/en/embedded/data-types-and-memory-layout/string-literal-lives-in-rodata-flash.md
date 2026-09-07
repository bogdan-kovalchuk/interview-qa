---
id: emb-dtypes-0035
title: "Where does the string literal `\"Hello, World!\"` live in an embedded program's memory?"
description: "The compiler places string literals in .rodata in Flash, so they cost no RAM."
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

In the **.rodata** section in Flash. The compiler places string literals in a read-only section – they take no RAM.

The same string is used only once (deduplication is compiler-dependent).

<span class="warn">Exception</span>: `char arr[] = "hello";` – the compiler initializes the array with the string's values, and the array (local/static) is placed on the stack / in `.data` respectively.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
