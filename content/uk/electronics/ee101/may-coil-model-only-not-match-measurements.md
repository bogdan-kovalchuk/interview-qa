---
id: emb-elee-0081
title: "Чому модель котушки лише з jωL може не збігтися з вимірами і що показує мультиметр на котушці?"
description: "Чому модель котушки лише з jωL може не збігтися з вимірами і що показує мультиметр на котушці?"
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

Реальна обмотка має активний опір <span class="formula">\(r_L\)</span>, паразитну ємність і втрати: точніша модель <span class="formula">\(R+r_L+j\omega L\)</span>. Мультиметр в режимі опору вимірює саме опір дроту, а не індуктивність.[^udemy-electronics-course]

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
