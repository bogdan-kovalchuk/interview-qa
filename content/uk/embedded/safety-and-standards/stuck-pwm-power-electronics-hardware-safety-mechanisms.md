---
id: emb-safety-0003
title: "Чому завислий PWM у силовій електроніці може бути небезпечним для hardware і які safety-механізми треба закласти?"
description: "Завислий PWM може залишити MOSFET/IGBT у небезпечному duty або одночасно відкрити плечі, що веде до shoot-through, перегріву чи руйнування навантаження. Потрібні hardware shutdown, dead-time, current/temperature limits, watchdog."
track: embedded
section: safety-and-standards
level: senior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
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
  - source_id: iec-61508-1-2010
    title: "IEC 61508-1:2010 ? Functional safety: General requirements"
    url: https://webstore.iec.ch/en/publication/5515
    accessed: 2026-09-06
    kind: spec
    version: "IEC 61508-1:2010"
    applicability: "Авторитетне джерело рівня секції для понять розділу safety-and-standards; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Завислий PWM може залишити MOSFET/IGBT у небезпечному duty або одночасно відкрити плечі, що веде до shoot-through, перегріву чи руйнування навантаження. Потрібні hardware shutdown, dead-time, current/temperature limits, watchdog, fault inputs timer-а і safe default state pins. <span class="warn">Safety не можна покладати тільки на main loop; критичний вимикач має працювати навіть при зависанні firmware.</span>[^dou-embedded-interview]

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
