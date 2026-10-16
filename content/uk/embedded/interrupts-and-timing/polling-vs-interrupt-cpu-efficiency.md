---
id: emb-irq-0001
title: "В чому різниця між polling і interrupt?"
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

**Polling** – CPU постійно опитує стан периферії в циклі: `while(!(UART->SR & TXE));`.[^dou-embedded-interview] Просто реалізувати, але CPU зайнятий навіть без подій, тому витрачається потужність і час.

**Interrupt** – периферія сигналізує CPU лише при наявності події. CPU виконує основний код, а при сигналі переривання – зберігає контекст і виконує ISR; ефективне використання CPU, низька латентність.

Вибір: polling – для простих випадків з передбачуваними подіями; interrupt – коли події нечасті, асинхронні або потрібна низька латентність.

## Detailed explanation

TODO
