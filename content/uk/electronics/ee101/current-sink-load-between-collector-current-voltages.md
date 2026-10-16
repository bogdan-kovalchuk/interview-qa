---
id: emb-elee-0224
title: "Current sink: `V_B` = 1,7 В, `R_E` = 100 Ом, навантаження 220 Ом між +9 В і колектором. Які струм і напруги?"
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
  - source_id: rohm-bjt-basics
    title: "ROHM: Bipolar Junction Transistor (BJT) Basics: Operation and Applications (NPN & PNP)"
    url: https://techweb.rohm.com/product/transistors-diodes/transistors/27319/
---

## Short answer

`I_E` = (1.7-0.7)/100 = 10 мА при `V_BE` ≈ 0,7 В, а `I_C` ≈ `I_E`.[^fiore-bjt-basics] Падіння на навантаженні ≈ 2,2 В, `V_C` ≈ 6,8 В, `V_E` ≈ 1 В: транзистор в активному режимі.[^mit-6071-bjt-notes]

## Detailed explanation

Схема – current sink на NPN-транзисторі: база має сталу напругу `V_B` = 1,7 В, а струм задає резистор `R_E` в емітері. Напруга на емітері `V_E` = `V_B`-`V_BE`. Для кремнію `V_BE` ≈ 0,7 В,[^fiore-bjt-basics] тож `V_E` ≈ 1,0 В і `I_E` = `V_E`/`R_E` = 1.0/100 = 10 мА. Струм емітера складається з колекторного й базового: `I_E` = `I_C` + `I_B`.[^fiore-bjt-basics] Коли `I_C` значно більший за `I_B`, колекторний струм майже дорівнює емітерному.[^fiore-bjt-basics] При β = 100 маємо α = β/(β+1) ≈ 0,99, тож `I_C` ≈ 9,9 мА, тобто на 1 % менше.[^mit-6071-bjt-notes]

Струм 10 мА тече через навантаження 220 Ом: падіння 220 Ом·0.01 А = 2,2 В, тож `V_C` = 9-2.2 = 6,8 В, а `V_CE` = 6,8-1.0 = 5,8 В. В активній зоні база–емітер пряма, база–колектор зворотна, і `V_BE` < `V_CE` < `V_CC`; тут 0,7 < 5,8 < 9.[^mit-6071-bjt-notes]

Є два обмеження. По-перше, `V_BE` впливає на струм: при `V_BE` = 0,6 В струм становив би (1.7-0.6)/100 = 11 мА, при 0,8 В – (1.7-0.8)/100 = 9 мА. Тобто похибка 0,1 В дає близько 10 % похибки струму. Для активного режиму типове `V_BE` – 0,6–0,7 В.[^rohm-bjt-basics] По-друге, активний режим вимагає, щоб колектор лишався вищим за базу, тобто `V_C` > `V_B`. Для 10 мА це `R_L`·10 мА < 9-1.7 = 7.3 В, отже `R_L` < 730 Ом. Більший опір переводить перехід база–колектор у прямий, і транзистор виходить з активного режиму.[^mit-6071-bjt-notes]

**Типові помилки:**

- Вважати `I_C` = β·`I_B` для current sink без перевірки режиму: у насиченні така залежність нелінійна.
- Ігнорувати залежність струму від `V_BE`: похибка 0,1 В дає близько 10 % похибки струму.
- Брати навантаження більше приблизно 730 Ом: колектор опускається до бази, і current sink перестає тримати 10 мА.
