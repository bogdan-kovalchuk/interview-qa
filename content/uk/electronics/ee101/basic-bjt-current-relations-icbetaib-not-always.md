---
id: emb-elee-0189
title: "Які основні співвідношення струмів BJT і чому I_C = βI_B не завжди виконується?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf
  - source_id: fiore-bjt-datasheet
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.4 BJT Data Sheet Interpretation"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.4:_BJT_Data_Sheet_Interpretation
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
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
