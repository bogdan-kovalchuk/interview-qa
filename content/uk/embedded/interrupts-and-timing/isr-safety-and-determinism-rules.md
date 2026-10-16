---
id: emb-irq-0008
title: "Що таке ISR і які правила роблять ISR безпечною та передбачуваною?"
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

**ISR** - це interrupt service routine, код який виконується у відповідь на hardware/software interrupt. Вона має бути короткою, deterministic, не blocking, без heap і довгих locks, з мінімальним shared state. Типовий патерн: clear interrupt flag, забрати/покласти мінімальні дані, notify task або main loop.[^dou-embedded-interview]

## Detailed explanation

TODO
