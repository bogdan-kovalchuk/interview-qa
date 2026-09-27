---
id: emb-elcmproj-0061
title: "Чому вибір резисторів світлодіодів розраховують за сумарним лімітом струму корпусу мікроконтролера?"
description: "Чому вибір резисторів світлодіодів розраховують за сумарним лімітом струму корпусу мікроконтролера?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 130 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Окремий вивід GPIO витримує до <span class="formula">\(20\text{–}40\ \text{мА}\)</span>, але сумарний струм через виводи живлення обмежений лімітом <span class="formula">\(200\ \text{мА}\)</span>. Одночасне ввімкнення кількох світлодіодів загрожує перевантаженням шин і перегрівом кристала. Збільшення опору резисторів до 330–1000 Ом обмежує загальний струм до безпечних меж.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
