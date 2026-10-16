---
id: emb-irq-0010
title: "Чому ISR не має повертати результат як звичайна функція і які патерни використовують замість цього?"
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

ISR викликається hardware/CPU exception механізмом, а не caller-ом, який чекає return value. Результат передають через flags, buffers, queues, semaphores, event bits або deferred work/task notification. **ISR має сигналізувати подію**, а важку обробку виконувати у main loop, worker task або bottom half.[^dou-embedded-interview]

## Detailed explanation

TODO
