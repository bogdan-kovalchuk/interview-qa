---
id: emb-raii-0006
title: "What does an interrupt-disable RAII guard look like and why is it safe in an ISR?"
description: "The constructor saves the interrupt state in PRIMASK and disables interrupts; the destructor restores the previous state, allowing safe nesting even in ISR context."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
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
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: cmsis-core-register-access
    title: "CMSIS-Core (Cortex-M): Core Register Access"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__Core__Register__gr.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Describes `__get_PRIMASK()`, `__set_PRIMASK()` and `__disable_irq()`: the last disables interrupts and configurable fault handlers by setting PRIMASK with the `CPSID i` instruction, runs in privileged mode only, and a disabled interrupt can still become pending. Does not describe how these functions are implemented in a particular compiler, and does not cover cores other than Cortex-M."
  - source_id: tm4c123-datasheet
    title: "Tiva TM4C123GH6PM Microcontroller Data Sheet (SPMS376E)"
    url: https://www.ti.com/lit/ds/symlink/tm4c123gh6pm.pdf
    accessed: 2026-10-06
    kind: official
    version: "SPMS376E"
    applicability: "For the Cortex-M4F core: PRIMASK = 1 prevents activation of all exceptions with configurable priority, while Reset, NMI and hard fault have fixed priority; the register is accessible only in privileged mode, and in Handler mode execution is always privileged. Other cores and chips can differ in detail."
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements ([stmt.jump])"
    url: https://eel.is/c++draft/stmt.jump
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "A note says that on exit from a scope by any means, objects with automatic storage duration constructed there are destroyed in reverse order; the exception is program termination through `exit()` or `abort()`. Says nothing about interrupts."
  - source_id: gcc-extended-asm
    title: "GCC: Extended Asm"
    url: https://gcc.gnu.org/onlinedocs/gcc/Extended-Asm.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Says the `\"memory\"` clobber tells the compiler that the asm reads or writes memory beyond its operands and acts as a barrier for the compiler, but does not stop the processor from doing speculative reads. Does not describe the `cpsid` instruction."
---

## Short answer

**The ctor saves the current interrupt state and disables interrupts; the dtor restores the saved state instead of enabling interrupts unconditionally.** On Cortex-M this is a read of PRIMASK plus `cpsid i`, with no blocking and no heap,[^cmsis-core-register-access] and PRIMASK is accessible in privileged mode, so in an ISR (Handler mode) the guard works.[^tm4c123-datasheet] Restoring the saved value allows nested sections; while PRIMASK = 1, all exceptions with configurable priority are masked, so keep the section short.[^tm4c123-datasheet]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
