---
id: emb-elcmproj-0055
title: "Чому лінію аналогового живлення AVCC мікроконтролера підключають через LC-фільтр?"
description: "Чому лінію аналогового живлення AVCC мікроконтролера підключають через LC-фільтр?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 128 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Комутація цифрових блоків ядра мікроконтролера створює значний високочастотний шум на загальній шині живлення VCC. Фільтр із феритової намистинки або дроселя <span class="formula">\(10\ \text{мкГн}\)</span> та конденсатора затримує ці перешкоди. Чисте живлення AVCC забезпечує високу точність і стабільність оцифрування аналогових сигналів.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
