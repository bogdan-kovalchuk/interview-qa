---
id: emb-eldig-0038
title: "Чому спільна земляна доріжка багатобітної шини потребує значно більшої ширини, ніж сигнальні лінії?"
description: "Чому спільна земляна доріжка багатобітної шини потребує значно більшої ширини, ніж сигнальні лінії?"
track: electronics
section: digital-logic
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 88 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, логічні вентилі, часові діаграми та цифрові мікросхеми TTL/CMOS."
---

## Short answer

Земляний провідник пропускає одночасний сумарний зворотний струм усіх активних ліній шини. Наприклад, якщо вісім ліній споживають по 100 мА, земляна доріжка повинна витримувати сумарний струм 800 мА. Тонка доріжка шириною 10 mil (фольга 0,5 oz) розрахована лише на 0,5 А і перегріватиметься, тому її ширину збільшують до 25 mil або застосовують суцільний земляний шар.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
