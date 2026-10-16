---
id: emb-memlink-0007
title: "What types of memory segments do you know?"
track: embedded
section: memory-and-linker
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
---

## Short answer

Typical memory layout of a C program:[^dou-embedded-interview]

- **.text** – machine code. Read-only, and on MCUs usually in Flash.
- **.rodata** – read-only data: string literals and some constants.
- **.data** – globals and statics with non-zero initialization, copied from Flash to RAM at startup.
- **.bss** – globals and statics with no initialization or `= 0`, zeroed by startup code;
- **Stack** – locals, arguments, return addresses;
- **Heap** – dynamic memory (`malloc`). On most architectures the stack grows down and the heap up, but that is platform/ABI dependent, not a rule of the C standard.

## Detailed explanation

TODO
