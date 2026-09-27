---
id: emb-eldig-0031
title: "Які дві умови рівнів напруг необхідні для прямої сумісності логічних сімейств?"
description: "Які дві умови рівнів напруг необхідні для прямої сумісності логічних сімейств?"
track: embedded
section: electronics-course-digital-logic
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 87 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, логічні вентилі, часові діаграми та цифрові мікросхеми TTL/CMOS."
---

## Short answer

Для передачі сигналу логічної 1 мінімальна вихідна напруга передавача має перевищувати поріг приймача: <span class="formula">\(V_{OH} \ge V_{IH}\)</span>. Для логічного 0 максимальна вихідна напруга передавача має бути нижчою за вхідний поріг приймача: <span class="formula">\(V_{OL} \le V_{IL}\)</span>. Окрім напруги, вихід передавача повинен забезпечувати необхідний вхідний струм навантаження в обох станах.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
