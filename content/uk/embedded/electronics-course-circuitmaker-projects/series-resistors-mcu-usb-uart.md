---
id: emb-elcmproj-0054
title: "Навіщо між мікроконтролером і мостом USB-UART послідовно встановлюють резистори 1 кОм?"
description: "Навіщо між мікроконтролером і мостом USB-UART послідовно встановлюють резистори 1 кОм?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 128 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Резистори 1 кОм обмежують наскрізний струм при конфлікті передавачів або замиканні сигнальних ліній шини UART. Вони також дозволяють зовнішньому адаптеру або щиту перехоплювати лінії без відпаювання мікросхеми моста. Додатково опір гасить паразитний брязкіт імпульсів на крутих фронтах сигналів.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
