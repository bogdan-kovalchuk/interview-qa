---
id: emb-eldig-0018
title: "Як пара послідовних інверторів допомагає усунути порушення часу встановлення або утримання?"
description: "Як пара послідовних інверторів допомагає усунути порушення часу встановлення або утримання?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 84 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, логічні вентилі, часові діаграми та цифрові мікросхеми TTL/CMOS."
---

## Short answer

Якщо сигнал надходить на вхід мікросхеми занадто рано відносно тактового фронту, його затримують за допомогою каскаду буферів. Два послідовні інвертори відновлюють вихідний логічний рівень сигналу, додаючи сумарну затримку поширення обох вентилів. Наприклад, два інвертори із затримкою по 5 нс забезпечують затримку 10 нс без зміни логічного змісту сигналу.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
