---
id: emb-eldig-0017
title: "Що таке час встановлення (setup time) і час утримання (hold time) у синхронній логіці?"
description: "Що таке час встановлення (setup time) і час утримання (hold time) у синхронній логіці?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 84 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, логічні вентилі, часові діаграми та цифрові мікросхеми TTL/CMOS."
---

## Short answer

Час встановлення <span class="formula">\(t_{SU}\)</span> – це мінімальний інтервал, протягом якого вхідні дані мають бути стабільними ДО активного фронту тактового сигналу. Час утримання <span class="formula">\(t_H\)</span> – це мінімальний час, протягом якого дані повинні зберігатися незмінними ПІСЛЯ фронту такту. Порушення цих параметрів спричиняє метастабільність тригера або захоплення некоректних даних.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
