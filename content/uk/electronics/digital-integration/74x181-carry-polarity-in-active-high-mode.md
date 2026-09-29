---
id: emb-elinteg-0050
title: "Чому сигнали перенесення Cn та Cn+4 у 74x181 мають інверсну полярність при роботі з активними високими даними?"
description: "Чому сигнали перенесення Cn та Cn+4 у 74x181 мають інверсну полярність при роботі з активними високими даними?"
track: electronics
section: digital-integration
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 101 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Мікросхема 74x181 спроєктована для універсальної підтримки як прямої (активний високий), так і інверсної (активний низький) логіки представлення операндів. При використанні активних високих рівнів для даних шина вхідного перенесення Cn є інверсною: Cn = 1 означає відсутність перенесення, а Cn = 0 – наявність. Для операції прямого додавання A + B без попереднього перенесення на вхід Cn слід обов'язково подати логічну одиницю.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
