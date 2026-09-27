---
id: emb-elinteg-0007
title: "Чому логічний сигнал не можна знімати у вузлі між світлодіодом та обмежувальним резистором?"
description: "Чому логічний сигнал не можна знімати у вузлі між світлодіодом та обмежувальним резистором?"
track: embedded
section: electronics-course-digital-integration
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 90 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Світлодіод у прямому напрямку фіксує спад напруги близько 1,8–2,2 В. Якщо зняти логічний сигнал у вузлі між світлодіодом і резистором, напруга потрапляє в невизначену зону логічних рівнів замість повного розмаху VCC або землі. Для надійного зчитування логічний сигнал необхідно підключати безпосередньо до вихідного виводу мікросхеми до резистора.[^udemy-electronics-course]

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
