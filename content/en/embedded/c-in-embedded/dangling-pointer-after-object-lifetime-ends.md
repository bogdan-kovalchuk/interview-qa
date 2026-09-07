---
id: emb-cppfound-0017
title: "What is a dangling pointer and when does it occur?"
description: "A pointer that refers to already freed or destroyed memory, arising from returning locals, use-after-free, or expired object lifetimes."
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

**Dangling pointer** – a pointer that refers to <span class="warn">already freed or destroyed</span> memory.

Causes: 1; Returning the address of a local variable: `int* f(){ int x=5; return &x; }` – x is destroyed on return; 2; After `free(ptr)` without nulling: `free(ptr); *ptr = 1;` – undefined behavior;
3. A pointer to an object whose lifetime has ended.

The danger: the memory <span class="warn">appears valid</span> until it is reused. The bugs are extremely hard to reproduce.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
