---
id: emb-elinteg-0017
title: "Які рівні встановлюються на виходах мультиплексора 74x151 при деактивованому вході дозволу?"
description: "Які рівні встановлюються на виходах мультиплексора 74x151 при деактивованому вході дозволу?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 93 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Коли вхід дозволу <span class="formula">\(\overline{E}\)</span> встановлено у стан 1 (заборона), мікросхема 74x151 не переводить виходи у високоімпедансний стан Hi-Z. Натомість прямий вихід Y примусово фіксується в логічний 0, а інверсний вихід <span class="formula">\(\overline{Y}\)</span> – у логічну 1 незалежно від вхідних сигналів. Для отримання Hi-Z на спільній шині потрібні мікросхеми з трьома станами виходу.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
