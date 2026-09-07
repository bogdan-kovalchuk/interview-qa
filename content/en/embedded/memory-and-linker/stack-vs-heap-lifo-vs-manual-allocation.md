---
id: emb-memlink-0005
title: "What is the difference between stack and heap?"
description: "Stack is automatic LIFO memory for locals managed by the compiler, while heap is manual dynamic memory allocated via malloc with fragmentation risk."
track: embedded
section: memory-and-linker
level: junior
type: comparison
tags: []
status: published
updated: 2026-09-07
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of this question and answer; the answer text is not independently verified against the original community Anki deck."
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
    accessed: 2026-09-06
    kind: official
    version: "2.47"
    applicability: "Authoritative section-level reference for memory and linker concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Stack** is automatic memory: local variables and function return addresses, managed by the compiler/CPU in LIFO order.[^dou-embedded-interview] Fast access, limited size, freed automatically on function exit.

**Heap** is dynamic memory: allocated manually via `malloc`/`free`. Larger capacity, but slower access and a risk of fragmentation; requires explicit deallocation.

In embedded, the heap is avoided because of nondeterminism: stack and heap bounds are set in the linker script.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
