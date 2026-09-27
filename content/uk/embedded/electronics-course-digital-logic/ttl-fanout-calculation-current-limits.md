---
id: emb-eldig-0011
title: "Як обчислюється навантажувальна здатність (fanout) виходу мікросхеми TTL?"
description: "Як обчислюється навантажувальна здатність (fanout) виходу мікросхеми TTL?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 83 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, логічні вентилі, часові діаграми та цифрові мікросхеми TTL/CMOS."
---

## Short answer

Fanout обчислюють окремо для стану HIGH як <span class="formula">\(|I_{OH}| / I_{IH}\)</span> і для стану LOW як <span class="formula">\(I_{OL} / |I_{IL}|\)</span>. Підсумковим fanout вибирають менше з двох отриманих значень. Для мікросхеми 74LS04 за типових паспортних струмів це забезпечує коефіцієнт розгалуження 20 для обох станів.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
