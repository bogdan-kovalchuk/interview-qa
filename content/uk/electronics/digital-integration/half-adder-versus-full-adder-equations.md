---
id: emb-elinteg-0044
title: "Чим повний двійковий суматор відрізняється від напівсуматора та якими рівняннями він описується?"
description: "Чим повний двійковий суматор відрізняється від напівсуматора та якими рівняннями він описується?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 100 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Напівсуматор додає лише два однобітні операнди (<span class="formula">\(S = A \oplus B\)</span>, <span class="formula">\(C_{out} = A\cdot B\)</span>), не маючи входу для перенесення. Повний суматор враховує вхідне перенесення <span class="formula">\(C_{in}\)</span> від молодшого розряду. Його виходи описуються формулами <span class="formula">\(S = A \oplus B \oplus C_{in}\)</span> та <span class="formula">\(C_{out} = A\cdot B + C_{in}\cdot(A \oplus B)\)</span>, що дозволяє об'єднувати суматори в ланцюжки довільної розрядності.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
