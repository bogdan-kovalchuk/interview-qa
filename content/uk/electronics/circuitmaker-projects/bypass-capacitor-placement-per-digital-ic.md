---
id: emb-elcmproj-0016
title: "Чому біля кожного корпусу цифрової мікросхеми обов’язково ставлять керамічний конденсатор 0,1 мкФ?"
description: "Чому біля кожного корпусу цифрової мікросхеми обов’язково ставлять керамічний конденсатор 0,1 мкФ?"
track: electronics
section: circuitmaker-projects
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 114 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Під час логічного перемикання цифрові мікросхеми створюють короткі високочастотні імпульси струму споживання. Індуктивність доріжок живлення викликає паразитне просідання напруги та взаємні збої сусідніх мікросхем. Керамічний конденсатор упритул до виводів живлення служить джерелом локального заряду, шунтуючи перешкоди.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
