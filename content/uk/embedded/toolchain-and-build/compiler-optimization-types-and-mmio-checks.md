---
id: emb-build-0019
title: "Які типи optimization використовує компілятор і як перевірити, що оптимізація не зламала MMIO або delay loop?"
description: "Компілятор робить inlining, dead-code elimination, constant propagation, loop optimization, instruction scheduling і LTO.MMIO перевіряй через volatile…"
track: embedded
section: toolchain-and-build
level: senior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу toolchain-and-build; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Компілятор робить inlining, dead-code elimination, constant propagation, loop optimization, instruction scheduling і LTO. MMIO перевіряй через `volatile` register definitions, barriers там, де потрібен порядок, disassembly/map review і target tests. <span class="warn">Busy delay loop без `volatile`, timer або intrinsic barrier може бути скорочений чи прибраний оптимізатором.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
