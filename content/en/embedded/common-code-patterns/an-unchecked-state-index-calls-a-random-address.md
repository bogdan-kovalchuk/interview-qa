---
id: emb-patterns-0040
title: "Trap: what happens if a state machine does not check the state index before `handlers[state]`?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: tm4c123-datasheet
    title: "Tiva TM4C123GH6PM Microcontroller Data Sheet (SPMS376E)"
    url: https://www.ti.com/lit/ds/symlink/tm4c123gh6pm.pdf
---

## Short answer

<span class="warn">Invalid/corrupted state -> out-of-bounds table read and an indirect call at a random address</span> (undefined behavior: on Cortex-M a fault, including HardFault, is likely but not guaranteed).[^iso-c-n1570]

Data becomes control flow, so a state from external input or corruption directly controls which function is called, and if the value read happens to point at real code, no fault occurs at all.[^tm4c123-datasheet]

Defense (for an unsigned `state`): `if (state < ARRAY_SIZE(handlers) && handlers[state]) handlers[state](evt); else on_error();`

## Detailed explanation

TODO
