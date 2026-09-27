---
id: emb-elcmproj-0015
title: "Що необхідно робити з входами невикористаної половини мікросхеми КМОН-лічильника 74HC393?"
description: "Що необхідно робити з входами невикористаної половини мікросхеми КМОН-лічильника 74HC393?"
track: embedded
section: electronics-course-circuitmaker-projects
level: junior
type: pitfall
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 114 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Вхідні каскади КМОН мають колосальний вхідний опір і легко вловлюють електростатичні перешкоди з навколишнього середовища. Вільний вхід зміщується в проміжну зону, викликаючи відкриття обох транзисторів і наскрізні струми споживання. Для запобігання паразитній генерації всі вільні входи жорстко садять на землю.[^udemy-electronics-course]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
