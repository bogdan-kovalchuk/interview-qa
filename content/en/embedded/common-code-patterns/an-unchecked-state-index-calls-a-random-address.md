---
id: emb-patterns-0040
title: "Trap: what happens if a state machine does not check the state index before `handlers[state]`?"
description: "An invalid or corrupted state causes an out-of-bounds read and an indirect call at a random address, likely a HardFault."
track: embedded
section: common-code-patterns
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-06
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-06; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Confirms that an array index out of bounds (6.5.6 para. 8, Annex J.2) and a call through a pointer to a function of an incompatible type (6.5.2.2 para. 9) are undefined behavior; says nothing about the behavior of a particular processor."
  - source_id: tm4c123-datasheet
    title: "Tiva TM4C123GH6PM Microcontroller Data Sheet (SPMS376E)"
    url: https://www.ti.com/lit/ds/symlink/tm4c123gh6pm.pdf
    accessed: 2026-10-06
    kind: official
    version: "SPMS376E"
    applicability: "For the Cortex-M4F core: a bus error on instruction fetch, a jump into an XN region and an attempt to execute with the Thumb bit clear raise a fault, and a fault without an enabled handler escalates to HardFault. Section 2.6 Fault Handling. Other cores and chips differ in detail; an address that points at real code raises no fault."
---

## Short answer

<span class="warn">Invalid/corrupted state -> out-of-bounds table read and an indirect call at a random address</span> (undefined behavior: on Cortex-M a fault, including HardFault, is likely but not guaranteed).[^iso-c-n1570]

Data becomes control flow, so a state from external input or corruption directly controls which function is called, and if the value read happens to point at real code, no fault occurs at all.[^tm4c123-datasheet]

Defense (for an unsigned `state`): `if (state < ARRAY_SIZE(handlers) && handlers[state]) handlers[state](evt); else on_error();`

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
