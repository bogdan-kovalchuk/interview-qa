---
id: emb-elee-0189
title: "Які основні співвідношення струмів BJT і чому <span class=\"formula\">\\(I_C=\\beta I_B\\)</span> не завжди виконується?"
description: "Які основні співвідношення струмів BJT і чому \\(I_C=\\beta I_B\\) не завжди виконується?"
track: electronics
section: ee101
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
    applicability: "Походження питання й відповіді: картка до лекції 67 курсу на Udemy, перенесена з колоди курсу як є; відповідь не перевірена незалежно від матеріалів курсу."
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

<span class="formula">\(I_E=I_C+I_B\)</span>; в активному режимі <span class="formula">\(I_C\approx\beta I_B\)</span>, <span class="formula">\(V_B=V_E+V_{BE}\)</span> (<span class="formula">\(V_{BE}\)</span> ≈ 0,6–0,7 В). При <span class="formula">\(I_B\)</span> = 20 мкА і β = 100 модель дає 2 мА, але якщо колекторне коло дозволяє лише 1 мА, транзистор насичується, і формула не діє.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
