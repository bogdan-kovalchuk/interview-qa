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

Watchdog скидає систему, якщо firmware не виконує refresh у правильний час. <span class="key">Independent watchdog</span> зазвичай має окремий low-speed clock і працює навіть при проблемах main clock. <span class="key">Window watchdog</span> вимагає refresh не надто рано й не надто пізно, тому ловить як зависання, так і runaway loop.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
