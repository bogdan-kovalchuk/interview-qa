---
id: emb-memlink-0006
title: "What problems can arise if a function returns a pointer to a local variable?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
---

## Short answer

A local variable lives on the **stack** and is destroyed when the function returns (SP changes).[^dou-embedded-interview] The returned pointer becomes a <span class="warn">dangling pointer</span> into memory that is no longer valid, and reading or writing through it is <span class="warn">undefined behavior</span>: garbage, overwritten variables or a crash.

```c
int* f(void) { int x = 42; return &x; }
```

The next call may overwrite that memory, and GCC warns: `warning: function returns address of local variable [-Wreturn-local-addr]`.[^embeddedinterviewlab]

Alternatives: return a value; allocate via `malloc`; use a `static` variable (not thread-safe); or pass a buffer through a parameter.

## Detailed explanation

TODO
