---
id: emb-elee-0195
title: "Чому в тій самій схемі (`V_B` = 1,7 В, `R_E` = 1 кОм, +5 В) навантаження 4,7 кОм порушує стабілізацію струму?"
description: "Чому в тій самій схемі (`V_B` = 1,7 В, `R_E` = 1 кОм, +5 В) навантаження 4,7 кОм порушує стабілізацію струму?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Походження питання: лекція 68, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; курс не є доказом цих тверджень."
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
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 4.2: I_E = I_C + I_B, I_C = β·I_B; при значно більшому I_C, ніж I_B, I_E ≈ I_C; V_BE ≈ 0,7 В для кремнію. Загальна картина, не для конкретного транзистора."
  - source_id: fiore-bjt-collector-curves
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.3 BJT Collector Curves"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.3:_BJT_Collector_Curves"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 4.3: три зони колекторних характеристик – насичення ліворуч (V_CE(sat) кілька десятих вольта), майже постійний струм посередині для лінійних підсилювачів і пробій праворуч. Загальна картина, не для конкретного транзистора."
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 4.6: навантажувальна пряма, Q-точка (I_CQ, V_CEQ) лежить на ній; якщо розрахунковий струм перевищує граничний, транзистор у насиченні й реальний струм дорівнює граничному; типове V_CE(sat) близько десятої вольта, у прикладі 0,15 В при I_C = 10 мА і I_B = 0,3 мА. Точні значення беруть із графіків транзистора."
---

## Short answer

Навантаження 4,7 кОм між +5 В і колектором при 1 мА падає 4,7 В, тож `V_C` ≈ 0,3 В, тобто нижче за `V_E` ≈ 1 В. Колектор має бути вище емітера щонайменше на напругу насичення, яка становить кілька десятих вольта.[^fiore-bjt-collector-curves] Без цього транзистор виходить із зони постійного струму, і струм через навантаження падає.

## Detailed explanation

Схема працює як джерело струму. База тримається на 1,7 В, тому емітер лежить приблизно на 0,7 В нижче: `V_E` = 1,7 В - 0,7 В = 1,0 В. Струм емітера задає резистор: `I_E` = 1,0 В / 1 кОм = 1 мА. Для кремнію `V_BE` ≈ 0,7 В, а `I_E` = `I_C` + `I_B` і `I_C` = β*`I_B`. Оскільки `I_C` значно більший за `I_B`, колекторний струм практично дорівнює `I_E`, тобто 1 мА, поки транзистор працює в активному режимі.[^fiore-bjt-basics]

Навантаження між +5 В і колектором при `I_C` = 1 мА має падіння 1 мА * 4,7 кОм = 4,7 В, тож колектор опиняється на 5 В - 4,7 В = 0,3 В. Це нижче за емітер: `V_CE` = 0,3 В - 1,0 В = -0,7 В. Щоб транзистор лишався в зоні постійного струму, `V_CE` має бути вище напруги насичення. У прикладі підручника `V_CE(sat)` ≈ 0,15 В при `I_C` = 10 мА і `I_B` = 0,3 мА, а для малосигнальних приладів воно типово становить близько десятої вольта.[^fiore-bjt-dc-load-line]

Приймемо `V_CE(sat)` ≈ 0,15 В як орієнтир. Тоді колектор не опускається нижче `V_E` + 0,15 В ≈ 1,15 В, і найбільше навантаження, яке ще дає 1 мА, становить (5 В - 1,15 В) / 1 мА ≈ 3,85 кОм. За 4,7 кОм транзистор входить у насичення. Якщо `V_B` лишається ідеальним джерелом (емітер на 1,0 В, база віддає надлишок ≈ 0,18 мА), то струм через навантаження стає (5 В - 1,15 В) / 4,7 кОм ≈ 0,82 мА, тобто на 18 % менше за 1 мА. Підручник пояснює, що коли розрахунковий струм перевищує граничний, транзистор насичений і реальний струм дорівнює граничному.[^fiore-bjt-dc-load-line]

Щоб зберегти 1 мА, перевірку запасу напруги варто зробити до розрахунку струму: `V_CC` - `I_C`*`R_L` >= `V_E` + `V_CE(sat)`. Для 4,7 кОм і 1 мА це дає `V_CC` >= 5,85 В. Інакше треба або підняти живлення, або зменшити навантаження приблизно до 3,85 кОм. Точне `V_CE(sat)` залежить від струму й транзистора, тож його беруть із графіків даташита.[^fiore-bjt-dc-load-line]

**Типові помилки:**

- Вважати, що `R_E` задає 1 мА за будь-якого навантаження, не перевіривши напругу на колекторі.
- Брати `V_CE(sat)` = 0: тоді запас напруги здається більшим, ніж є насправді.[^fiore-bjt-dc-load-line]
- Порівнювати колекторну напругу із землею замість `V_CE`, тобто з напругою відносно емітера.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
