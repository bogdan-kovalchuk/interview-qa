---
id: emb-irq-0007
title: "How is delay implemented in firmware, and why is busy-wait often worse than a timer-based approach?"
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
  - source_id: freertos-task-delay
    title: "FreeRTOS vTaskDelay API reference"
    url: https://www.freertos.org/Documentation/02-Kernel/04-API-references/01-Task-control/01-vTaskDelay
  - source_id: cmsis-core-cm4-header
    title: "CMSIS 6: core_cm4.h (Cortex-M4 core peripheral access layer)"
    url: https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Core/Include/core_cm4.h
  - source_id: cmsis-core-systick
    title: "CMSIS-Core (Cortex-M): SysTick Timer"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__SysTick__gr.html
---

## Short answer

Delay can be a busy loop, CPU cycle counter, SysTick, hardware timer or RTOS sleep. **Timer-based delay** better preserves CPU time, allows sleep/power saving and does not break when the clock or optimization changes. <span class="warn">Busy-wait blocks the main loop/task and scales poorly for ISR-driven or RTOS firmware.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
