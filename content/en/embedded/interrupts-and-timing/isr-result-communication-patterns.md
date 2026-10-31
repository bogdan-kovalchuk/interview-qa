---
id: emb-irq-0010
title: "Why should an ISR not return a result like a regular function, and what patterns are used instead?"
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
  - source_id: freertos-isr-comms
    title: "FreeRTOS xTaskNotifyFromISR API reference"
    url: https://www.freertos.org/Documentation/02-Kernel/04-API-references/05-Direct-to-task-notifications/02-xTaskNotifyFromISR
  - source_id: linux-circular-buffers
    title: "Linux kernel: Circular Buffers"
    url: https://docs.kernel.org/core-api/circular-buffers.html
---

## Short answer

An ISR is invoked by a hardware/CPU exception mechanism, not by a caller expecting a return value. Results are passed through flags, buffers, queues, semaphores, event bits or deferred work/task notification. **An ISR should signal an event**, while heavy processing belongs in the main loop, a worker task or a bottom half.[^dou-embedded-interview]

## Detailed explanation

TODO
