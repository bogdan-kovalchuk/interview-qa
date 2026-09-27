---
id: emb-elcmproj-0038
title: "Як величина падіння напруги dropout voltage визначає термін служби батареї пристрою?"
description: "Як величина падіння напруги dropout voltage визначає термін служби батареї пристрою?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 122 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Мінімальна вхідна напруга стабілізації визначається сумою: <span class="formula">\(V_{in(min)} = V_{out} + V_{DO}\)</span>. Зменшення величини <span class="formula">\(V_{DO}\)</span> дозволяє пристрою працювати на пологій ділянці розрядної характеристики батареї нижче 7 В. Літієва батарея типу Крона забезпечує значно стабільнішу напругу порівняно зі звичайною лужною.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
