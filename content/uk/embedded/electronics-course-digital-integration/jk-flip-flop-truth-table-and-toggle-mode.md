---
id: emb-elinteg-0062
title: "Які стани формує універсальний JK-тригер і чому режим J = 1, K = 1 є фундаментальним для лічильників?"
description: "Які стани формує універсальний JK-тригер і чому режим J = 1, K = 1 є фундаментальним для лічильників?"
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

JK-тригер усуває заборонений стан SR-тригера: при J = 0, K = 0 стан зберігається, при 10 – встановлюється 1, при 01 – скидається в 0. Комбінація J = 1, K = 1 переводить тригер у режим лічильного перемикання (toggle), коли кожен тактовий імпульс інвертує вихід на протилежний. Завдяки цьому JK-тригер є ідеальним дільником частоти на 2 і базовою коміркою двійкових лічильників.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
