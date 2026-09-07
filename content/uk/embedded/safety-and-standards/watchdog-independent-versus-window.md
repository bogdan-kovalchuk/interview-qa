---
id: emb-safety-0001
title: "Які функції watchdog бувають і чим independent watchdog відрізняється від window watchdog?"
description: "Independent watchdog працює від окремого clock, а window watchdog виявляє refresh як надто ранній, так і надто пізній."
track: embedded
section: safety-and-standards
level: middle
type: concept
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
  - source_id: iec-61508-1-2010
    title: "IEC 61508-1:2010 ? Functional safety: General requirements"
    url: https://webstore.iec.ch/en/publication/5515
    accessed: 2026-09-06
    kind: spec
    version: "IEC 61508-1:2010"
    applicability: "Авторитетне джерело рівня секції для понять розділу safety-and-standards; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Watchdog скидає систему, якщо firmware не виконує refresh у правильний час. **Independent watchdog** зазвичай має окремий low-speed clock і працює навіть при проблемах main clock. **Window watchdog** вимагає refresh не надто рано й не надто пізно, тому ловить як зависання, так і runaway loop.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
