---
id: emb-eldig-0029
title: "З яких логічних вентилів складається напівсуматор (half adder) і які функції вони виконують?"
description: "З яких логічних вентилів складається напівсуматор (half adder) і які функції вони виконують?"
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

Напівсуматор додає два двійкові біти A і B без урахування вхідного переносу. Біт суми S формується елементом XOR за рівнянням <span class="formula">\(S = A \oplus B\)</span>, даючи 1 лише за різних входів. Біт вихідного переносу C формується елементом AND за рівнянням <span class="formula">\(C = A \cdot B\)</span>, спрацьовуючи лише тоді, коли обидва входи дорівнюють 1.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
