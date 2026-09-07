---
id: emb-memlink-0002
title: "What problems can arise from not freeing memory?"
description: "Unfreed memory causes a memory leak that exhausts the heap, eventually making malloc return NULL and crashing or resetting the device."
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

**Memory leak** – allocated memory is not returned to the system even though it is no longer used.[^dou-embedded-interview] Consequences:

- the heap is gradually exhausted, so `malloc` returns `NULL`;
- the system slows down or hangs;
- in embedded (MCU without MMU or OS) this is especially critical: a small heap can run out after hours or days, and the device goes into reset/fault or an incorrect state.

Related problems: <span class="warn">dangling pointer</span> (accessing freed memory), <span class="warn">double free</span> (UB).

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
