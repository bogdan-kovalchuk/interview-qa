---
id: emb-eldig-0028
title: "Чому використання доповнення до двох дозволяє замінити операцію віднімання додаванням?"
description: "Чому використання доповнення до двох дозволяє замінити операцію віднімання додаванням?"
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

Віднімання числа <span class="formula">\(A - B\)</span> математично еквівалентне додаванню протилежного значення <span class="formula">\(A + (-B)\)</span>. Оскільки від'ємне число формується як <span class="formula">\(\overline{B} + 1\)</span>, процесор використовує той самий апаратний суматор для обох дій. Будь-який вихідний біт переносу за межі розрядної сітки під час віднімання просто відкидається.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
