---
id: emb-eldig-0012
title: "Чому навантажувальна здатність мікросхем CMOS обмежується ємністю, а не струмом?"
description: "Чому навантажувальна здатність мікросхем CMOS обмежується ємністю, а не струмом?"
track: embedded
section: electronics-course-digital-logic
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 83 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, логічні вентилі, часові діаграми та цифрові мікросхеми TTL/CMOS."
---

## Short answer

Входи польових транзисторів CMOS мають величезний вхідний опір і мізерний статичний струм витоку. Проте кожен вхід створює паразитну ємність <span class="formula">\(C_I \approx 1\text{–}10\text{ pF}\)</span>, яка навантажує вихід. Максимальний fanout визначається як <span class="formula">\(C_L / C_I\)</span>; перевищення паспортної ємності навантаження C_L затягує фронти сигналів і порушує часові параметри.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
