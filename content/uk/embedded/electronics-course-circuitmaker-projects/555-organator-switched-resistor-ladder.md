---
id: emb-elcmproj-0036
title: "Як комутація ланцюжка резисторів у схемі генератора 555 формує звуковий ряд клавіатури?"
description: "Як комутація ланцюжка резисторів у схемі генератора 555 формує звуковий ряд клавіатури?"
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

У таймері 555 частота прямо залежить від величини опору в ланцюзі скидання: <span class="formula">\(f \approx 1{,}44 / ((R_A + 2R_B)\,C)\)</span>. Кожна клавішна кнопка підключає свій прецизійний резистор <span class="formula">\(R_B\)</span>, задаючи точний час заряду конденсатора. Одночасне натискання кількох кнопок створює паралельне з’єднання резисторів, підвищуючи тон.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
