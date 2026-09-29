---
id: emb-elinteg-0008
title: "Чим відрізняються семисегментні індикатори зі спільним анодом та спільним катодом?"
description: "Чим відрізняються семисегментні індикатори зі спільним анодом та спільним катодом?"
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

В індикаторі зі спільним анодом аноди всіх сегментів з'єднані разом і підключаються до позитивної шини VCC, а окремі сегменти вмикаються подачею низького рівня (LOW) на катоди. В індикаторі зі спільним катодом усі катоди заземлені, а сегменти запалюються високим рівнем (HIGH) на анодах. Відповідно, для спільного анода використовують драйвер 74LS47, а для спільного катода – 74LS48.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
