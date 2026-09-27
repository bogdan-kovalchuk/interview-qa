---
id: emb-elcmproj-0059
title: "Як схема на діодах Шотткі захищає пристрій при одночасному живленні від USB і зовнішньої батареї?"
description: "Як схема на діодах Шотткі захищає пристрій при одночасному живленні від USB і зовнішньої батареї?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 129 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Діоди вмикають за схемою «Монтажне АБО» у ланцюги живлення від порту USB та акумуляторної батареї. Струм автоматично споживається від лінії з вищим потенціалом, блокуючи друге джерело зворотним зміщенням. Мале падіння на діодах Шотткі захищає комп’ютерний порт USB від зустрічного струму батареї.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
