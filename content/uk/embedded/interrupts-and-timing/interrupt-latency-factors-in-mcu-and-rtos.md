---
id: emb-irq-0006
title: "Що таке interrupt latency і які фактори її збільшують у MCU або RTOS?"
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

Interrupt latency – час від hardware event до виконання першої корисної інструкції ISR. Її збільшують disabled interrupts, вищі priority ISR, довгі critical sections, flash wait states, cache misses, bus contention, FPU stacking і RTOS interrupt masking. Для зменшення latency ISR має бути короткою, а важку роботу треба переносити в task/deferred handler.[^dou-embedded-interview]

## Detailed explanation

TODO
