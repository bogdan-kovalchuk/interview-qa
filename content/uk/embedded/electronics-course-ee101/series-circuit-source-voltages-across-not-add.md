---
id: emb-elee-0064
title: "Послідовне RC-коло: R = 100 Ом, <span class=\"formula\">\\(X_C\\)</span> = 75 Ом, джерело 10 В RMS. Чому напруги на R і C (8 В і 6 В) не дають у сумі 14 В?"
description: "Послідовне RC-коло: R = 100 Ом, \\(X_C\\) = 75 Ом, джерело 10 В RMS. Чому напруги на R і C (8 В і 6 В) не дають у сумі 14 В?"
track: embedded
section: electronics-course-ee101
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
    applicability: "Походження питання й відповіді: картка до лекції 42 курсу на Udemy, перенесена з колоди курсу як є; відповідь не перевірена незалежно від матеріалів курсу."
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

Z = 100 − j75 = 125∠−36,87° Ом, I = 0,08∠36,87° А. Напруги на R і C зсунуті на 90°, тому додаються як перпендикулярні вектори: <span class="formula">\(\sqrt{8^2+6^2}=10\)</span> В. Додавання модулів замість фазорів – типова помилка.[^udemy-electronics-course]

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
