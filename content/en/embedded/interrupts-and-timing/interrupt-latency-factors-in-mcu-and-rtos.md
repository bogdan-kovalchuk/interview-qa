---
id: emb-irq-0006
title: "What is interrupt latency and what factors increase it in an MCU or RTOS?"
track: embedded
section: interrupts-and-timing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/latest/
  - source_id: freertos-interrupt-config
    title: "FreeRTOS interrupt nesting and priority configuration"
    url: https://www.freertos.org/Documentation/02-Kernel/02-Kernel-features/06-Interrupt-management
---

## Short answer

Interrupt latency is the time from a hardware event to the first useful instruction of the ISR. It is increased by disabled interrupts, higher-priority ISRs, long critical sections, flash wait states, cache misses, bus contention, FPU stacking and RTOS interrupt masking. To reduce latency, keep the ISR short and move heavy work to a task or deferred handler.[^dou-embedded-interview]

## Detailed explanation

TODO
