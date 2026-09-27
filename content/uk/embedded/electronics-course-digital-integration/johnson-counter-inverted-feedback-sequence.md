---
id: emb-elinteg-0027
title: "Яку послідовність станів формує регістр зсуву з інвертованим зворотним зв'язком (лічильник Джонсона)?"
description: "Яку послідовність станів формує регістр зсуву з інвертованим зворотним зв'язком (лічильник Джонсона)?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 95 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Якщо інверсний вихід останнього тригера регістра зсуву підключити до послідовного входу першого розряду, утворюється лічильник Джонсона. Для n-розрядного регістра довжина повного циклу становить <span class="formula">\(2n\)</span> тактових імпульсів. Регістр послідовно заповнюється n одиницями, після чого наступні n тактів послідовно очищають його нулями.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
