---
id: emb-elinteg-0058
title: "Чому невідповідність підключення світлодіодного індикатора виходу перенесення призводить до хибного відображення переповнення?"
description: "Чому невідповідність підключення світлодіодного індикатора виходу перенесення призводить до хибного відображення переповнення?"
track: electronics
section: digital-integration
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 103 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Якщо світлодіод увімкнено катодом до виходу мікросхеми, а анодом через резистор до VCC, він світиться при низькому рівні LOW. Якщо вихід перенесення АЛП є активним високим (HIGH при перенесенні), індикатор світитиметься за відсутності перенесення і згасатиме при його виникненні. Полярність увімкнення індикаторів повинна завжди узгоджуватися з активним рівнем конкретного сигналу за даташитом.[^udemy-electronics-course]

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
