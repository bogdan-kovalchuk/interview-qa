---
id: emb-cppfound-0052
title: "What is the difference between `char arr[] = \"hello\"` and `char *p = \"hello\"`?"
description: "How writable character arrays differ from pointers to string literals."
track: embedded
section: c-in-embedded
level: junior
type: concept
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

## Short answer

`char arr[] = "hello"` is an **array**: the compiler allocates 6 bytes and copies the characters; the data resides in writable memory (stack or .data). `arr[0] = 'H'` is legal.

`char *p = "hello"` is a **pointer** to a string literal in .rodata (Flash/read-only). `p[0] = 'H'` -> <span class="warn">UB/HardFault</span>.

`sizeof(arr) = 6`, `sizeof(p) = 4` (or 8) – the array is on the stack, the pointer only holds the address.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
