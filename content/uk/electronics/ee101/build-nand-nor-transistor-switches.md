---
id: emb-elee-0237
title: "Як із транзисторних ключів отримати NAND, NOR, AND і OR?"
description: "Як із транзисторних ключів отримати NAND, NOR, AND і OR?"
track: electronics
section: ee101
level: junior
type: concept
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
    applicability: "Походження питання: лекція 76, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-14; курс не є доказом цих тверджень."
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
  - source_id: montana-eele414-cmos
    title: "Montana State University EELE 414: CMOS combinational logic, module 6 lecture notes"
    url: "https://www.montana.edu/aolson/eele414/lecture_notes/eele414_module_06_logic.pdf"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Лекційні нотатки EELE 414 (модуль 6, CMOS-комбінаційна логіка): правило «послідовно – AND, паралельно – OR» для мережі; у NAND NMOS у pull-down стоять послідовно, у NOR – паралельно. Розглянуто CMOS, не NPN-ключі; правило мережі те саме."
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Підручник, розділ 4.6: навантажувальна пряма V_CE = V_CC - I_C*R_C, тобто I_C = (V_CC - V_CE)/R_C; для малосигнальних приладів V_CE(sat) порядку десятих вольта (приклад: 0,15 В при 10 мА). Загальна картина, не для конкретного транзистора."
---

## Short answer

Два NPN послідовно до землі (вихід підтягнутий до плюса) замикають вихід на землю лише тоді, коли обидва входи високі – NAND.[^montana-eele414-cmos] Два паралельно – вихід падає за будь-якого високого входу – NOR. Вихідний інвертор перетворює NAND на AND, а NOR на OR.

## Detailed explanation

Вихід з резистором pull-up до плюса має лише два стани: якщо мережа від виходу до землі провідна, вихід низький, а інакше його піднімає резистор. Тому вихід дорівнює інверсії умови провідності: `Y = NOT(f)`, де `f` – умова, за якої мережа проводить. Послідовно з’єднані транзистори дають `f = A*B`, паралельні – `f = A+B`. У CMOS-нотатках те саме правило: послідовно означає AND, паралельно – OR.[^montana-eele414-cmos]

Приклад NAND з двох NPN. При `A = 0` верхній транзистор закритий, шлях розірваний, і вихід через резистор високий. При `A = B = 1` обидва транзистори насичені (за достатнього струму бази), і вихід падає до суми їхніх `V_CE,sat`. Якщо кожен `V_CE,sat` ≈ 0.1 V, низький рівень становить ≈ 0.2 V; якщо кожен ≈ 0.15 V (значення прикладу Fiore при 10 мА), то ≈ 0.3 V.[^fiore-bjt-dc-load-line] Отже, низький рівень зростає з кількістю послідовно з’єднаних транзисторів, і це треба враховувати при виборі логіки.

NOR будують паралельно: вихід падає, якщо відкритий будь-який із двох транзисторів, тобто `Y = NOT(A+B)`. Щоб отримати AND або OR, до NAND чи NOR додають інвертор на виході (наприклад, однотранзисторний каскад із резистором pull-up): `NOT(NOT(A*B)) = A*B` і `NOT(NOT(A+B)) = A+B`. Без такого інвертора мережа дає лише NAND чи NOR.

**Типові помилки:**

- Плутати послідовне й паралельне з’єднання: послідовне дає умову «всі входи високі», паралельне – «будь-який високий».[^montana-eele414-cmos]
- Вважати, що NAND з двох NPN дає AND без інвертора: вихід NAND інвертований.
- Залишати незадіяний вхід плаваючим: база без визначеного потенціалу дає невизначений стан транзистора.

## Sources

<!-- generated from frontmatter -->
