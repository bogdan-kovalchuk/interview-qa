---
id: emb-elcmproj-0070
title: "Чому файли Gerber перед замовленням на виробництві обов’язково перевіряють у незалежному переглядачі?"
description: "Чому файли Gerber перед замовленням на виробництві обов’язково перевіряють у незалежному переглядачі?"
track: embedded
section: electronics-course-circuitmaker-projects
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 134 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Вбудований переглядач САПР показує внутрішню базу даних проєкту, маскуючи реальні дефекти файлового експорту. Автономний переглядач (наприклад, Gerbv або ViewMate) відображає саме ті вектори, які отримає виробничий станок. Це дозволяє вчасно виявити розбіжність шарів, пошкодження апертур або зникнення полігонів.[^udemy-electronics-course]

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
