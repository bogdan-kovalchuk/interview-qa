---
id: emb-memlink-0014
title: "Як реалізувати ownership і lifetime для буферів без heap у embedded C?"
track: embedded
section: memory-and-linker
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
---

## Short answer

Виділити буфери статично або в pool і явно визначити owner: driver, task, queue чи caller. Передавати не «сирий ресурс назавжди», а handle або descriptor зі станом `free/in_use/done`. Для ISR/DMA добре працюють ring buffer, double buffer і callback/queue, де lifetime завершується після явного release.[^dou-embedded-interview]

## Detailed explanation

TODO
