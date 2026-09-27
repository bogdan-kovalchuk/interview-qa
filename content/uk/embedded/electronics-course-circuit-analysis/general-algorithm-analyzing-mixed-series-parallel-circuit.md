---
id: emb-elcirc-0020
title: "Який загальний алгоритм аналізу змішаної (series-parallel) схеми?"
description: "Який загальний алгоритм аналізу змішаної (series-parallel) схеми?"
track: embedded
section: electronics-course-circuit-analysis
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
    applicability: "Походження питання й відповіді: картка до лекції 29 курсу на Udemy, перенесена з колоди курсу як є; відповідь не перевірена незалежно від матеріалів курсу."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

1) Замінити послідовні групи одним R. 2) Замінити паралельні групи одним R. 3) Повторювати до R_eq; 4) <span class="formula">\(I_{total}=V_s/R_{eq}\)</span>. 5) Зворотне розгортання: знайти V і I для кожного елемента. 6) Перевірити KCL у вузлах розгалуження.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
