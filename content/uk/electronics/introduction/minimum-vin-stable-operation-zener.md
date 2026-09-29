---
id: emb-elintro-0189
title: "Яка мінімальна <span class=\"formula\">\\(V_{in}\\)</span> для стабільної роботи Зенера 5.1 В?"
description: "Яка мінімальна \\(V_{in}\\) для стабільної роботи Зенера 5.1 В?"
track: electronics
section: introduction
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
    applicability: "Походження питання й відповіді: картка до лекції 18 курсу на Udemy, перенесена з колоди курсу як є; відповідь не перевірена незалежно від матеріалів курсу."
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

<span class="formula">\(V_{in}\)</span> повинна забезпечити <span class="formula">\(I_{total}\)</span> &gt; <span class="formula">\(I_{Z(min)}\)</span> + <span class="formula">\(I_{load}\)</span>. Практично: <span class="formula">\(V_{in}\)</span> ≥ <span class="formula">\(V_Z\)</span> + 3 В = ≥ 8 В для Зенера 5.1 В. При меншій напрузі Зенер виходить з активного режиму і <span class="formula">\(V_{out}\)</span> падає.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
