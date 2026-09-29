---
id: emb-elpcb-0015
title: "Чому стек шарів друкованої плати має бути симетричним і містити парну кількість шарів?"
description: "Чому стек шарів друкованої плати має бути симетричним і містити парну кількість шарів?"
track: electronics
section: pcb-design
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 108 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Плати виготовляють із парною кількістю шарів (2, 4, 6, 8), симетрично розташованих відносно центру, для запобігання деформаціям (вигину та скручуванню). Несиметричний розподіл шарів міді або непарна кількість шарів створюють різницю коефіцієнтів теплового розширення й механічних напружень при гарячому пресуванні та паянні. Це призводить до короблення плати, через що компоненти поверхневого монтажу тріскаються або відриваються від площадок.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
