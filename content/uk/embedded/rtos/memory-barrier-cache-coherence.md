---
id: emb-rtos-0007
title: "Що таке memory barrier і cache coherence?"
description: "Memory barrier обмежує переупорядкування memory operations, а cache coherence узгоджує копії даних між CPU, cache та DMA."
track: embedded
section: rtos
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
---

## Short answer

<span class="key">Memory barrier</span> – інструкція або compiler primitive, яка обмежує переупорядкування операцій пам'яті компілятором або CPU. Вона потрібна, коли порядок доступів важливий: lock-free код, MMIO-регістри, DMA, multi-core synchronization.[^dou-embedded-interview]

<span class="key">Cache coherence</span> – узгодженість копій даних у кешах різних CPU/core або між cache і пам'яттю, з якою працює DMA. Якщо DMA записав буфер у RAM, CPU може все ще бачити стару copy в cache без invalidate/clean.

Практично: для shared memory використовують atomics/barriers, а для DMA – cache clean/invalidate або non-cacheable buffers залежно від MCU/MPU.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
