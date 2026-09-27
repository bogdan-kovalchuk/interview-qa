---
id: emb-elinteg-0030
title: "Чому послідовні логічні схеми обов'язково потребують початкового скидання після ввімкнення живлення?"
description: "Чому послідовні логічні схеми обов'язково потребують початкового скидання після ввімкнення живлення?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 96 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

При подачі напруги живлення внутрішні тригери та регістри переходять у випадкові стани, обумовлені асиметрією порогів окремих транзисторів. Без примусової ініціалізації цифрова система починає виконання з невизначеного або забороненого стану. Спеціальне асинхронне коло скидання (POR) утримує сигнал скидання активним до повної стабілізації напруги живлення.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
