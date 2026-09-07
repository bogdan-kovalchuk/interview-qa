---
id: emb-memlink-0008
title: "What happens if `free` is called twice?"
description: "Calling free twice on the same block is double free and undefined behavior that can crash the program, corrupt the heap, or open a security vulnerability."
track: embedded
section: memory-and-linker
level: junior
type: pitfall
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

A repeated `free(ptr)` on the same allocated block is <span class="warn">double free</span> and undefined behavior.[^dou-embedded-interview] Consequences can vary: crash, heap metadata corruption, random errors later, or a security vulnerability.

Safe pattern: null out the pointer after freeing – `free(ptr); ptr = NULL;`. Calling `free(NULL)` is allowed and does nothing, so nulling reduces the risk of a repeated free. But if there are multiple copies of the same pointer, ownership must be tracked rather than relying on `NULL` alone.

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
