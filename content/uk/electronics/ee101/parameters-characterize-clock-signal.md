---
id: emb-elee-0243
title: "Які параметри характеризують тактовий сигнал?"
description: "Які параметри характеризують тактовий сигнал?"
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
    applicability: "Походження питання: лекція 78, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-14; курс не є доказом цих тверджень."
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
  - source_id: ti-snaa285
    title: "TI SNAA285: Time-Domain Jitter Measurement Considerations for Low-Noise Oscillators"
    url: https://www.ti.com/lit/an/snaa285/snaa285.pdf
    accessed: 2026-10-14
    kind: official
    version: "SNAA285, October 2015"
    applicability: "Визначення period jitter і cycle-to-cycle jitter за JEDEC JESD65B, рекомендована вибірка 1000–10 000 циклів; вимірювання осцилографом у часовій області, не фазовий шум."
  - source_id: ti-sdaa032
    title: "TI SDAA032: Seamless PWM Duty Cycle Updates Without Intermediate Artifacts"
    url: https://www.ti.com/lit/an/sdaa032/sdaa032.pdf
    accessed: 2026-10-14
    kind: official
    version: null
    applicability: "Формула duty cycle `Duty = 100 × High/(High + Low)` (рівняння 5) у контексті PWM на EPWM TDA4x; сама формула стосується будь-якого сигналу з двома станами."
---

## Short answer

Тактовий сигнал характеризують частота `f`, період `T = 1/f` і частка високого стану `D = t_HIGH/T` (у відсотках `D = 100*t_HIGH/T`; у TI записують `D = 100*High/(High + Low)`).[^ti-sdaa032] Також важливі логічні рівні, час наростання й спадання фронтів і jitter, тобто відхилення тривалості циклу від ідеального періоду.[^ti-snaa285]

## Detailed explanation

Тактовий сигнал описують частотою і часовими параметрами. Частота `f` вимірюється в герцах, а період `T = 1/f` – це час одного повного циклу. Частка високого стану (duty cycle) показує, яку частину періоду сигнал тримає в стані 1: `D = t_HIGH/T`, а у відсотках `D = 100*t_HIGH/T`. У документі TI про PWM це записують як `D = 100*High/(High + Low)`, де сума High і Low дає період.[^ti-sdaa032]

**Приклад:** при `f = 50 МГц` маємо `T = 1/(50*10^6) = 20 нс`. Якщо `t_HIGH = 9 нс`, то `t_LOW = 11 нс` і `D = 100*9/(9 + 11) = 45 %`. Такий сигнал несиметричний, і це важить для схем, які залежать від тривалості високого стану, а не лише від частоти.

Логічні рівні визначають, які напруги наступний вхід сприймає як 1 і як 0. Час наростання й спадання фронтів визначає, скільки часу сигнал проходить між цими рівнями, і від цього залежить, наскільки швидко й чисто схема перемикається.

Jitter – це відхилення від ідеального часу. За JEDEC JESD65B period jitter – це відхилення тривалості циклу від ідеального періоду на випадковій вибірці циклів, а cycle-to-cycle jitter – зміна тривалості між сусідніми циклами.[^ti-snaa285] Period jitter здебільшого використовують для гарантії setup і hold часу логіки в CPU та FPGA. Вимірювати його треба на вибірці з 1000 до 10 000 циклів.[^ti-snaa285]

**Типові помилки:**

- вважати duty cycle 50 % за замовчуванням без перевірки datasheet;
- плутати jitter з похибкою частоти: jitter описує відхилення окремих циклів, а допуск у ppm зсуває всю частоту;
- вимірювати jitter на малій кількості циклів, тоді як для достовірного результату потрібно багато циклів.

## Sources

<!-- generated from frontmatter -->
