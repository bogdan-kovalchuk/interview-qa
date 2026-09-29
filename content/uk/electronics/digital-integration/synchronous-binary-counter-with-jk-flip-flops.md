---
id: emb-elinteg-0063
title: "Як побудувати синхронний двійковий лічильник на JK-тригерах і чому в ньому відсутня затримка поширення?"
description: "Як побудувати синхронний двійковий лічильник на JK-тригерах і чому в ньому відсутня затримка поширення?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 104 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

У синхронному лічильнику тактові входи всіх тригерів з'єднані паралельно до одного генератора, тому перемикання відбувається одночасно. Молодший тригер має входи J0 = K0 = 1, а для кожного наступного входи з'єднують із виходом Q попередніх розрядів (J1 = K1 = Q0, J2 = K2 = Q0·Q1). Завдяки паралельному тактуванню час встановлення всього лічильника дорівнює затримці лише одного тригера.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
