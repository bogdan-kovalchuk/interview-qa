---
id: emb-irq-0011
title: "How do hardware timers work in PWM, input capture, output compare, and one-pulse modes?"
track: embedded
section: interrupts-and-timing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
---

## Short answer

In **PWM** the timer counts the period and compares the counter with the duty value, driving the output pin. **Input capture** stores the counter value on an edge for time measurement, and **output compare** generates an event/pin change on match. **One-pulse** produces a single pulse of a given duration after a trigger.[^dou-embedded-interview]

## Detailed explanation

TODO
