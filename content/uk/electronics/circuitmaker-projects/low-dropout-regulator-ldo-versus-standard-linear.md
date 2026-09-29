---
id: emb-elcmproj-0037
title: "Чому для живлення схеми від 9-вольтової батареї потрібен стабілізатор LDO замість LM7805?"
description: "Чому для живлення схеми від 9-вольтової батареї потрібен стабілізатор LDO замість LM7805?"
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

Класичний лінійний регулятор LM7805 вимагає різниці напруг між входом і виходом не менше <span class="formula">\(2{,}0\text{–}2{,}5\ \text{В}\)</span>. Стабілізатор LDO з падінням всього <span class="formula">\(0{,}65\ \text{В}\)</span> підтримує вихідні <span class="formula">\(5\ \text{В}\)</span> при розряді батареї аж до <span class="formula">\(5{,}65\ \text{В}\)</span>. Це дозволяє корисно вичерпати майже всю енергію джерела живлення.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
