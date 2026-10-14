---
id: emb-elee-0232
title: "Чи може підсилювач напруги з кілоомними резисторами напряму живити динамік 8 Ом?"
description: "Чи може підсилювач напруги з кілоомними резисторами напряму живити динамік 8 Ом?"
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
    applicability: "Походження питання: лекція 75, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-14; курс не є доказом цих тверджень."
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
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Підручник, розділ 7.3: розділові конденсатори – розімкнення для постійного струму і коротке замикання для сигналу, якщо їх реактивний опір значно менший за сусідні резистори; A_v = -r_C/(r'_e + r_E) має мінус (інверсія, зсув фази на 180°); Z_out ≈ R_C, коли R_C значно менший за r'_C; з навантаженням A_divider = R_L/(R_L + R_C) (приклад 7.1)."
  - source_id: fiore-common-collector-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.4 Common Collector Amplifier"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.4:_Common_Collector_Amplifier"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Підручник, розділ 7.4: емітерний повторювач має підсилення напруги близько одиниці, низький вихідний опір і дає підсилення струму та потужності; призначений для низькоомних навантажень, наприклад динаміків."
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Підручник, розділ 4.6: навантажувальна пряма; I_C(sat) = V_CC/R_C – найбільший колекторний струм; V_CE(cutoff) = V_CC при I_C = 0; у насиченні V_CE(sat) становить десяті частки вольта для малосигнальних приладів."
  - source_id: ti-slaa067
    title: "Texas Instruments: Understanding Basic Analog – Circuit Equations"
    url: https://www.ti.com/lit/pdf/slaa067
    accessed: 2026-10-14
    kind: official
    version: "SLAA067"
    applicability: "Закон Ома V = I·R для резистивного кола (розділ Laws of Physics). Лише закон Ома; розрахунків навантаження динаміка документ не містить."
---

## Short answer

Ні: вихідний опір каскаду з колекторним резистором приблизно дорівнює `R_C`, коли `R_C` значно менший за внутрішній опір транзистора, тож 8-омний динамік утворює з ним дільник і отримує малу частку напруги.[^fiore-common-emitter-amplifier] Для динаміка потрібен каскад з малим вихідним опором, наприклад емітерний повторювач.[^fiore-common-collector-amplifier]

## Detailed explanation

У каскаді зі спільним емітером колекторний резистор `R_C` визначає вихідний опір для змінного сигналу. Зі сторони навантаження транзистор виглядає як джерело струму з дуже великим внутрішнім опором, тому вихід можна розглядати як джерело напруги з послідовним опором, приблизно рівним `R_C`.[^fiore-common-emitter-amplifier] Навантаження `R_L` і `R_C` утворюють дільник, і до навантаження доходить частка `R_L/(R_L + R_C)` напруги холостого ходу.[^fiore-common-emitter-amplifier]

**Приклад:** `R_C = 4,7 кОм`, динамік `R_L = 8 Ом`, напруга холостого ходу на виході 1 В RMS. Частка `8/(4700 + 8) ≈ 0,0017`, тобто на динаміку лишається близько 1,7 мВ, а втрата становить близько 55 дБ. Потужність на 8 Ом з такою напругою дорівнює `(0,0017)^2/8 ≈ 0,36 мкВт`. Щоб на 8 Ом було 1 В RMS, потрібен струм `I = V/R = 0,125 А` (закон Ома[^ti-slaa067]) і потужність `V^2/R = 0,125 Вт`.

Другий бік – струм. Колекторний струм не може бути меншим за нуль: при `I_C = 0` транзистор у відсіканні.[^fiore-bjt-dc-load-line] Тому синус без обрізання не може мати амплітуду струму більшу за струм спокою. При `V_CC = 9 В` і `V_CE ≈ V_CC/2 = 4,5 В` (без резистора в емітері) спокійний струм через `R_C = 4,7 кОм` становить близько 0,96 мА, тож навіть через розділовий конденсатор у динамік піде не більше ≈ 0,96 мА амплітуди. Потужність тоді `(0,96 мА)^2 · 8 Ом / 2 ≈ 3,7 мкВт`, тобто на кілька порядків менше за 0,125 Вт.

Рішення – буферний каскад з малим вихідним опором. Емітерний повторювач має підсилення напруги близько одиниці, низький вихідний опір і підсилення струму, тому його використовують як драйвер низькоомних навантажень, зокрема динаміків.[^fiore-common-collector-amplifier] Для гучності потрібні транзистори, розраховані на струм і розсіювану потужність, а не лише на напругу.

**Типові помилки:**

- Вважати, що на динаміку буде напруга з розрахунку без навантаження: дільник з вихідним опором її зменшує.
- Підключати динамік до колектора без розділового конденсатора: постійна напруга колектора опиниться майже на нулі, і каскад піде в насичення.
- Оцінювати гучність за напругою, не рахуючи струм і потужність на 8 Ом.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
