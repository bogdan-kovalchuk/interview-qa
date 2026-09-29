---
id: emb-elinteg-0022
title: "Як паразитні параметри аналогового ключа 74HC4051 впливають на пропускання високочастотних сигналів?"
description: "Як паразитні параметри аналогового ключа 74HC4051 впливають на пропускання високочастотних сигналів?"
track: electronics
section: digital-integration
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 94 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Ключ має власний внутрішній опір у відкритому стані <span class="formula">\(R_{ON}\)</span> та паразитні ємності відносно підкладки й суміжних каналів. Ці параметри утворюють RC-фільтр низьких частот, що обмежує смугу пропускання та викликає завал фронтів імпульсних сигналів. На високих частотах (від одиниць мегагерців) прямокутні імпульси зазнають викидів і дзвону через паразитні індуктивності макетних з'єднань.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
