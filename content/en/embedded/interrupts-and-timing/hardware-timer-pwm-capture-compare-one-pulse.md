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
  - source_id: st-an4013
    title: "STMicroelectronics Application Note AN4013: STM32 cross-series timer overview"
    url: https://www.st.com/resource/en/application_note/an4013-stm32-crossseries-timer-overview-stmicroelectronics.pdf
---

## Short answer

In **PWM** mode, the timer counts the period and compares the counter against a duty value to drive an output pin. **Input capture** latches the counter on an external edge to measure signal timing, while **output compare** generates an event or toggles a pin on match. **One-pulse** mode generates a single pulse of a defined duration after a trigger.[^dou-embedded-interview]

## Detailed explanation

TODO
