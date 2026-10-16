---
id: emb-irq-0004
title: "Як працює таймер MCU: counter, prescaler, auto-reload, compare і interrupt event?"
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

Timer clock ділиться через `prescaler`, після чого `counter` рахує ticks. `auto-reload` задає період overflow/update event, а `compare` генерує подію при збігу counter з каналом. Interrupt або DMA trigger виникає на update/compare/capture, якщо відповідні flags і NVIC enabled.[^dou-embedded-interview]

## Detailed explanation

TODO
