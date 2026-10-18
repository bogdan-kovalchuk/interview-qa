---
id: emb-cemb-0011
title: "How does a function call work?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

A call follows the **calling convention** of the ABI.[^dou-embedded-interview] Arguments go in registers or on the stack, the return address is saved, control transfers to the function, and it builds its own **stack frame** for locals and saved registers.

The result returns usually in a register, or through a hidden pointer for large structs; saved registers and the stack pointer are then restored and control returns to the call address. Details differ across x86-64, ARM Cortex-M and AAPCS, but the idea is one contract between caller and callee.

## Detailed explanation

TODO
