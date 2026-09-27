---
id: emb-elee-0179
title: "Джерело 9 В RMS 50 Гц, міст, C = 1000 мкФ, навантаження 0,1 А. Які пульсації і дно напруги на C?"
description: "Джерело 9 В RMS 50 Гц, міст, C = 1000 мкФ, навантаження 0,1 А. Які пульсації і дно напруги на C?"
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
    applicability: "Походження питання й відповіді: картка до лекції 65 курсу на Udemy, перенесена з колоди курсу як є; відповідь не перевірена незалежно від матеріалів курсу."
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

Частота пульсацій 100 Гц, <span class="formula">\(\Delta V_{pp}\approx\frac{0{,}1}{100\cdot 0{,}001}=1\)</span> Вpp. Дно: <span class="formula">\(\sqrt{2}\cdot 9-2\cdot 0{,}7-1\approx 10{,}33\)</span> В. Потрібно <span class="formula">\(V_{in,trough}&gt;V_{out}+V_{dropout}\)</span>.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
