---
id: emb-elee-0189
title: "Які основні співвідношення струмів BJT і чому I_C = βI_B не завжди виконується?"
description: "Які основні співвідношення струмів BJT і чому I_C = βI_B не завжди виконується?"
track: electronics
section: ee101
level: junior
type: concept
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
    applicability: "Походження питання: лекція 67, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; курс не є доказом цих тверджень."
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
    applicability: "Підручник, розділ 4.2: назви виводів, будова NPN і PNP, напрямок звичайного струму, KCL I_E = I_C + I_B, V_BE ≈ 0,7 В для кремнію, β = I_C/I_B (для малосигнальних транзисторів зазвичай 100–200, для потужних близько 25–50). Ідеалізована модель; номінали конкретних транзисторів можуть відрізнятися."
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: "https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf"
    accessed: 2026-10-13
    kind: book
    version: "Spring 2006"
    applicability: "Лекційні нотатки університетського курсу: умови областей (активний: B–E прямий, B–C зворотний, I_C = β·I_B; насичення: обидва переходи прямі, максимум I_C не залежить від I_B та β), I_C(sat) = (V_CC − V_CE(sat))/R_C, типове V_CE(sat) близько 0,2 В. Не документ виробника; конкретні транзистори можуть відрізнятися."
  - source_id: fiore-bjt-datasheet
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.4 BJT Data Sheet Interpretation"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.4:_BJT_Data_Sheet_Interpretation"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 4.4: даташит 2N3904 – β (h_FE) падає при дуже малих і дуже великих I_C, розкид близько 3:1 при 10 мА, залежність від I_C і температури. Приклад однієї моделі, не загальне правило."
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 4.6: навантажувальна пряма; I_C(sat) = V_CC/R_C – максимум колекторного струму в насиченні; розрахунковий струм вище I_C(sat) дає I_C(sat). Формула V_CC/R_C не враховує V_CE(sat)."
---

## Short answer

`I_E = I_C + I_B`; в активному режимі `I_C = β*I_B`, а `V_BE ≈ 0,7 В` для кремнію, тож `V_B = V_E + V_BE`. Формула не виконується в насиченні: тоді `I_C` обмежує зовнішнє коло, а не `I_B`. Наприклад, при `I_B = 20 мкА` і `β = 100` формула дає 2 мА, але коло з 5 В і 5 кОм допускає лише близько 0,96 мА. Крім того, β залежить від струму й температури, тому це наближення.[^fiore-bjt-basics][^mit-6071-bjt-notes][^fiore-bjt-datasheet]

## Detailed explanation

Струми зв’язані законом Кірхгофа для вузла: `I_E = I_C + I_B`. Через малий базовий струм `I_E ≈ I_C`. Коефіцієнт передачі β = I_C/I_B для малосигнальних транзисторів зазвичай 100–200, а для потужних менший, близько 25–50.[^fiore-bjt-basics]

Співвідношення `I_C = β*I_B` є рівнянням для активного режиму: B–E прямо зміщений, B–C зворотно, і колекторний струм визначається базовим, а не зовнішнім колом.[^mit-6071-bjt-notes] Приклад: при `I_B = 20 мкА` і `β = 100` активний режим дає `I_C = 2 мА`. Щоб цей струм протік через `R_C = 5 кОм`, на резисторі мало б упасти `2 мА · 5 кОм = 10 В`, а джерело дає лише 5 В. Така робоча точка недосяжна.

Транзистор тоді переходить у насичення. Там обидва переходи прямо зміщені, максимум `I_C` не залежить від `I_B` та β і дорівнює `(V_CC − V_CE(sat))/R_C`.[^mit-6071-bjt-notes][^fiore-bjt-dc-load-line] Для `V_CE(sat) ≈ 0,2 В` маємо `(5 − 0,2)/5000 = 0,96 мА`. Тоді `I_C/I_B ≈ 0,96 мА / 20 мкА ≈ 48`, тобто менше за β = 100. Формула `I_C = β*I_B` тут не діє: транзистор не може віддати 2 мА, і його струм визначає `R_C`.

β не є сталою величиною. Для одного типу він залежить від `I_C` і температури та різниться між екземплярами: у даташиті 2N3904 розкид при 10 мА близько 3:1, а при дуже малих і дуже великих струмах β падає.[^fiore-bjt-datasheet] Тому розрахунок на одне номінальне β, наприклад 100, є лише наближенням. У схемі закладають запас або навмисно працюють у насиченні, де β вже не визначає струму.[^mit-6071-bjt-notes]

**Типові помилки:**
- Вважати, що `I_C = β*I_B` виконується завжди, незалежно від `R_C` і `V_CC`: зовнішнє коло обмежує струм колектора.[^fiore-bjt-dc-load-line]
- Брати β з листа як сталу: у даташиті це діапазон, який залежить від струму й температури.[^fiore-bjt-datasheet]
- Вважати, що в насиченні `I_C` росте разом з `I_B`: у насиченні максимум колекторного струму задає коло.[^mit-6071-bjt-notes]

## Sources

<!-- generated from frontmatter -->
