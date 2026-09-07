---
id: emb-debug-0005
title: "Які прості hardware і firmware методи прибирають noise/bounce на цифровому вході сенсора?"
description: "Hardware: pull-up/pull-down, RC filter, Schmitt trigger, shielding/grounding, series resistor або opto/isolator. Firmware: debounce timer, majority vote, state machine з stable time, interrupt masking."
track: embedded
section: debugging-and-tracing
level: senior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 3
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
  - source_id: gdb-manual
    title: "Debugging with GDB"
    url: https://sourceware.org/gdb/current/onlinedocs/gdb.pdf
    accessed: 2026-09-06
    kind: official
    version: "current"
    applicability: "Авторитетне джерело рівня секції для понять розділу debugging-and-tracing; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Hardware: pull-up/pull-down правильного номіналу, RC filter, Schmitt trigger, shielding/grounding, series resistor або opto/isolator за потреби. Firmware: debounce timer, majority vote, state machine з stable time, interrupt masking на debounce window. <span class="warn">Не маскуй firmware-фільтром проблему wiring/grounding, якщо noise може пошкодити input або викликати safety event.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
