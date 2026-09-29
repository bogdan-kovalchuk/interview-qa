---
id: emb-elee-0195
title: "Чому в тій самій схемі (<span class=\"formula\">\\(V_B\\)</span> = 1,7 В, <span class=\"formula\">\\(R_E\\)</span> = 1 кОм, +5 В) навантаження 4,7 кОм порушує стабілізацію струму?"
description: "Чому в тій самій схемі (\\(V_B\\) = 1,7 В, \\(R_E\\) = 1 кОм, +5 В) навантаження 4,7 кОм порушує стабілізацію струму?"
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
    applicability: "Походження питання й відповіді: картка до лекції 68 курсу на Udemy, перенесена з колоди курсу як є; відповідь не перевірена незалежно від матеріалів курсу."
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

Для 1 мА потрібно ≈ 4,65 В на навантаженні, тобто <span class="formula">\(V_C\approx 0{,}35\)</span> В – нижче за <span class="formula">\(V_E\)</span> ≈ 1 В. Модель стає непридатною, і струм зменшується: джерелу струму потрібен запас напруги (compliance).[^udemy-electronics-course]

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
