---
id: emb-elintro-0213
title: "Як розрахувати <span class=\"formula\">\\(R_B\\)</span> для гарантованого насичення транзистора?"
description: "Як розрахувати \\(R_B\\) для гарантованого насичення транзистора?"
track: embedded
section: electronics-course-introduction
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
    applicability: "Походження питання й відповіді: картка до лекції 20 курсу на Udemy, перенесена з колоди курсу як є; відповідь не перевірена незалежно від матеріалів курсу."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

1) <span class="formula">\(I_{C(max)}\)</span> = <span class="formula">\(V_{CC}\)</span> / <span class="formula">\(R_C\)</span>. 2) <span class="formula">\(I_{B(min)}\)</span> = <span class="formula">\(I_{C(max)}\)</span> / <span class="formula">\(\beta_{min}\)</span>. 3) Беремо <span class="formula">\(I_B\)</span> = 5 × <span class="formula">\(I_{B(min)}\)</span> (overdrive для надійності). 4) <span class="formula">\(R_B\)</span> = (<span class="formula">\(V_{in}\)</span> − <span class="formula">\(V_{BE}\)</span>) / <span class="formula">\(I_B\)</span>. Округлюємо до стандарту у меншу сторону.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
