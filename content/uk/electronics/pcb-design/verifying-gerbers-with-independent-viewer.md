---
id: emb-elpcb-0018
title: "Чому виробничі файли Gerber небезпечно перевіряти лише вбудованим переглядачем CAD?"
description: "Чому виробничі файли Gerber небезпечно перевіряти лише вбудованим переглядачем CAD?"
track: electronics
section: pcb-design
level: junior
type: pitfall
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

Вбудований переглядач САПР часто бере графічні дані з внутрішньої бази проєкту, маскуючи реальні помилки експорту. Сторонній автономний Gerber-переглядач відображає вихідні вектори так, як їх прочитає фотоплотер на заводі. Це дозволяє вчасно виявити зміщення шарів, дзеркальне відображення, пропущені файли свердління, пошкоджені апертури чи інвертовані полігони до оплати виробничої партії.[^udemy-electronics-course]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
