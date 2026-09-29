---
id: emb-eldig-0032
title: "Чому вихід 5-вольтової мікросхеми CMOS може напряму керувати входом 5-вольтового TTL?"
description: "Чому вихід 5-вольтової мікросхеми CMOS може напряму керувати входом 5-вольтового TTL?"
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

Вихід 5-вольтового CMOS забезпечує <span class="formula">\(V_{OH} \approx 4{,}4\text{–}4{,}5\text{ В}\)</span>, що значно перевищує вхідний поріг <span class="formula">\(V_{IH} = 2{,}0\text{ В}\)</span> мікросхеми TTL. Вихідний рівень нуля <span class="formula">\(V_{OL} \le 0{,}4\text{ В}\)</span> також впевнено лежить нижче порогу <span class="formula">\(V_{IL} = 0{,}8\text{ В}\)</span>. Розробнику потрібно лише переконатися, що вихід CMOS здатен приймати втікаючий струм <span class="formula">\(I_{IL} \approx 0{,}4\text{ мА}\)</span> вхідного каскаду TTL.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
