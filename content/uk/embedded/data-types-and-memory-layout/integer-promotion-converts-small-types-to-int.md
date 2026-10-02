---
id: emb-dtypes-0014
title: "Що таке integer promotion у C?"
description: "Integer promotion перетворює цілі типи з рангом не вище int на int або unsigned int у визначених стандартом виразах."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 4
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Integer promotion – **автоматичне перетворення** цілого типу з рангом не вище `int` до `int` або `unsigned int` у виразах, де стандарт C вимагає цього. Якщо `int` може подати всі значення початкового типу, результатом є `int`; інакше – `unsigned int`.

Наприклад, `uint8_t` зазвичай підвищується до `int`, а 16-бітний `unsigned int` може лишитися `unsigned int`; це залежить від діапазонів реалізації.[^iso-c-n1570]

## Detailed explanation

Integer promotions застосовуються до певних операндів, зокрема в unary `+`, `-`, `~`, зсувах і як частина usual arithmetic conversions. Правило не означає, що кожна змінна вузького типу завжди змінює тип у пам'яті: перетворюється значення для конкретного виразу, а оголошений тип об'єкта лишається тим самим.[^iso-c-n1570]

Якщо `int` може представити весь діапазон початкового типу, значення стає `int`. Інакше воно стає `unsigned int`. Тому `uint8_t` переходить до `int` на реалізаціях із типовим мінімумом `INT_MAX` не менше 32767, тоді як 16-бітний `uint16_t` може перейти до `unsigned int`, якщо `int` не вміщує всі його значення.[^iso-c-n1570]

Приклад: два `uint8_t` зі значеннями 200 і 100 підвищуються до `int` до додавання, тож сума у виразі дорівнює 300. Присвоєння цієї суми назад до `uint8_t` перетворює її за модулем 256 і дає 44. Отже, результат у змінній вузького типу пояснюється окремим перетворенням при присвоєнні, а не переповненням під час додавання.[^iso-c-n1570]

**Типова помилка:** робити висновок про тип або переповнення виразу лише з типу змінних-операндів. Перевіряйте promotions та usual arithmetic conversions для конкретної операції й цільової реалізації.

## Sources

<!-- generated from frontmatter -->
