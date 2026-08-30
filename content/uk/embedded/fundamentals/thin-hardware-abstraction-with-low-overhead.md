---
id: emb-fund-0021
title: "Як абстрагувати hardware layer без надмірного runtime overhead?"
description: "Тримай abstraction тонкою: inline functions, static dispatch, templates у C++, function tables тільки там, де потрібна runtime заміна.HAL boundary має…"
track: embedded
section: fundamentals
level: senior
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

Тримай abstraction тонкою: inline functions, static dispatch, templates у C++, function tables тільки там, де потрібна runtime заміна.<br><span class="key">HAL boundary</span> має приховувати register details, але не маскувати timing, blocking behavior, DMA ownership або interrupt context.<br><span class="warn">Надто товстий HAL робить driver непередбачуваним і важким для debug на MCU.</span>[^dou-embedded-interview]
## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
