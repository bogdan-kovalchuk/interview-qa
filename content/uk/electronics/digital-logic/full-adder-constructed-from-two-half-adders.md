---
id: emb-eldig-0030
title: "Як будується повний суматор (full adder) на основі двох напівсуматорів і додаткового вентиля?"
description: "Як будується повний суматор (full adder) на основі двох напівсуматорів і додаткового вентиля?"
track: electronics
section: digital-logic
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 86 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, логічні вентилі, часові діаграми та цифрові мікросхеми TTL/CMOS."
---

## Short answer

Перший напівсуматор додає вхідні біти A і B, формуючи проміжну суму та перший перенос. Другий напівсуматор додає отриману суму з бітом вхідного переносу C_IN, утворюючи фінальну суму <span class="formula">\(S = A \oplus B \oplus C_{IN}\)</span>. Вихідні переноси обох напівсуматорів об'єднуються через двовходовий елемент OR для формування сумарного переносу <span class="formula">\(C_{OUT}\)</span>.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
