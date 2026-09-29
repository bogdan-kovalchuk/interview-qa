---
id: emb-elee-0109
title: "Яка передавальна функція RC-ФВЧ і фаза на частоті зрізу?"
description: "Яка передавальна функція RC-ФВЧ і фаза на частоті зрізу?"
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
    applicability: "Походження питання й відповіді: картка до лекції 51 курсу на Udemy, перенесена з колоди курсу як є; відповідь не перевірена незалежно від матеріалів курсу."
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

<span class="formula">\(H=\frac{j\omega RC}{1+j\omega RC}\)</span>, <span class="formula">\(|H|=\frac{f/f_c}{\sqrt{1+(f/f_c)^2}}\)</span>, <span class="formula">\(\varphi=90^\circ-\arctan(f/f_c)\)</span>, <span class="formula">\(f_c=\frac{1}{2\pi RC}\)</span>. На <span class="formula">\(f_c\)</span> вихід випереджає вхід на 45°.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
