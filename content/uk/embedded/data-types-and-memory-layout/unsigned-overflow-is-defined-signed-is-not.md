---
id: emb-dtypes-0049
title: "Що таке unsigned integer overflow і чим він відрізняється від signed?"
description: "Unsigned overflow визначений стандартом як modular arithmetic, а signed overflow - undefined behavior."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
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

Обчислення в unsigned типі визначене за модулем `2^N`, де `N` – ширина цього типу; signed overflow натомість є <span class="warn">undefined behavior</span> за C. Водночас `uint8_t` і часто `uint16_t` спершу підвищуються до `int` у виразі, тому саме додавання `255 + 1` може дати `256`, а нуль з’явиться під час перетворення результату назад до `uint8_t`.[^iso-c-n1570]

## Detailed explanation

Стандарт C по-різному визначає вихід за межі для signed та unsigned типів. Якщо unsigned-операція має результат за верхньою межею свого діапазону, значення зводиться за модулем `2^N`, де `N` – ширина unsigned типу. Для signed арифметики результат, який не представний у типі результату, є undefined behavior; очікуване на певному MCU двійкове обертання не є гарантією мови.[^iso-c-n1570]

Важлива деталь – integer promotions. Операнди типу `uint8_t` зазвичай спершу перетворюються на `int`, якщо `int` може представити всі значення початкового типу. Тоді `uint8_t x = 255; x + 1` обчислює значення `256` у `int`, а присвоєння назад до `uint8_t` дає `0` згідно з правилами перетворення до unsigned типу. Для `uint16_t` це залежить від діапазону `int` у реалізації; не можна вважати тип промоції однаковим на всіх платформах.[^iso-c-n1570]

Практично це розрізнення важливе в лічильниках, таймерах і циклічних буферах. Якщо алгоритму потрібне визначене циклічне значення, unsigned тип виражає цю семантику; водночас звичайна integer promotion може тимчасово розширити тип виразу. Якщо ж важливо обмежити результат конкретною шириною, явне перетворення до цільового unsigned типу задає точку, де модульне зведення відбувається.[^iso-c-n1570]

Signed overflow може зламати логіку перевірок, бо оптимізатор має право припускати, що його не трапляється у визначено виконуваному коді. Наприклад, перевірка після переповненого додавання запізнюється: спочатку потрібна межова перевірка або безпечний helper. Для unsigned теж перевіряють, чи циклічність справді бажана, адже wraparound може приховати помилку довжини чи індексу.[^iso-c-n1570]

**Типові помилки:**
- Називати вираз `uint8_t + 1` обчисленням у восьми бітах без урахування promotions.
- Переносити очікуваний unsigned wraparound на signed типи.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
