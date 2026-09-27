---
id: emb-elcmproj-0018
title: "Як обмеження вихідного струму логіки серії 74HC впливає на вибір резисторів для світлодіодів?"
description: "Як обмеження вихідного струму логіки серії 74HC впливає на вибір резисторів для світлодіодів?"
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

Вихідні каскади логіки 74HC гарантують номінальний струм близько <span class="formula">\(4\text{–}6\ \text{мА}\)</span> при максимальному ліміті <span class="formula">\(25\ \text{мА}\)</span>. Сучасні світлодіоди забезпечують достатню яскравість уже при струмі <span class="formula">\(2\text{–}3\ \text{мА}\)</span>. Обмежувальні резистори 470–1000 Ом задають безпечний струм споживання, виключаючи перегрів і пошкодження кристала мікросхеми.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
