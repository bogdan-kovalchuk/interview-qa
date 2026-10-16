---
id: emb-irq-0011
title: "Як працюють hardware timers у режимах PWM, input capture, output compare і one-pulse?"
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

У **PWM** timer рахує період і порівнює counter з duty value, керуючи output pin. **Input capture** зберігає counter на edge для вимірювання часу, а **output compare** генерує подію/зміну pin при match. **One-pulse** запускає одноразовий імпульс заданої тривалості після trigger.[^dou-embedded-interview]

## Detailed explanation

TODO
