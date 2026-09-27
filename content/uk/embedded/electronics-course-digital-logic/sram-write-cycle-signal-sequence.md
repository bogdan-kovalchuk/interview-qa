---
id: emb-eldig-0020
title: "Яка послідовність сигналів потрібна для коректного циклу запису в мікросхему статичної пам'яті (SRAM)?"
description: "Яка послідовність сигналів потрібна для коректного циклу запису в мікросхему статичної пам'яті (SRAM)?"
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

Спершу на шині встановлюється стабільна адреса комірки пам'яті. Потім активуються сигнал вибору кристала /CE (/CS) та строб запису /WE, а дані виставляються на двонаправлену шину. Шина даних має утримуватися стабільною протягом визначеного вікна встановлення до закінчення імпульсу запису, після чого строб знімається.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
