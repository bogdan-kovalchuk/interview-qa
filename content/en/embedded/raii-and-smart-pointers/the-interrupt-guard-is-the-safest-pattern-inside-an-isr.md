---
id: emb-raii-0030
title: "Which RAII pattern is the safest to use inside an ISR?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: ti-tm4c123-datasheet
    title: "Tiva TM4C123GH6PM Microcontroller Data Sheet (Texas Instruments)"
    url: https://www.ti.com/lit/ds/symlink/tm4c123gh6pm.pdf
  - source_id: freertos-reference-manual
    title: "The FreeRTOS Reference Manual, V10.0.0"
    url: https://www.freertos.org/media/2018/FreeRTOS_Reference_Manual_V10.0.0.pdf
---

## Short answer

**Interrupt-disable/restore scope guard, touching registers only.**

It saves PRIMASK (or BASEPRI), disables interrupts in the ctor and restores the saved value in the dtor.[^ti-tm4c123-datasheet] It has no blocking or heap operations, so it can be used inside an ISR.

Rule: inside an RTOS ISR the guard must either touch only registers or call only FromISR API functions; blocking calls stay outside the interrupt.[^freertos-reference-manual]

## Detailed explanation

TODO
