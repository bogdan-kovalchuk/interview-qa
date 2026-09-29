---
id: emb-elinteg-0041
title: "Як каскадувати компаратори 74x85 для порівняння багаторозрядних слів і як налаштувати перший каскад?"
description: "Як каскадувати компаратори 74x85 для порівняння багаторозрядних слів і як налаштувати перший каскад?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 99 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Для збільшення розрядності виходи A &gt; B, A &lt; B та A = B молодшого компаратора підключають до однойменних входів каскадування старшого. Якщо компаратор працює як одиночний або є першим у каскаді, його вхід A = B обов'язково підтягують до логічної 1, а входи A &gt; B та A &lt; B з'єднують із землею. Інакше при рівності молодших бітів схема видасть помилковий нуль.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
