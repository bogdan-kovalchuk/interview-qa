---
id: emb-elee-0199
title: "Як врахувати навантаження подільника зміщення базою транзистора?"
description: "Як врахувати навантаження подільника зміщення базою транзистора?"
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
    applicability: "Походження питання й відповіді: картка до лекції 69 курсу на Udemy, перенесена з колоди курсу як є; відповідь не перевірена незалежно від матеріалів курсу."
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

Подільник замінюють еквівалентом Тевеніна: <span class="formula">\(V_{TH}=V_{CC}\frac{R_2}{R_1+R_2}\)</span>, <span class="formula">\(R_{TH}=R_1\parallel R_2\)</span>. Тоді <span class="formula">\(I_B\approx\frac{V_{TH}-V_{BE}}{R_{TH}+(\beta+1)R_E}\)</span> і <span class="formula">\(V_B=V_{TH}-I_BR_{TH}\)</span>.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
