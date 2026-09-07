---
id: emb-debug-0004
title: "На осцилографі видно заваду на переході сенсора 0-1. Як відрізнити bounce, EMI, ground issue і sampling problem?"
description: "Bounce зазвичай повторюваний і прив'язаний до механічного edge; EMI може корелювати з motor/PWM/radio events. Ground issue видно як зсув reference, ringing між ground points."
track: embedded
section: debugging-and-tracing
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
  - source_id: gdb-manual
    title: "Debugging with GDB"
    url: https://sourceware.org/gdb/current/onlinedocs/gdb.pdf
    accessed: 2026-09-06
    kind: official
    version: "current"
    applicability: "Авторитетне джерело рівня секції для понять розділу debugging-and-tracing; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Bounce** зазвичай повторюваний і прив'язаний до механічного edge; EMI може корелювати з motor/PWM/radio events. Ground issue видно як зсув reference, ringing між ground points або зміна при іншому probe grounding. Sampling problem проявляється, коли analog сигнал нормальний, але firmware ловить alias/metastability через неправильний threshold, debounce або sample rate.[^dou-embedded-interview]

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
