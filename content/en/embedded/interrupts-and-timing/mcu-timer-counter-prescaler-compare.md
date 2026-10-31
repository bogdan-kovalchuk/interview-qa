---
id: emb-irq-0004
title: "How does an MCU timer work: counter, prescaler, auto-reload, compare, and interrupt event?"
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
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/latest/
---

## Short answer

The timer clock is divided by the `prescaler`, after which the `counter` counts ticks. `auto-reload` sets the period for the overflow/update event, and `compare` generates an event when the counter matches a channel. An interrupt or DMA trigger occurs on update/compare/capture if the corresponding flags and NVIC are enabled.[^dou-embedded-interview]

## Detailed explanation

TODO
