---
id: emb-elinteg-0034
title: "Чому в регістрах зсуву на макетних платах виникають помилкові спрацьовування та зайві біти?"
description: "Чому в регістрах зсуву на макетних платах виникають помилкові спрацьовування та зайві біти?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 97 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Безпайкові макетні плати та довгі сполучні дроти мають високу паразитну ємність (до 2–5 пФ на контакт) і паразитну індуктивність. Швидкі фронти перемикання світлодіодних навантажень створюють стрибки напруги по шинах живлення та землі, що наводяться на тактовий вхід. У результаті регістр сприймає перешкоду як додатковий тактовий імпульс і записує зайві одиниці.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
