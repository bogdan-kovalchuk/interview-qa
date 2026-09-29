---
id: emb-elinteg-0037
title: "Чому нерівномірна буферизація паралельних ліній спричиняє перекіс сигналів (skew)?"
description: "Чому нерівномірна буферизація паралельних ліній спричиняє перекіс сигналів (skew)?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 98 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Кожен буферний елемент додає скінченну затримку поширення сигналу <span class="formula">\(t_{pd}\)</span> (зазвичай від 1 до 10 нс залежно від серії). Якщо частина ліній паралельної шини проходить через буфери, а частина йде напряму, між сигналами виникає часовий зсув (перекіс, skew). Якщо перекіс перевищить допустиме вікно синхронізації, приймач зафіксує спотворені або недійсні дані.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
