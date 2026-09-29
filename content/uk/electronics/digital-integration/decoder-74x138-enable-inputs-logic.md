---
id: emb-elinteg-0004
title: "Навіщо дешифратор 74x138 має три входи дозволу різної полярності?"
description: "Навіщо дешифратор 74x138 має три входи дозволу різної полярності?"
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

Мікросхема 74x138 має два активні низькі входи <span class="formula">\(\overline{E_1}\)</span>, <span class="formula">\(\overline{E_2}\)</span> та один активний високий вхід <span class="formula">\(E_3\)</span>. Дешифрація відбувається лише тоді, коли одночасно подано <span class="formula">\(\overline{E_1}=0\)</span>, <span class="formula">\(\overline{E_2}=0\)</span> і <span class="formula">\(E_3=1\)</span>. Різна полярність дозволів уможливлює легке каскадування дешифраторів або дешифрацію адрес пам'яті без використання зовнішніх логічних вентилів.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
