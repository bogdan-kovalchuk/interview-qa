---
id: emb-elinteg-0003
title: "Як працює двійковий дешифратор 2:4 і які логічні рівняння описують його виходи?"
description: "Як працює двійковий дешифратор 2:4 і які логічні рівняння описують його виходи?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 89 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Дешифратор перетворює n-бітний вхідний код на активний сигнал на одному з <span class="formula">\(2^n\)</span> виходів. Для двох адресних входів S1 і S0 формуються чотири вихідні мінтерми: <span class="formula">\(Y_0 = \overline{S_1}\cdot\overline{S_0}\)</span>, <span class="formula">\(Y_1 = \overline{S_1}\cdot S_0\)</span>, <span class="formula">\(Y_2 = S_1\cdot\overline{S_0}\)</span> та <span class="formula">\(Y_3 = S_1\cdot S_0\)</span>. У кожен момент часу активним стає рівно один вихід, що відповідає поданому двійковому числу.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
