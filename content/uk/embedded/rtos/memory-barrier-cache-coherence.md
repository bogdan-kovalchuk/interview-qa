---
id: emb-rtos-0007
title: "Що таке memory barrier і cache coherence?"
track: embedded
section: rtos
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
---

## Short answer

**Memory barrier** – інструкція або compiler primitive, яка обмежує переупорядкування операцій пам'яті компілятором або CPU. Вона потрібна, коли порядок доступів важливий: lock-free код, MMIO-регістри, DMA, multi-core synchronization.[^dou-embedded-interview]

**Cache coherence** – узгодженість копій даних у кешах різних CPU/core або між cache і пам'яттю, з якою працює DMA. Якщо DMA записав буфер у RAM, CPU може все ще бачити стару copy в cache без invalidate/clean.

Практично: для shared memory використовують atomics/barriers, а для DMA – cache clean/invalidate або non-cacheable buffers залежно від MCU/MPU.

## Detailed explanation

TODO
