---
id: emb-elcmproj-0051
title: "Як пріоритетний шифратор 74HC148 оптимізує підключення восьми кнопок до мікроконтролера?"
description: "Як пріоритетний шифратор 74HC148 оптимізує підключення восьми кнопок до мікроконтролера?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 127 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Шифратор кодує вісім вхідних сигналів від кнопок у компактний 3-бітний двійковий код: <span class="formula">\(n = \lceil \log_2 8 \rceil = 3\)</span>. Це вивільняє п’ять цінних ліній порту вводу-виводу процесора для іншої периферії. Додатковий груповий вихід GS фіксує факт натискання будь-якої кнопки, формуючи переривання.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
