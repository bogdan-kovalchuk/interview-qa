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

Вищі <code>-O</code> рівні змінюють instruction order, inline, register allocation і timing, тому delay loops, race conditions і UB можуть проявитися інакше.<br>Debug стає складнішим: змінні optimized out, breakpoints зсуваються, call stack може бути неточним.<br><span class="warn">Коректний firmware не повинен залежати від побічних ефектів UB або не-<code>volatile</code> доступу до MMIO.</span>[^dou-embedded-interview]
## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
