---
id: emb-elee-0241
title: "Чому логічний нуль транзисторного NAND на двох послідовних ключах не дорівнює 0 В?"
description: "Чому логічний нуль транзисторного NAND на двох послідовних ключах не дорівнює 0 В?"
track: electronics
section: ee101
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
    applicability: "Походження питання й відповіді: картка до лекції 77 курсу на Udemy, перенесена з колоди курсу як є; відповідь не перевірена незалежно від матеріалів курсу."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

Кожен насичений транзистор має <span class="formula">\(V_{CE,sat}\)</span> ≈ 0,2 В, тому вихідний нуль ≈ 0,4 В. Реальний рівень залежить від транзисторів, струму, базового керування і навантаження; у NOR для низького виходу достатньо одного провідного транзистора.[^udemy-electronics-course]

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
