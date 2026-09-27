---
id: emb-eldig-0004
title: "Чому тотожності з комплементом X·/X = 0 та X + /X = 1 важливі для оптимізації логіки?"
description: "Чому тотожності з комплементом X·/X = 0 та X + /X = 1 важливі для оптимізації логіки?"
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

Змінна та її інверсія завжди набувають протилежних значень 0 і 1. Оскільки AND із нулем завжди дає 0, добуток <span class="formula">\(X \cdot \overline{X} = 0\)</span>. Оскільки OR з одиницею дає 1, сума <span class="formula">\(X + \overline{X} = 1\)</span>. Це дозволяє усувати зайві змінні та логічні вентилі з цифрової схеми без зміни її поведінки.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
