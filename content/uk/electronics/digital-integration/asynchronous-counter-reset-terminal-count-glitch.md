---
id: emb-elinteg-0072
title: "Чому скидання лічильника 7493 на заданому коді породжує короткочасний паразитний імпульс (глітч)?"
description: "Чому скидання лічильника 7493 на заданому коді породжує короткочасний паразитний імпульс (глітч)?"
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

Асинхронні входи скидання R0(1) і R0(2) спрацьовують лише тоді, коли дешифратор виявляє код кінцевого стану (наприклад, 13 при рахунку до 12). Отже, код 13 мусить фізично з'явитися на виходах лічильника на кілька наносекунд, перш ніж сигнал через вентиль обнулить тригери. Цей короткий перехідний імпульс (глітч) може бути помилково сприйнятий швидкими зовнішніми мікросхемами як дійсний стан.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
