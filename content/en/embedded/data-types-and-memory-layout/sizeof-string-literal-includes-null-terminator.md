---
id: emb-dtypes-0015
title: "What do `sizeof(\"hello\")` and `strlen(\"hello\")` print?"
description: "sizeof counts the null terminator and gives 6; strlen counts characters without it and gives 5."
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

`sizeof("hello")` -> **6**: the string literal is an array `{'h','e','l','l','o','\0'}` (6 bytes), and `sizeof` counts the null terminator at compile time. `strlen("hello")` -> **5**: a runtime function counts characters up to (not including) `'\0'`.

Common mistake: allocating `malloc(strlen(s))` without +1 for `'\0'` -> buffer overflow.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
