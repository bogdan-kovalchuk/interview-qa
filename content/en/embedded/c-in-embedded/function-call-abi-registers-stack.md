---
id: emb-cemb-0042
title: "How does a function call work at the ABI level: stack frame, registers, return address, and calling convention?"
track: embedded
section: c-in-embedded
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

The ABI defines which arguments and return value go in registers, what is placed on the stack, and which registers the caller/callee must preserve. During a call the return address is saved, a stack frame is created for locals/spills, then the callee returns the result and restores the required state. For debugging HardFault it is useful to examine SP, LR, PC, and the stack frame.[^dou-embedded-interview]

## Detailed explanation

TODO
