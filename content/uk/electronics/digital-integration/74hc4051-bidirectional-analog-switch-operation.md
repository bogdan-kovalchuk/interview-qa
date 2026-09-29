---
id: emb-elinteg-0019
title: "Як працює мікросхема 74HC4051 у режимах аналогового мультиплексора та демультиплексора?"
description: "Як працює мікросхема 74HC4051 у режимах аналогового мультиплексора та демультиплексора?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 94 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Мікросхема 74HC4051 містить 8 двонапрямлених CMOS-ключів, що з'єднують обраний канал Y0–Y7 зі спільним виводом Z. Завдяки двонапрямленості вона працює як мультиплексор (комутує 8 входів на 1 вихід) або як демультиплексор (розподіляє 1 сигнал на 8 виходів). Керування здійснюється трьома цифровими адресними лініями S0–S2.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
