---
id: emb-eldig-0033
title: "Чому з'єднання виходу 5 В TTL із входом 5 В CMOS потребує підтягувального резистора?"
description: "Чому з'єднання виходу 5 В TTL із входом 5 В CMOS потребує підтягувального резистора?"
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

Стандартний вихід TTL гарантує рівень одиниці лише <span class="formula">\(V_{OH} \ge 2{,}4\text{ В}\)</span>, тоді як вхід CMOS вимагає поріг не менше <span class="formula">\(V_{IH} = 3{,}5\text{ В}\)</span>. Під навантаженням напруга TTL не досягає порогу спрацьовування CMOS, спричиняючи збої логіки. Підтягувальний резистор опором 1–10 кОм до шини +5 В підтягує вихідний рівень до напруги живлення.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
