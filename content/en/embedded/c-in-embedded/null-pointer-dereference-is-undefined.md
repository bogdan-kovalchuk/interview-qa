---
id: emb-cppfound-0019
title: "What is a NULL pointer and what happens when it is dereferenced?"
track: embedded
section: c-in-embedded
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**NULL pointer** – a guaranteed invalid address (null pointer constant): `0` or `(void*)0` in C, `nullptr` in C++.

Dereferencing NULL -> <span class="warn">undefined behavior</span>. On Cortex-M: address `0x00000000` is the start of Flash (Vector Table). Writing there -> HardFault or Vector Table corruption.

Protection: always check before dereferencing: `if(p != NULL) *p = val;`; initialize: `int *p = NULL;`[^embeddedinterviewlab]

## Detailed explanation

TODO
