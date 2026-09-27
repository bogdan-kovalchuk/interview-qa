---
id: emb-elcmproj-0049
title: "Чому зворотний шлях струму динаміка відокремлюють від земляного контуру генератора 555?"
description: "Чому зворотний шлях струму динаміка відокремлюють від земляного контуру генератора 555?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 126 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Потужні імпульсні струми навантаження динаміка викликають спади напруги на омічному опорі земляних провідників. Якщо цей струм проходить через спільну земляну шину таймера, виникає паразитний зворотний зв’язок. Це призводить до плавання висоти звуку, хрипів та низькочастотного самозбудження генератора.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
