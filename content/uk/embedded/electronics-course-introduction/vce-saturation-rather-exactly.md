---
id: emb-elintro-0211
title: "Чому <span class=\"formula\">\\(V_{CE}\\)</span> у насиченні ≈ 0.1–0.2 В, а не точно 0?"
description: "Чому \\(V_{CE}\\) у насиченні ≈ 0.1–0.2 В, а не точно 0?"
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

Залишкове падіння <span class="formula">\(V_{CE(sat)}\)</span> зумовлене внутрішнім опором переходів і контактів. Це не дефект – фізична межа `BJT`. `MOSFET` має ще менше <span class="formula">\(R_{DS(on)}\)</span>. Чим глибше насичення (більший <span class="formula">\(I_B\)</span>), тим менше <span class="formula">\(V_{CE(sat)}\)</span>.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
