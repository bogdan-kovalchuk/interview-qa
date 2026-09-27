---
id: emb-elinteg-0049
title: "Як здійснюється вибір між логічними та арифметичними функціями в мікросхемі АЛП 74x181?"
description: "Як здійснюється вибір між логічними та арифметичними функціями в мікросхемі АЛП 74x181?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 101 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Вибір режиму роботи 74x181 визначається керуючим входом M: коли M = 1 (HIGH), блок виконує одну з 16 побітових логічних функцій без участі внутрішнього перенесення. Коли M = 0 (LOW), схема виконує одну з 16 арифметичних операцій з урахуванням перенесення. Конкретна операція всередині обраного режиму кодується 4-бітним словом на селекторних входах S3–S0.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
