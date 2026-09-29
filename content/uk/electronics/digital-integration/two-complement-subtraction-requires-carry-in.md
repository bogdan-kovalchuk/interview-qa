---
id: emb-elinteg-0056
title: "Чому при виконанні віднімання в АЛП на основі доповнювального коду необхідно примусово подавати вхідне перенесення?"
description: "Чому при виконанні віднімання в АЛП на основі доповнювального коду необхідно примусово подавати вхідне перенесення?"
track: electronics
section: digital-integration
level: junior
type: pitfall
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 103 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Операція віднімання в апаратному забезпеченні реалізується як додавання доповнення: <span class="formula">\(B - A = B + \overline{A} + 1\)</span>. Інверсія операнда <span class="formula">\(\overline{A}\)</span> формує лише зворотний (одиничний) код. Для перетворення його на справжній доповнювальний код необхідно додати одиницю через вхід перенесення <span class="formula">\(C_n = 1\)</span>, інакше отриманий результат буде рівно на 1 меншим за правильний.[^udemy-electronics-course]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
