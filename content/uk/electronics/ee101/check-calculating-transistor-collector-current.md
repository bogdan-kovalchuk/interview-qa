---
id: emb-elee-0196
title: "Що перевірити після обчислення колекторного струму транзистора?"
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
  - source_id: fiore-bjt-ebers-moll
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.5 Ebers-Moll Model"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.5:_Ebers-Moll_Model
  - source_id: fiore-bjt-datasheet
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.4 BJT Data Sheet Interpretation"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.4:_BJT_Data_Sheet_Interpretation
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
---

## Short answer

Перевірте режим: для активної роботи NPN має бути `V_C` > `V_B` > `V_E`.[^fiore-bjt-ebers-moll] Потім порівняйте розсіювану потужність `P` ≈ `V_CE`*`I_C` з паспортною межею та граничними значеннями `I_C` і `V_CE`. Симуляція з моделлю конкретного транзистора показує відхилення від ідеального розрахунку. β залежить від струму й температури, а `V_CE(sat)` від струму.[^fiore-bjt-datasheet]

## Detailed explanation

Обчислений `I_C` має сенс лише тоді, коли транзистор справді працює в режимі, для якого записано `I_C` = β*`I_B`. Для правильного зміщення NPN колекторно-базовий перехід має бути зворотно зміщений, а базово-емітерний – прямо, тобто `V_C` > `V_B` > `V_E`.[^fiore-bjt-ebers-moll] При прямо зміщеному переході `V_BE` ≈ 0,7 В для кремнію, `I_E` = `I_C` + `I_B`, і коли `I_C` значно більший за `I_B`, `I_E` ≈ `I_C`.[^fiore-bjt-basics] Перша перевірка – напруги у вузлах. Якщо `V_C` опустився нижче за `V_B`, колекторний перехід стає прямо зміщеним, транзистор у насиченні, і `I_C` визначає коло, а не β*`I_B`.[^fiore-bjt-dc-load-line]

Друга перевірка – потужність. Транзистор розсіює `P` ≈ `V_CE`*`I_C`, бо доданок `V_BE`*`I_B` малий, коли `I_C` значно більший за `I_B`.[^fiore-bjt-basics] Приклад: `V_CE` = 10 В і `I_C` = 100 мА дають `P` = 1 Вт. Кожне значення окремо лежить у межах паспорта 2N3904, який розбирає підручник (`I_C` до 200 мА, `V_CE` до 40 В), але 1 Вт перевищує його граничні 625 мВт при 25 °C у вільному повітрі. Підручник прямо каже, що прилад не витримує максимальних струму й напруги одночасно.[^fiore-bjt-datasheet]

Третя перевірка – параметри з даташита. β не є сталим: у прикладі підручника нормована β при 0,2 мА падає до 0,7 від значення при 10 мА, тож β з таблиці за іншого струму може дати похибку. Граничне `V_CE(sat)` теж беруть із графіка для потрібного струму, а не з оцінки.[^fiore-bjt-datasheet]

Четверта перевірка – симуляція з моделлю конкретного транзистора. Ідеалізація `V_CE` = 0 у розрахунку насичення завищує граничний струм `V_CC`/`R_C`: реальне `V_CE(sat)` для малосигнальних приладів близько десятої вольта, тож фактичний струм трохи менший.[^fiore-bjt-dc-load-line]

**Типові помилки:**

- Перевіряти лише `I_C` і не дивитися на напруги у вузлах та режим.
- Вважати, що якщо `I_C` і `V_CE` окремо в межах, то `P` теж у межах.
- Брати `V_CE(sat)` = 0 або β з каталогу без поправки на струм і температуру.[^fiore-bjt-datasheet]
