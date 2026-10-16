---
id: emb-fnptr-0058
title: "What should a good interview answer about embedded callbacks contain?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Mechanism, contract and risks.**

Mechanism: a function pointer with a concrete signature. Contract: who registers, who calls, when, with which context pointer and lifetime. Risks: null pointer, incompatible call signature (undefined behavior in C), ISR context, dangling context, reentrancy, blocking calls and dispatch index validation.[^iso-c-n1570]

Rule: a strong embedded answer does not stop at the syntax of `void (*cb)(void)`; it explains runtime ownership and execution context.[^embeddedinterviewlab]

## Detailed explanation

TODO
