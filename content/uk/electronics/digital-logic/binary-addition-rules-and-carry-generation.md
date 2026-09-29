---
id: emb-eldig-0025
title: "Які правила діють для однорозрядного додавання двійкових чисел і формування переносу?"
description: "Які правила діють для однорозрядного додавання двійкових чисел і формування переносу?"
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

Додавання нуля дає <span class="formula">\(0 + 0 = 0\)</span> та <span class="formula">\(1 + 0 = 1\)</span> без переносу. Сума двох одиниць <span class="formula">\(1 + 1 = 0\)</span> із переносом 1 у старший розряд, оскільки результат дорівнює двійковому числу 10₂ (десяткова 2). Додавання трьох одиниць <span class="formula">\(1 + 1 + 1 = 1\)</span> із формуванням вихідного переносу 1 у наступний розряд (число 11₂).[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
