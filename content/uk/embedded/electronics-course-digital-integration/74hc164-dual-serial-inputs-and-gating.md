---
id: emb-elinteg-0029
title: "Як організовані послідовні входи в мікросхемі 74HC164 і як їх використовують для стробування даних?"
description: "Як організовані послідовні входи в мікросхемі 74HC164 і як їх використовують для стробування даних?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 96 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Мікросхема 74HC164 має два послідовні входи DSA і DSB, які всередині об'єднані двовходовим логічним елементом AND. Це дозволяє використовувати один із входів як інформаційний канал, а другий – як лінію дозволу (стробування). Якщо на керуючий вхід подано 0, надходження даних блокується і в регістр зсуваються виключно нулі.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
