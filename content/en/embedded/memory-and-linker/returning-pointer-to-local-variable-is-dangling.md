---
id: emb-memlink-0006
title: "What problems can arise if a function returns a pointer to a local variable?"
description: "A local variable is destroyed on function return, so the returned pointer becomes dangling and accessing it is undefined behavior."
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-07
    kind: community
    version: null
    applicability: "Origin of the code snippet and the GCC warning in this answer; the DOU deck supports the remaining claims."
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
    accessed: 2026-09-06
    kind: official
    version: "2.47"
    applicability: "Authoritative section-level reference for memory and linker concepts; details of specific devices and toolchains can differ."
---

## Short answer

A local variable lives on the **stack** and is destroyed when the function returns (SP changes).[^dou-embedded-interview] The returned pointer becomes a <span class="warn">dangling pointer</span> – it points to memory that is no longer valid. Reading or writing through it is <span class="warn">undefined behavior</span>: it may return garbage, overwrite other variables, or cause a crash.

```c
int* f(void) { int x = 42; return &x; }
```

The memory may be overwritten by the next function call, and GCC warns: `warning: function returns address of local variable [-Wreturn-local-addr]`.[^embeddedinterviewlab]

Correct alternatives: return a value (not a pointer); allocate via `malloc` (heap); use a `static` variable (but not thread-safe); pass a buffer through a parameter.

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
