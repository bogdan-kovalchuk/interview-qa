---
id: emb-elinteg-0006
title: "Чому світлодіод підключають анодом до живлення, а катодом до виходу дешифратора з активним низьким рівнем?"
description: "Чому світлодіод підключають анодом до живлення, а катодом до виходу дешифратора з активним низьким рівнем?"
track: embedded
section: electronics-course-digital-integration
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

Вихід із активним низьким рівнем переходить у нуль при спрацьовуванні, замикаючи коло на землю та вбираючи струм (sinking). Логічні мікросхеми серії TTL здатні вбирати значно більший вихідний струм <span class="formula">\(I_{OL}\)</span>, ніж віддавати у стані одиниці <span class="formula">\(I_{OH}\)</span>. Тому підключення катода світлодіода через резистор до виходу забезпечує яскраве світіння без перевантаження мікросхеми.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
