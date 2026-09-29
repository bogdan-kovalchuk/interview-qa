---
id: emb-elinteg-0009
title: "Чому виходи дешифратора 74LS47 виконані за схемою з відкритим колектором?"
description: "Чому виходи дешифратора 74LS47 виконані за схемою з відкритим колектором?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 91 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Виходи з відкритим колектором не мають верхнього підтягувального транзистора і здатні лише замикати вивід на землю. Це дозволяє безпечно вбирати струм до 24 мА на сегмент та комутувати індикатори з напругою живлення вищою за 5 В. Для нормальної роботи кожного сегмента індикатора зі спільним анодом обов'язково встановлюють зовнішній струмообмежувальний резистор.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
