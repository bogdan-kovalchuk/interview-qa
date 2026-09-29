---
id: emb-elinteg-0066
title: "Чим принципово відрізняються автомати Мура та Мілі і чому виходи автомата Мілі схильні до глітчів?"
description: "Чим принципово відрізняються автомати Мура та Мілі і чому виходи автомата Мілі схильні до глітчів?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 105 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

В автоматі Мура вихідні сигнали залежать виключно від поточного стану, збереженого в тригерах, тому виходи завжди синхронні та вільні від перехідних перешкод. В автоматі Мілі виходи обчислюються як функція поточного стану і безпосередніх зовнішніх входів. Будь-які асинхронні перепади чи брязкіт на входах автомата Мілі можуть миттєво проникати на вихід у вигляді коротких помилкових імпульсів (глітчів).[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
