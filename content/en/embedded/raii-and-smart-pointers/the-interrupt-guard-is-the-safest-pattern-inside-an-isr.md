---
id: emb-raii-0030
title: "Which RAII pattern is the safest to use inside an ISR?"
description: "An interrupt-disable and restore scope guard using register-level operations only."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-13; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: ti-tm4c123-datasheet
    title: "Tiva TM4C123GH6PM Microcontroller Data Sheet (Texas Instruments)"
    url: https://www.ti.com/lit/ds/symlink/tm4c123gh6pm.pdf
    accessed: 2026-10-13
    kind: official
    version: "June 12, 2014"
    applicability: "Cortex-M4 register descriptions of PRIMASK and BASEPRI in the TI datasheet: PRIMASK masks exceptions with programmable priority, while Reset, NMI and hard fault have fixed priority; BASEPRI sets the minimum priority for exception processing. It does not describe an RTOS and is not a C++ standard."
  - source_id: freertos-reference-manual
    title: "The FreeRTOS Reference Manual, V10.0.0"
    url: https://www.freertos.org/media/2018/FreeRTOS_Reference_Manual_V10.0.0.pdf
    accessed: 2026-10-13
    kind: official
    version: "V10.0.0"
    applicability: "Sections on API use in interrupt service routines and on taskENTER_CRITICAL_FROM_ISR()/taskEXIT_CRITICAL_FROM_ISR(): API functions not ending in FromISR must not be used in an ISR; on ports that support nesting the FromISR critical section masks interrupts at and below configMAX_SYSCALL_INTERRUPT_PRIORITY; critical sections must be short. It does not describe a particular port or hardware."
---

## Short answer

**Interrupt-disable/restore scope guard, touching registers only.**

It saves PRIMASK (or BASEPRI), disables interrupts in the ctor and restores the saved value in the dtor.[^ti-tm4c123-datasheet] It has no blocking or heap operations, so it can be used inside an ISR.

Rule: inside an RTOS ISR the guard must either touch only registers or call only FromISR API functions; blocking calls stay outside the interrupt.[^freertos-reference-manual]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
