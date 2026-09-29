---
id: emb-eldig-0013
title: "Навіщо в цифрових схемах потрібен тристабільний буфер і стан Hi-Z?"
description: "Навіщо в цифрових схемах потрібен тристабільний буфер і стан Hi-Z?"
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

Пряме з'єднання звичайних виходів призводить до короткого замикання, якщо один чіп видає 1, а інший 0. Тристабільний буфер має вхід дозволу (зазвичай активний низький /OE), за вимкнення якого вихід переходить у стан високого імпедансу Hi-Z. У стані Hi-Z опір виходу становить мегаоми, що дозволяє кільком мікросхемам почергово працювати на спільну шину даних.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
