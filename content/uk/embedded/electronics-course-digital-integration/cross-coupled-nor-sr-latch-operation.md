---
id: emb-elinteg-0060
title: "Як працює асинхронний SR-тригер на двох елементах NOR і чому комбінація S = 1, R = 1 є забороненою?"
description: "Як працює асинхронний SR-тригер на двох елементах NOR і чому комбінація S = 1, R = 1 є забороненою?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 104 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Два елементи NOR із перехресним зворотним зв'язком зберігають біт завдяки циркуляції сигналу: подача S = 1 встановлює Q = 1, а R = 1 скидає Q = 0; при S = R = 0 стан зберігається. Якщо одночасно подати S = 1 і R = 1, обидва виходи Q та <span class="formula">\(\overline{Q}\)</span> примусово переходять у нуль, порушуючи умову інверсності. При одночасному знятті входів у 00 схема потрапляє в стан перегонів і переходить у непередбачуваний рівень.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
