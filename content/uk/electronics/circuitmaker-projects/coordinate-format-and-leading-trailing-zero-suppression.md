---
id: emb-elcmproj-0069
title: "Що задають формат координат і режим придушення нулів у файлах Gerber і свердління NC Drill?"
description: "Що задають формат координат і режим придушення нулів у файлах Gerber і свердління NC Drill?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 133 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Формат координат (наприклад, 2:4 у дюймах) визначає кількість розрядів, задаючи точність позиціонування <span class="formula">\(0{,}1\ \text{mil}\)</span>. Придушення нулів leading або trailing стискає текстовий файл числових векторів. Розбіжність налаштувань між САПР і CAM-системою призводить до масштабного спотворення розмірів або зсуву отворів.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
