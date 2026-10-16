---
id: emb-elee-0183
title: "Яка ємність потрібна, щоб імпульс навантаження 100 мА тривалістю 1 мс спричинив просідання не більше 0,1 В?"
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
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
  - source_id: ti-switching-regulator-fundamentals
    title: "Texas Instruments: Switching regulator fundamentals"
    url: https://www.ti.com/lit/an/snva559c/snva559c.pdf
---

## Short answer

Без ESR з `i = C*dv/dt` випливає `C = I*t/V`: 0,1 А × 1 мс / 0,1 В = 1000 мкФ.[^fiore-ac-circuit-analysis] Якщо ж ESR дорівнює 0,2 Ом, миттєвий стрибок `I*ESR = 20 мВ` займає частину допуску, і потрібно щонайменше 1250 мкФ.

## Detailed explanation

Розрахунок починається з рівняння конденсатора `i = C*dv/dt`: напруга змінюється зі швидкістю `i/C`.[^fiore-ac-circuit-analysis] Якщо струм навантаження I сталий протягом імпульсу тривалістю t, спад напруги лінійний і дорівнює `dV = I*t/C`, звідси `C = I*t/dV`. Для 100 мА і 1 мс без урахування ESR: `C = 0,1 А * 0,001 с / 0,1 В = 0,001 Ф = 1000 мкФ`. Це консервативна оцінка, бо вона припускає, що джерело під час імпульсу не віддає жодного струму.

Реальний конденсатор має послідовний опір ESR, через який тече той самий струм.[^ti-switching-regulator-fundamentals] Стрибок `I*ESR` не залежить від ємності і з’являється одразу на початку імпульсу. Для ESR 0,2 Ом він становить `0,1 А * 0,2 Ом = 0,02 В = 20 мВ`. Допуск 0,1 В тоді ділиться так: 20 мВ на ESR і 80 мВ на спад ємності, тому `C = 0,1 А * 0,001 с / 0,08 В = 0,00125 Ф = 1250 мкФ`. Перевірка: спад від ємності `0,1 * 0,001 / 0,00125 = 0,08 В`, плюс 0,02 В на ESR, разом 0,1 В.

Межі застосування. ESR сильно залежить від температури: для типового алюмінієвого електроліту він може зрости приблизно в 40 разів при падінні температури від 25 °C до −40 °C.[^ti-switching-regulator-fundamentals] Тому на холоді стрибок на ESR і спад можуть бути значно більшими, ніж у розрахунку при кімнатній температурі. Якщо ж регулятор із достатньою смугою частот частину струму під час імпульсу віддає сам, потрібна менша ємність; формула дає запас на найгірший випадок.

**Типові помилки:**

- Ігнорувати ESR і вважати, що весь допуск напруги доступний спаду на ємності.
- Брати ESR без урахування температури, хоча на холоді він може зрости багаторазово.
- Сприймати формулу як точний розрахунок для будь-якої схеми: регулятор і джерело під час імпульсу можуть віддавати струм, і тоді потрібна менша ємність.
