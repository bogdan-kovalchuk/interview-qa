---
id: emb-elcmproj-0004
title: "Як побудовано каскад керування світлодіодами у схемі бігучого вогника магічної палички?"
description: "Як побудовано каскад керування світлодіодами у схемі бігучого вогника магічної палички?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 111 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Генератор на таймері 555 виробляє тактові імпульси частотою кілька герц для двійкового лічильника 74HC393. Три старші біти лічильника надходять на входи дешифратора 74HC138, який по черзі активує один із восьми каналів. Активний низький рівень виходу запалює відповідний світлодіод, створюючи ефект вогника.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
