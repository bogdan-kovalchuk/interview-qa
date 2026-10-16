---
id: emb-irq-0007
title: "Як реалізований delay у firmware і чому busy-wait delay часто гірший за timer-based підхід?"
track: embedded
section: interrupts-and-timing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
---

## Short answer

Delay може бути busy loop, CPU cycle counter, SysTick, hardware timer або RTOS sleep. **Timer-based delay** краще зберігає CPU time, дозволяє sleep/power saving і не ламається від зміни clock чи optimization. <span class="warn">Busy-wait блокує main loop/task і погано масштабується для ISR-driven або RTOS firmware.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
