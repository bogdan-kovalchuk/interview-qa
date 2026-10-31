---
id: emb-irq-0009
title: "How is data transferred between an ISR and the main loop or an RTOS task without race conditions?"
track: embedded
section: interrupts-and-timing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: linux-circular-buffers
    title: "Circular Buffers (Linux kernel documentation)"
    url: https://www.kernel.org/doc/html/latest/core-api/circular-buffers.html
  - source_id: freertos-isr-comms
    title: "FreeRTOS xTaskNotifyFromISR API reference"
    url: https://www.freertos.org/Documentation/02-Kernel/04-API-references/05-Direct-to-task-notifications/02-xTaskNotifyFromISR
---

## Short answer

Use **volatile/atomic flags**, lock-free ring buffers, critical sections, RTOS queues/semaphores or direct task notification. Shared multi-byte state is protected by interrupt disable, mutex in task context or atomic operations, depending on the platform. <span class="warn">`volatile` alone does not make an operation atomic and does not resolve a race condition.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
