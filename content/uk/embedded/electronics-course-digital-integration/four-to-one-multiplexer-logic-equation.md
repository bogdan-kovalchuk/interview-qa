---
id: emb-elinteg-0016
title: "Яке булеве рівняння описує логіку роботи цифрового мультиплексора 4:1?"
description: "Яке булеве рівняння описує логіку роботи цифрового мультиплексора 4:1?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 93 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Вихід мультиплексора 4:1 описується сумою добутків інформаційних входів D0–D3 та селекторних ліній S1, S0: <span class="formula">\(Y = \overline{S_1}\cdot\overline{S_0}\cdot D_0 + \overline{S_1}\cdot S_0\cdot D_1 + S_1\cdot\overline{S_0}\cdot D_2 + S_1\cdot S_0\cdot D_3\)</span>. Кожна комбінація адресних ліній розблоковує рівно один тривходовий кон'юнктор AND, передаючи його сигнал через загальний диз'юнктор OR.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
