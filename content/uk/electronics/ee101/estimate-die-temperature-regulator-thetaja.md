---
id: emb-elee-0159
title: "Як оцінити температуру кристала стабілізатора 12 В -> 5 В при 0,2 А, якщо <span class=\"formula\">\\(\\theta_{JA}\\)</span> = 60 °C/Вт, <span class=\"formula\">\\(T_a\\)</span> = 25 °C?"
description: "Як оцінити температуру кристала стабілізатора 12 В -> 5 В при 0,2 А, якщо \\(\\theta_{JA}\\) = 60 °C/Вт, \\(T_a\\) = 25 °C?"
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
    applicability: "Походження питання й відповіді: картка до лекції 61 курсу на Udemy, перенесена з колоди курсу як є; відповідь не перевірена незалежно від матеріалів курсу."
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

<span class="formula">\(P_{loss}=(12-5)\cdot 0{,}2=1{,}4\)</span> Вт; <span class="formula">\(T_j\approx T_a+P\,\theta_{JA}=25+1{,}4\cdot 60\approx 109\)</span> °C. Результат порівнюють з допустимою температурою із запасом; <span class="formula">\(\theta_{JA}\)</span> залежить від монтажу і не є універсальною сталою.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
