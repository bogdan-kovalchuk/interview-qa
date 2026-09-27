---
id: emb-elinteg-0010
title: "Як поводиться дешифратор 74LS47 при подачі на входи двійкових кодів від 10 до 15?"
description: "Як поводиться дешифратор 74LS47 при подачі на входи двійкових кодів від 10 до 15?"
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

Мікросхема 74LS47 спроєктована для двійково-десяткового коду BCD (цифри 0–9), а не для повноцінних шістнадцяткових символів A–F. При кодах від 10 до 14 на індикаторі відображаються псевдовипадкові спеціальні символи або кути, а код 15 повністю гасить усі сегменти. Справжні літери A–F потребують спеціалізованих шістнадцяткових дешифраторів або програмованої логіки.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
