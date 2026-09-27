---
id: emb-elee-0079
title: "RL-коло: R = 200 Ом, L = 2,2 мГн, f = 100 Гц, вхід 7 В RMS. Чому напруга на котушці лише близько 48 мВ?"
description: "RL-коло: R = 200 Ом, L = 2,2 мГн, f = 100 Гц, вхід 7 В RMS. Чому напруга на котушці лише близько 48 мВ?"
track: embedded
section: electronics-course-ee101
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
    applicability: "Походження питання й відповіді: картка до лекції 45 курсу на Udemy, перенесена з колоди курсу як є; відповідь не перевірена незалежно від матеріалів курсу."
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

<span class="formula">\(X_L=2\pi\cdot 100\cdot 0{,}0022\approx 1{,}38\)</span> Ом – набагато менше за 200 Ом. Тому I ≈ 35,0 мА∠−0,4°, <span class="formula">\(V_R\)</span> ≈ 7,00 В, а <span class="formula">\(V_L\)</span> ≈ 48,4 мВ∠89,6°. Майже вся напруга падає на резисторі.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
