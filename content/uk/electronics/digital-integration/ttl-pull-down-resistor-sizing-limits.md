---
id: emb-elinteg-0043
title: "Чому резистор притягування до землі номіналом 10 кОм не забезпечує логічного нуля для входів 74LS?"
description: "Чому резистор притягування до землі номіналом 10 кОм не забезпечує логічного нуля для входів 74LS?"
track: electronics
section: digital-integration
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 99 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Входи стандартної логіки TTL серії 74LS у стані нуля виштовхують вхідний струм витоку <span class="formula">\(I_{IL}\)</span> до 0,4 мА. Протікаючи через резистор 10 кОм, цей струм створює спад напруги <span class="formula">\(U = 0{,}4\text{ мА}\times 10\text{ кОм} = 4\text{ В}\)</span>, що значно перевищує поріг <span class="formula">\(V_{IL} \le 0{,}8\text{ В}\)</span>. Для гарантованого нуля на входах TTL опір притягування до землі не повинен перевищувати 470–1000 Ом.[^udemy-electronics-course]

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
