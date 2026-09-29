---
id: emb-elinteg-0011
title: "Які функції виконують входи /LT, /RBI та /BI/RBO в мікросхемі 74LS47?"
description: "Які функції виконують входи /LT, /RBI та /BI/RBO в мікросхемі 74LS47?"
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

Вхід тестування ламп <span class="formula">\(\overline{LT}\)</span> примусово запалює всі сім сегментів для перевірки їхньої справності. Вхід <span class="formula">\(\overline{RBI}\)</span> (ripple blanking input) гасить незначащі нулі в старших розрядах багаторозрядного числа. Вивід <span class="formula">\(\overline{BI}/\overline{RBO}\)</span> служить для примусового гасіння сегментів або передачі сигналу гасіння в наступний розряд каскаду.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
