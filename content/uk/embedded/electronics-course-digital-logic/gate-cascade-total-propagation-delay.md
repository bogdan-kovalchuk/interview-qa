---
id: emb-eldig-0014
title: "Як розраховується сумарна затримка поширення сигналу в багатокаскадній комбінаційній схемі?"
description: "Як розраховується сумарна затримка поширення сигналу в багатокаскадній комбінаційній схемі?"
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

Затримка комбінаційної мережі дорівнює сумі затримок поширення всіх послідовних каскадів логічних вентилів уздовж найдовшого шляху. Якщо сигнал проходить через вентиль із затримкою 15 нс, а потім через вентиль із затримкою 10 нс, сумарний час формування результату становить приблизно 25 нс. Цей час визначає мінімальний інтервал між зміною входів і стабільністю вихідних даних.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
