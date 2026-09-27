---
id: emb-elcmproj-0052
title: "Чому напругу шини USB не можна розглядати як стабільне й прецизійне джерело 5,0 В?"
description: "Чому напругу шини USB не можна розглядати як стабільне й прецизійне джерело 5,0 В?"
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

Специфікація USB допускає коливання напруги живлення в діапазоні від <span class="formula">\(4{,}75\ \text{В}\)</span> до <span class="formula">\(5{,}25\ \text{В}\)</span> зі значними пульсаціями. До того ж довгі кабелі створюють динамічні спади напруги під навантаженням. Для точних вимірювань вбудованим АЦП обов’язково використовують стабілізовані джерела опорної напруги.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
