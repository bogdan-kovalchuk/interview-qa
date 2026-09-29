---
id: emb-elcirc-0013
title: "Як KCL доводить формулу паралельного з'єднання резисторів?"
description: "Як KCL доводить формулу паралельного з'єднання резисторів?"
track: electronics
section: circuit-analysis
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
    applicability: "Походження питання й відповіді: картка до лекції 28 курсу на Udemy, перенесена з колоди курсу як є; відповідь не перевірена незалежно від матеріалів курсу."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

При однакових вузлах A і B: <span class="formula">\(I_s = I_1+I_2 = V/R_1 + V/R_2 = V(1/R_1+1/R_2)\)</span>. Але також <span class="formula">\(I_s=V/R_{eq}\)</span> -> <span class="formula">\(1/R_{eq}=1/R_1+1/R_2\)</span>. Для двох: <span class="formula">\(R_{eq}=R_1R_2/(R_1+R_2)\)</span>.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
