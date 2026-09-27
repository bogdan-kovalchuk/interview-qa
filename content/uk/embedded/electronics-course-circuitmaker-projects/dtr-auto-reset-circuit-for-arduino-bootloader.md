---
id: emb-elcmproj-0057
title: "Як конденсатор 0,1 мкФ у колі DTR забезпечує автоматичне скидання мікроконтролера при прошивці?"
description: "Як конденсатор 0,1 мкФ у колі DTR забезпечує автоматичне скидання мікроконтролера при прошивці?"
track: embedded
section: electronics-course-circuitmaker-projects
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 129 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Коли комп’ютер відкриває COM-порт, лінія DTR переходить у нуль і залишається низькою весь час обміну. Послідовний конденсатор разом із підтяжкою лінії RESET утворює диференціюючий RC-ланцюг. Він генерує короткий негативний імпульс скидання, запускаючи завантажувач у потрібний момент.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
