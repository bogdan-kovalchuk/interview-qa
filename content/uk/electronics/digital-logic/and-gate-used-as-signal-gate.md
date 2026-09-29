---
id: emb-eldig-0005
title: "Як вентиль AND використовується в ролі керованого ключа (gate) для проходження сигналу?"
description: "Як вентиль AND використовується в ролі керованого ключа (gate) для проходження сигналу?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 81 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, логічні вентилі, часові діаграми та цифрові мікросхеми TTL/CMOS."
---

## Short answer

Вентиль AND підпорядковується законам множення <span class="formula">\(X \cdot 1 = X\)</span> та <span class="formula">\(X \cdot 0 = 0\)</span>. Якщо подати сигнал на один вхід, а сигнал дозволу (enable) на інший, за рівня 1 сигнал проходить на вихід без змін. Подання рівня 0 примусово блокує вихід, утримуючи на ньому логічний 0.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
