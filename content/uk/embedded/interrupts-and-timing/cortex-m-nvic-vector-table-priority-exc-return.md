---
id: emb-irq-0005
title: "Як працює interrupt handling на Cortex-M: NVIC, vector table, priority і return from ISR?"
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

Vector table містить initial SP і addresses handlers; NVIC enable-ить IRQ, виставляє pending state і вибирає найвищий priority. При вході в ISR Cortex-M автоматично stacking-ить частину registers, переходить у handler mode і може робити nested interrupts. Return from ISR через спеціальне `EXC_RETURN` відновлює context; у RTOS це також точка для context switch.[^dou-embedded-interview]

## Detailed explanation

TODO
