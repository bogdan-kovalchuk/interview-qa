---
id: emb-build-0018
title: "Як compiler optimization levels впливають на timing, debug і undefined behavior у firmware?"
description: "Вищі -O рівні змінюють instruction order, inline, register allocation і timing, тому delay loops, race conditions і UB можуть проявитися інакше.Debug …"
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

Вищі `-O` рівні змінюють instruction order, inline, register allocation і timing, тому delay loops, race conditions і UB можуть проявитися інакше. Debug стає складнішим: змінні optimized out, breakpoints зсуваються, call stack може бути неточним. <span class="warn">Коректний firmware не повинен залежати від побічних ефектів UB або не-`volatile` доступу до MMIO.</span>[^dou-embedded-interview]

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
