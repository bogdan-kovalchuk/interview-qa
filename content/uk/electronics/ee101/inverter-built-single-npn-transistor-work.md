---
id: emb-elee-0236
title: "Як працює інвертор на одному NPN-транзисторі?"
description: "Як працює інвертор на одному NPN-транзисторі?"
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
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Підручник, розділ 4.2: V_BE ≈ 0,7 В для кремнію у прямому включенні; для малосигнальних приладів β типово 100–200. Загальна картина, не для конкретного транзистора."
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Підручник, розділ 4.6: навантажувальна пряма V_CE = V_CC - I_C*R_C, тобто I_C = (V_CC - V_CE)/R_C; для малосигнальних приладів V_CE(sat) порядку десятих вольта (приклад: 0,15 В при 10 мА). Загальна картина, не для конкретного транзистора."
---

## Short answer

Колектор через `R_C` підтягнутий до живлення, емітер на землі, вхід через `R_B` подається на базу. Низький вхід тримає транзистор у відсічці, і вихід піднімається; високий вхід насичує його, і вихід падає до низького рівня, тобто інвертує сигнал (NOT). Навантажувальна пряма `I_C = (V_CC - V_CE)/R_C` при 5 В, `R_C = 4.7 kOhm` і насиченні `V_CE,sat ≈ 0.2 V` дає колекторний струм ≈ 1,02 мА.[^fiore-bjt-dc-load-line]

## Detailed explanation

Транзистор тут працює як ключ. При низькому вході напруга база–емітер менша за напругу відкривання, струм бази майже не тече, колекторний струм нульовий, і через `R_C` не падає напруга: вихід дорівнює напрузі живлення. При високому вході база отримує струм через `R_B`, і кремнієвий перехід база–емітер відкривається за напруги близько 0,7 В.[^fiore-bjt-basics] Тоді струм бази `I_B = (V_in - 0.7) / R_B`.

Колекторний струм визначає зовнішнє коло, а не лише коефіцієнт β. Навантажувальна пряма описує це співвідношення: `V_CE = V_CC - I_C*R_C`, тобто `I_C = (V_CC - V_CE)/R_C`.[^fiore-bjt-dc-load-line] Коли транзистор насичений, `V_CE` падає до `V_CE,sat`, який для малосигнальних приладів становить десяті частки вольта (у прикладі Fiore – 0,15 В при 10 мА). Тому низький вихід дорівнює кільком десятим вольта, а не нулю.

Щоб транзистор насичувався, фактичний β має бути не меншим за `I_C / I_B`. Для малосигнальних приладів β типово 100–200.[^fiore-bjt-basics] Беремо β = 100 як нижню оцінку: `I_C / 100 = 1.02 mA / 100 = 0.0102 mA` (близько 10 мкА). Резистор `R_B = 10 kOhm` дає `I_B = (5 - 0.7) / 10000 = 0.43 mA`, тобто приблизно в 42 рази більше за потрібне; насичення зберігається, поки фактичний β перевищує `1.02 / 0.43 ≈ 2.4`. Якщо взяти `R_B = 470 kOhm`, то `I_B ≈ 0.0091 mA` (9,1 мкА) менше за 10,2 мкА, і при β = 100 транзистор може не насититися, а вихід лишиться вищим за `V_CE,sat`.

Схема інвертує коректно лише тоді, коли вхідна напруга однозначно лежить у зоні низького або високого рівня і база отримує достатній струм. Без `R_B` базовий струм обмежують лише вихідний опір драйвера та перехід база–емітер, тому драйвер може бути перевантажений. Плаваючий вхід дає невизначений стан, бо база не має відомого потенціалу.

**Типові помилки:**

- Вважати, що вихід опускається до 0 В: насичений транзистор дає лише `V_CE,sat`, що зазвичай десяті частки вольта.[^fiore-bjt-dc-load-line]
- Брати β як гарантовану константу: типовий діапазон широкий, тому базовий струм рахують із запасом.[^fiore-bjt-basics]
- Залишати вхід плаваючим: база без визначеного потенціалу дає невизначений вихід.

## Sources

<!-- generated from frontmatter -->
