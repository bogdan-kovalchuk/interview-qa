---
id: emb-elintro-0009
title: Що означають 4 смуги на резисторі?
description: Що означають 4 смуги на резисторі?
track: electronics
section: introduction
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
anki:
  export: true
sources:
- source_id: udemy-electronics-course
  title: 'Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу'
  url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  accessed: 2026-09-27
  kind: community
  version: null
  applicability: 'Historical question provenance: lecture 3 of the Udemy course. Original flashcards remain in imports.
    Current answers and explanations were independently revised against cited technical sources on 2026-10-04; this
    source is not factual proof of the revised prose.'
- source_id: aac-direct-current
  title: 'All About Circuits textbook, Volume I: DC'
  url: https://www.allaboutcircuits.com/textbook/direct-current/
  accessed: 2026-09-27
  kind: book
  version: null
  applicability: 'Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання;
    конкретні номінали й схеми курсу можуть відрізнятися.'
- source_id: aac-semiconductors
  title: 'All About Circuits textbook, Volume III: Semiconductors'
  url: https://www.allaboutcircuits.com/textbook/semiconductors/
  accessed: 2026-09-27
  kind: book
  version: null
  applicability: 'Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела
    живлення; конкретні номінали й схеми курсу можуть відрізнятися.'
- source_id: vishay-colors
  title: Vishay resistor color code chart
  url: https://www.vishay.com/docs/49411/resistor_color_code_calculator.pdf
  accessed: 2026-10-04
  kind: official
  version: null
  applicability: Four/five band digits, multipliers and tolerances.
---

## Short answer

У four-band resistor code дві смуги задають significant digits, третя – multiplier, четверта – tolerance. Brown-black-red-gold означає `10 × 100 = 1000 Ω` з tolerance ±5%; multiplier також може бути дробовим. [^vishay-colors]

## Detailed explanation

Four-band code читають від кінця з digits до tolerance band, яку часто відділяє більший проміжок. Brown – це 1, black – 0, тому значуще число дорівнює 10, а не десятковому 1.0. Red множить на 100; gold задає ±5%. [^vishay-colors]

Отже, nominal value – 1 kΩ. Розрахунковий tolerance interval становить від `1000*(1-0.05)` до `1000*(1+0.05)`, тобто 950–1050 Ω за умов specification. Це не обіцянка, що температура чи aging ніколи не змінять опір за межі початкового tolerance interval.

Gold у ролі multiplier означає 0.1, silver – 0.01, тому пояснення multiplier лише як «дописування нулів» неповне. Five-band code має три significant digits, після яких ідуть multiplier та tolerance. Спочатку визначте формат коду; роль кольору залежить від позиції смуги. [^vishay-colors]

## Sources

<!-- generated from frontmatter -->
