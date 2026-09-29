---
id: emb-elee-0083
title: "Які передавальні функції та частота зрізу RL-кола з виходом на R і на L?"
description: "Які передавальні функції та частота зрізу RL-кола з виходом на R і на L?"
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
    applicability: "Походження питання й відповіді: картка до лекції 46 курсу на Udemy, перенесена з колоди курсу як є; відповідь не перевірена незалежно від матеріалів курсу."
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

<span class="formula">\(H_R=\frac{R}{R+j\omega L}\)</span>, <span class="formula">\(H_L=\frac{j\omega L}{R+j\omega L}\)</span>, <span class="formula">\(f_c=\frac{R}{2\pi L}\)</span>. На <span class="formula">\(f_c\)</span>: <span class="formula">\(|H_R|=|H_L|=\frac{1}{\sqrt{2}}\)</span>, <span class="formula">\(\varphi_R=-45^\circ\)</span>, <span class="formula">\(\varphi_L=+45^\circ\)</span>. Для R = 200 Ом і L = 2,2 мГн <span class="formula">\(f_c\)</span> ≈ 14,47 кГц.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
