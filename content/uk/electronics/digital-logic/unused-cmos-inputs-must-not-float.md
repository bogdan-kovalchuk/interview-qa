---
id: emb-eldig-0034
title: "Чому невикористані входи мікросхем CMOS не можна залишати непідключеними (floating)?"
description: "Чому невикористані входи мікросхем CMOS не можна залишати непідключеними (floating)?"
track: electronics
section: digital-logic
level: junior
type: pitfall
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 87 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, логічні вентилі, часові діаграми та цифрові мікросхеми TTL/CMOS."
---

## Short answer

Входи польових транзисторів мають величезний опір і поводяться як антени, вловлюючи паразитні наведення. Плаваючий потенціал може потрапити в проміжну лінійну зону між 0 і 1, відкривши обидва комплементарні транзистори одночасно. Це викликає наскрізний струм короткого замикання через живлення, перегрів і вихід мікросхеми з ладу; тому входи з'єднують із VCC або GND.[^udemy-electronics-course]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
