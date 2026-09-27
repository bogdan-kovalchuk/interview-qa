---
id: emb-elcmproj-0035
title: "Як рівномірно темперована шкала визначає співвідношення частот сусідніх нот у музичному синтезаторі?"
description: "Як рівномірно темперована шкала визначає співвідношення частот сусідніх нот у музичному синтезаторі?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 121 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

У 12-ступеневій темперованій системі частота кожного наступного півтону зростає в однакове геометричне співвідношення: <span class="formula">\(f_{n+1} = f_n \cdot \sqrt[12]{2} \approx f_n \cdot 1{,}05946\)</span>. Повний інтервал октави з дванадцяти півтонів подвоює вихідну частоту звуку. Розрахунок точних номіналів резисторів у схемі спирається на цей логарифмічний розподіл.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
