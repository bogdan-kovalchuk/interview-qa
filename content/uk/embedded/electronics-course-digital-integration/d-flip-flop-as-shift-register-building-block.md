---
id: emb-elinteg-0024
title: "Як послідовно з'єднані D-тригери утворюють базову комірку регістра зсуву?"
description: "Як послідовно з'єднані D-тригери утворюють базову комірку регістра зсуву?"
track: embedded
section: electronics-course-digital-integration
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 95 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

D-тригер зберігає значення входу D і передає його на вихід Q за кожним активним фронтом тактового сигналу. Якщо з'єднати вихід Q першого тригера із входом D наступного і подати на них спільний тактовий сигнал, стан просуватиметься на один тригер праворуч за кожен такт. Ланцюжок із n таких тригерів утворює повноцінний n-бітний регістр зсуву.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
