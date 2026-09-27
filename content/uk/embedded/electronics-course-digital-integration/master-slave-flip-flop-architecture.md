---
id: emb-elinteg-0061
title: "Як двоступенева архітектура Master-Slave усуває явище перегонів в імпульсних тригерах?"
description: "Як двоступенева архітектура Master-Slave усуває явище перегонів в імпульсних тригерах?"
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

Конструкція Master-Slave складається з двох послідовних тригерів, тактованих протифазними тактовими сигналами. Поки тактовий імпульс високий, відкритий вхідний тригер Master, який фіксує значення входу, тоді як вихідний Slave заблокований. При переході такту в низький рівень Master від'єднується від входів, а Slave переписує зафіксований стан на вихід Q, унеможливлюючи наскрізне проходження перешкод.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
