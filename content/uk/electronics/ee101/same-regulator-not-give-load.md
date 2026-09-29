---
id: emb-elee-0143
title: "Чому той самий стабілізатор (9 В, 5,1 В, 390 Ом) не дає 5,1 В на навантаженні 100 Ом?"
description: "Чому той самий стабілізатор (9 В, 5,1 В, 390 Ом) не дає 5,1 В на навантаженні 100 Ом?"
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
    applicability: "Походження питання й відповіді: картка до лекції 58 курсу на Udemy, перенесена з колоди курсу як є; відповідь не перевірена незалежно від матеріалів курсу."
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

Для 5,1 В на 100 Ом потрібно 51 мА, а резистор 390 Ом дає лише ≈ 10 мА. Обчислений <span class="formula">\(I_Z\)</span> від’ємний – ознака, що припущення <span class="formula">\(V_{out}\approx V_Z\)</span> хибне. Стабілітрон не проводить, і вихід задає подільник: <span class="formula">\(9\cdot\frac{100}{490}\approx 1{,}84\)</span> В.[^udemy-electronics-course]

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
