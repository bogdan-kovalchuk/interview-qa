---
id: emb-elinteg-0053
title: "Як за допомогою логічних вентилів OR перетворити вісім окремих кнопок на 3-бітний код команди для АЛП?"
description: "Як за допомогою логічних вентилів OR перетворити вісім окремих кнопок на 3-бітний код команди для АЛП?"
track: embedded
section: electronics-course-digital-integration
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 102 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Кожна кнопка відповідає одній математичній операції, генеруючи рівень 1 при натисканні. Кожен розряд вихідного коду S0, S1, S2 формується вентилем OR, на входи якого підключаються лише ті кнопки, у двійковому номері яких відповідний розряд дорівнює 1. Наприклад, біт S0 формується об'єднанням кнопок із непарними кодами 1, 3, 5 та 7.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
