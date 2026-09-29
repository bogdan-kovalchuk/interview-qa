---
id: emb-elcmproj-0041
title: "Навіщо між виходом таймера 555 і базою транзистора підсилювача ставлять розділовий конденсатор?"
description: "Навіщо між виходом таймера 555 і базою транзистора підсилювача ставлять розділовий конденсатор?"
track: electronics
section: circuitmaker-projects
level: junior
type: concept
tags: []
status: published
updated: 2026-09-27
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 123 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Вихідний сигнал таймера 555 містить велику постійну складову на рівні половини живильної напруги. Розділовий конденсатор ізолює постійний струм, пропускаючи на підсилювач виключно змінний акустичний сигнал звукової частоти. Це захищає підсилювальний транзистор від потрапляння в режим насичення або теплового пробою.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
