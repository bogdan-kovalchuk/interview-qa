---
id: emb-elee-0218
title: "Як побудований транзисторний ключ двигуна в нижньому плечі (low-side)?"
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
  - source_id: fiore-bjt-switching
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.7 BJT Switching and Driver Applications"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.7:_BJT_Switching_and_Driver_Applications
  - source_id: fiore-bjt-collector-curves
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.3 BJT Collector Curves"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.3:_BJT_Collector_Curves
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
---

## Short answer

Емітер NPN – на спільний провід, колектор – до нижнього контакту двигуна, верхній контакт двигуна – до плюса живлення. Базовий резистор обмежує струм керування.[^fiore-bjt-switching]

## Detailed explanation

**Топологія.** Транзистор у нижньому плечі замикає коло «плюс живлення – двигун – колектор – емітер – земля». Так само побудований насичувальний LED-драйвер у Fiore: транзистор замикає коло між джерелом, навантаженням і резистором у колекторі, а емітер іде на землю. Fiore також наводить пряме керування двигуном постійного струму насичувальним BJT-ключем.[^fiore-bjt-switching] Емітер на спільному проводі, тож керувальна напруга відраховується від землі, а двигун отримує повне живлення, коли транзистор відкритий.

**Керування базою.** Логічна напруга `V_in` дає струм бази `I_B = (V_in - V_BE)/R_B`, де `V_BE` для кремнію близько 0,7 В.[^fiore-bjt-basics] Умовний приклад: `V_in = 5 В`, `R_B = 430 Ом`, тоді `I_B = (5 - 0,7)/430 ≈ 10 мА`. Нехай двигун бере `I_C = 100 мА`, а β не менше 100. Тоді `I_C/I_B = 10`, тобто відношення в десять разів менше за β. Такий стан і є насиченням: колекторний струм визначає схема, а не β.[^fiore-bjt-switching]

**Втрати.** У насиченні `V_CE(sat)` становить кілька десятих вольта.[^fiore-bjt-collector-curves] Припустімо `V_CE(sat) = 0,2 В`: розсіювання на транзисторі становить `0,2 В * 0,1 А = 20 мВт`. Якби транзистор працював у лінійній зоні при `V_CE = 6 В` і тому самому струмі, розсіювання було б `0,6 Вт`. Тому ключ працює між двома станами: повністю відкритий або закритий.

**Типові помилки:**

- Занадто малий `R_B`: великий струм бази без потреби навантажує джерело керування.
- Занадто великий `R_B`: `I_B` стає замалим, відношення `I_C/I_B` наближається до β, транзистор не насичується і гріється.[^fiore-bjt-switching]
- Відсутній діод на обмотці двигуна: при вимиканні виникає викид напруги, який може пошкодити транзистор (див. qid:emb-elee-0219).[^fiore-bjt-switching]
