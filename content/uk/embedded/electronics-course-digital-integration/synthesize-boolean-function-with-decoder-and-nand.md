---
id: emb-elinteg-0005
title: "Як реалізувати довільну логічну функцію за допомогою дешифратора 74x138 і одного вентиля NAND?"
description: "Як реалізувати довільну логічну функцію за допомогою дешифратора 74x138 і одного вентиля NAND?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 90 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Виходи 74x138 є активними низькими мінтермами вхідних змінних. За правилом де Моргана вентиль NAND над активними низькими сигналами еквівалентний вентилю OR над прямими мінтермами. Для реалізації функції достатньо подати відповідні виходи дешифратора на входи одного багато- або двовходового елемента NAND.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
