---
id: emb-elee-0223
title: "Чим джерело (стабілізатор) струму відрізняється від джерела напруги?"
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
  - source_id: fiore-source-conversions
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 6.2 Source Conversions"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/06:_Analysis_Theorems_and_Techniques/6.2:_Source_Conversions
---

## Short answer

Джерело напруги підтримує `V_out` при зміні струму навантаження – у межах доступного струму.[^fiore-source-conversions] Джерело струму підтримує `I_load` при зміні падіння напруги на навантаженні – у межах доступної напруги.[^fiore-source-conversions]

## Detailed explanation

Ідеальне джерело напруги видає задану напругу незалежно від того, що до нього під’єднано, тож струм визначається навантаженням за законом Ома. Ідеальне джерело струму, навпаки, завжди видає той самий струм незалежно від навантаження, а напругу на навантаженні визначає сам ланцюг.[^fiore-source-conversions] Звідси різниця: при зміні опору навантаження джерело напруги змінює струм, а джерело струму змінює напругу.

Приклад. Джерело напруги 5 В: при навантаженні 100 Ом струм 5/100 = 50 мА, при 1 кОм – 5/1000 = 5 мА, а напруга лишається 5 В. Джерело струму 10 мА: при 100 Ом напруга 10 мА·100 Ом = 1 В, при 1 кОм – 10 мА·1000 Ом = 10 В, а струм лишається 10 мА. Тут видно межу: щоб утримати 10 мА на 1 кОм, джерело має видати 10 В, тож при живленні 9 В стабільний струм утримати не вдасться.

Реальні джерела описують внутрішнім опором. Для джерела напруги він включений послідовно й обмежує струм, ідеально це 0 Ом; для джерела струму він включений паралельно й обмежує напругу, ідеально це нескінченність.[^fiore-source-conversions] Тому розімкнений вихід джерела струму не є безпечним станом: за законом Ома напруга зростає до тисяч або мільйонів вольт, бо її визначає опір повітря між виводами.[^fiore-source-conversions]

**Типові помилки:**

- Вважати джерело струму таким, що тримає струм за будь-якої напруги: межа напруги визначає, коли стабілізація зникає.
- Залишати вихід джерела струму розімкненим: напруга зростає до небезпечних значень.
- Замикати вихід джерела напруги без розрахунку струму: струм дорівнює E/R, де R – внутрішній опір джерела.
