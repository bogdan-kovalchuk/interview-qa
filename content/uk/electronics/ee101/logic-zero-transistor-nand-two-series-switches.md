---
id: emb-elee-0241
title: "Чому логічний нуль транзисторного NAND на двох послідовних ключах не дорівнює 0 В?"
description: "Чому логічний нуль транзисторного NAND на двох послідовних ключах не дорівнює 0 В?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-14
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 77, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-14; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: nexperia-pmbt3904
    title: "Nexperia PMBT3904 NPN switching transistor datasheet"
    url: https://assets.nexperia.com/documents/data-sheet/PMBT3904.pdf
    accessed: 2026-10-14
    kind: official
    version: null
    applicability: "Максимальна напруга насичення VCEsat PMBT3904: 200 мВ при IC = 10 мА, IB = 1 мА і 300 мВ при IC = 50 мА, IB = 5 мА; інші транзистори мають власні значення."
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
    accessed: 2026-10-14
    kind: official
    version: SCLS181H
    applicability: "Рекомендовані умови й електричні характеристики NAND серії HC: VIH і VIL при VCC 4,5 В, VOH при малому навантаженні; інші сімейства логіки мають інші пороги."
---

## Short answer

У NAND з двома послідовними транзисторами низький рівень дорівнює сумі `V_CE(sat)` обох провідних транзисторів, тому не дорівнює 0 В. Для PMBT3904 максимальне `V_CE(sat)` становить 0,2 В при IC = 10 мА і 0,3 В при IC = 50 мА, тож два транзистори дають до 0,4 В або 0,6 В.[^nexperia-pmbt3904] У NOR з паралельними транзисторами низький рівень задає один провідний транзистор.

## Detailed explanation

Низький рівень з’являється, коли обидва входи в стані 1 і обидва транзистори відкриті до насичення: струм тече від навантаження через верхній транзистор і нижній транзистор до землі. Насичений транзистор не є ідеальним замиканням. Між колектором і емітером лишається напруга насичення `V_CE(sat)`, яка залежить від струму колектора і від базового струму.

Напруга на виході дорівнює сумі напруг обох транзисторів: `V_out = V_CE1(sat) + V_CE2(sat)`. Вузол між транзисторами має напругу `V_CE2(sat)` відносно землі, а верхній транзистор лежить між виходом і цим вузлом. Datasheet PMBT3904 задає максимум `V_CE(sat)` 200 мВ при `IC = 10 мА`, `IB = 1 мА`, і 300 мВ при `IC = 50 мА`, `IB = 5 мА`.[^nexperia-pmbt3904] Для двох однакових транзисторів це дає не більше 0,4 В у першому випадку і не більше 0,6 В у другому.

**Приклад:** SN74HC00 при VCC = 4,5 В має VIL max 1,35 В.[^ti-hc00] Якщо низький рівень NAND дорівнює 0,6 В (максимум при 50 мА), наступний вхід читає його як низький із запасом `1,35 - 0,6 = 0,75 В`. За тими самими даними при 10 мА вихід не перевищує 0,4 В, і запас становить `1,35 - 0,4 = 0,95 В`.

У NOR транзистори з’єднані паралельно, тому низький рівень задає один провідний транзистор і приблизно дорівнює його `V_CE(sat)`, а не сумі двох. Отже, однакові транзистори дають різний низький рівень залежно від топології. Одне число з таблиці не гарантує значення для будь-якого струму.

**Типові помилки:**

- вважати, що насичений транзистор має 0 В між колектором і емітером;
- додавати напруги насичення в NOR з паралельними транзисторами так само, як у NAND з послідовними;
- брати одне типове значення `V_CE(sat)` без перевірки струму з datasheet.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
