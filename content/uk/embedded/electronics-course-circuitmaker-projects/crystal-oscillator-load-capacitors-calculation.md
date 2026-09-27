---
id: emb-elcmproj-0053
title: "Як розраховують номінали навантажувальних конденсаторів для кварцового резонатора ATmega328P?"
description: "Як розраховують номінали навантажувальних конденсаторів для кварцового резонатора ATmega328P?"
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

Номінал ємності навантаження резонатора описується формулою: <span class="formula">\(C_L = (C_1 \cdot C_2)/(C_1 + C_2) + C_{stray}\)</span>. За симетричної схеми розрахунок спрощується: <span class="formula">\(C_1 = C_2 = 2\,(C_L - C_{stray})\)</span>. За паразитної ємності плати <span class="formula">\(C_{stray} \approx 4\ \text{пФ}\)</span> для кварцу 16 МГц із <span class="formula">\(C_L = 15\ \text{пФ}\)</span> обирають конденсатори 22 пФ.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
