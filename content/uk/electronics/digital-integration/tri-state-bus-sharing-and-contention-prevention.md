---
id: emb-elinteg-0036
title: "Що таке стан високого імпедансу (Hi-Z) і чому конфлікт шини є небезпечним явищем?"
description: "Що таке стан високого імпедансу (Hi-Z) і чому конфлікт шини є небезпечним явищем?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 98 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

У стані високого імпедансу Hi-Z обидва вихідні транзистори закриті, і вивід не передає струм, електрично від'єднуючись від лінії. Конфлікт шини (bus contention) виникає тоді, коли два або більше драйверів одночасно намагаються видати різні рівні на спільну шину. Це спричиняє протікання великих наскрізних струмів, просідання напруги живлення та можливий тепловий пробій мікросхем.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
