---
id: emb-eldig-0019
title: "Як працює вхід асинхронного скидання /CLR у тригері D-типу?"
description: "Як працює вхід асинхронного скидання /CLR у тригері D-типу?"
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

Вхід /CLR зазвичай є активним низьким (active-low) і діє асинхронно, тобто незалежно від стану входу D чи тактового сигналу CLK. Подання логічного 0 на /CLR негайно переводить вихід Q у стан 0 (а /Q – в 1) із власною затримкою поширення. У робочому режимі цей вхід підтягують до VCC резистором 10 кОм для запобігання хибному скиданню.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
