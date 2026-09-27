---
id: emb-elcmproj-0019
title: "Яку роль відіграє Engineering Change Order при синхронізації змін між схемою та платою?"
description: "Яку роль відіграє Engineering Change Order при синхронізації змін між схемою та платою?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 115 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Механізм ECO зіставляє електричний netlist схеми з поточним станом розводки у документі друкованої плати. Він формує перелік точкових дій: додавання компонентів, оновлення footprint та перепризначення змінених ланцюгів. Це дозволяє гнучко переносити схемні правки на плату без видалення готових трас.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
