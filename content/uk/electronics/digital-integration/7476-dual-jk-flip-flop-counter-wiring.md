---
id: emb-elinteg-0070
title: "Як налаштувати мікросхему 7476 для реалізації 2-бітного асинхронного лічильника?"
description: "Як налаштувати мікросхему 7476 для реалізації 2-бітного асинхронного лічильника?"
track: electronics
section: digital-integration
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 106 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Для переведення обох JK-тригерів мікросхеми 7476 у лічильний режим на їхні входи J і K подають логічну одиницю (VCC). Тактовий імпульс генератора надходить на вхід такту першого тригера, а прямий вихід Q0 підключається до тактового входу другого розряду. Асинхронні входи встановлення <span class="formula">\(\overline{PR}\)</span> та скидання <span class="formula">\(\overline{CLR}\)</span> утримують у високому рівні, використовуючи при потребі для миттєвого обнулення.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
