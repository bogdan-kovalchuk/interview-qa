---
id: emb-elee-0134
title: "Стабілізатор: `V_in` = 9 В, `V_Z` ≈ 5,1 В, R = 390 Ом. Які струми та потужності?"
description: "Стабілізатор: `V_in` = 9 В, `V_Z` ≈ 5,1 В, R = 390 Ом. Які струми та потужності?"
track: electronics
section: ee101
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Походження питання: лекція 56, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: nexperia-an90031
    title: "Nexperia AN90031: Zener diodes – physical basics, parameters and application examples"
    url: https://assets.nexperia.com/documents/application-note/AN90031.pdf
    accessed: 2026-10-06
    kind: official
    version: "Rev. 3.0, 7 June 2023"
    applicability: "Поведінка стабілітрона в прямому й зворотному напрямках, ефект Зенера до ≈ 5 В і лавинний пробій вище, зміна знака температурного коефіцієнта S_Z біля 6 В, диференційний опір r_dif, струм вимірювання V_Z, вибір R за формулою R1 = (V_IN - V_Z)/(I_Z(min) + I_LOAD(max)) і розсіювані потужності в простому стабілізаторі; дані наведено для серій Nexperia, інші виробники можуть мати інші числа."
  - source_id: nexperia-bzx84
    title: "Nexperia BZX84 series: voltage regulator diodes (datasheet)"
    url: https://assets.nexperia.com/documents/data-sheet/BZX84_SER.pdf
    accessed: 2026-10-06
    kind: official
    version: "Rev. 7, 1 January 2023"
    applicability: "Параметри BZX84-C5V1: V_Z = 4,8–5,4 В при 5 мА, максимум r_dif 480 Ом при 1 мА і 60 Ом при 5 мА, P_tot ≤ 250 мВт при T_amb ≤ 25 °C; значення для цієї серії, а не для всіх стабілітронів на 5,1 В."
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Конденсаторний фільтр і пульсації (розряд між піками, зростання пульсацій зі струмом навантаження, зарядні піки струму), мостовий випрямляч (у кожному півперіоді провідні два діоди, два падіння V_F), простий стабілітронний стабілізатор і втрата регуляції при надто великому струмі навантаження; книга не наводить формули ΔV = I/(f*C) і не задає V_F конкретного діода."
---

## Short answer

`I_R = (9 - 5.1)/390 = 10 mA`. При навантаженні 5 мА стабілітрону лишається ≈ 5 мА. Без навантаження весь струм іде через стабілітрон: `P_Z = 5.1*0.01 ≈ 51 mW`, а резистор розсіює `P_R = 3.9²/390 ≈ 39 mW`. Усе це для номінальної `V_Z = 5,1 В`: реальна `V_Z` має допуск і залежить від струму.[^nexperia-an90031]

## Detailed explanation

Вихід тримається біля `V_Z = 5.1 V`, тож на резисторі падає `9 - 5.1 = 3.9 V`, а струм через нього `I_R = 3.9/390 = 10 mA`. Цей струм майже не залежить від навантаження, поки стабілітрон у пробої, і він ділиться на частини: `I_Z = I_R - I_load`.[^fiore-rectification]

**Потужності.** Без навантаження `I_Z = 10 mA`, тож `P_Z = 5.1*0.01 = 51 mW` і `P_R = 3.9*0.01 = 39 mW`; разом 90 мВт, що збігається з `9*0.01` від джерела. Це найгірший випадок для стабілітрона: він розсіює найбільше саме без навантаження.[^nexperia-an90031] При навантаженні 5 мА: `I_Z = 5 mA`, `P_Z = 5.1*0.005 = 25.5 mW`, навантаження отримує стільки ж, а резистор і далі розсіює 39 мВт, бо `I_R` не змінився. Навантаження 10 мА забрало б увесь струм R: стабілітрон закрився б, регуляція зникла б, а R і навантаження утворили б дільник.[^fiore-rectification]

**Допуски й режим стабілітрона.** «5.1 В» – номінал. Для BZX84-C5V1 Nexperia дає `V_Z = 4.8–5.4 V` при 5 мА, тож `I_R` лежить у межах від `(9 - 5.4)/390 = 9.2 mA` до `(9 - 4.8)/390 = 10.8 mA`.[^nexperia-bzx84] Отже, при навантаженні 5 мА стабілітрону може лишитися лише ≈ 4,2 мА, тобто менше за струм вимірювання `V_Z`. Це важливо, бо максимальний диференційний опір цієї серії 60 Ом при 5 мА, а при 1 мА вже 480 Ом.[^nexperia-bzx84] Зміна `V_in` проходить на вихід приблизно як дільник `r_dif/(R + r_dif)`: `60/(390 + 60) ≈ 0.13` при 5 мА (зміна `V_in` на 1 В дає ≈ 0,13 В на виході) і `480/(390 + 480) ≈ 0.55` при 1 мА.

**Потужність компонентів і коротке замикання.** 51 мВт на стабілітроні – це далеко від 250 мВт, які BZX84 допускає при 25 °C,[^nexperia-bzx84] а 39 мВт на резисторі – мало. Але при короткому замиканні виходу стабілітрон знеструмлений, а на резисторі падає все `V_in`: `P_R = 9²/390 ≈ 208 mW` (≈ 83 % від 0,25 Вт), тож для надійності резистор беруть із запасом.

**Типові помилки:**

- Рахувати `I_R = V_in/R = 9/390 ≈ 23 mA`, забуваючи відняти `V_Z`.
- Рахувати `P_Z` як `V_in*I` замість `V_Z*I_Z`.
- Вважати 5,1 В точним значенням і ігнорувати допуск та `r_dif`.
- Додавати навантаження 5 мА й вважати, що запас стабілітрона достатній.

## Sources

<!-- generated from frontmatter -->
