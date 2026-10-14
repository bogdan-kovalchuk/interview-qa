---
id: emb-elee-0244
title: "Генератор 10 МГц з допуском ±50 ppm і коефіцієнтом заповнення 50%. Які період, тривалість станів і похибка частоти?"
description: "Генератор 10 МГц з допуском ±50 ppm і коефіцієнтом заповнення 50%. Які період, тривалість станів і похибка частоти?"
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
  - source_id: ti-swra372
    title: "TI SWRA372C: AN100 Crystal Selection Guide"
    url: https://www.ti.com/lit/an/swra372c/swra372c.pdf
    accessed: 2026-10-14
    kind: official
    version: "SWRA372C, November 2013"
    applicability: "Загальний допуск кварцового генератора задається в ppm і складається з виробничого, температурного допуску та старіння; відхилення частоти в ppm відповідає такому самому відносному відхиленню. Приклад у документі стосується RF-частоти для радіомодулів TI."
  - source_id: ti-sdaa032
    title: "TI SDAA032: Seamless PWM Duty Cycle Updates Without Intermediate Artifacts"
    url: https://www.ti.com/lit/an/sdaa032/sdaa032.pdf
    accessed: 2026-10-14
    kind: official
    version: null
    applicability: "Формула duty cycle `Duty = 100 × High/(High + Low)` (рівняння 5) у контексті PWM на EPWM TDA4x; сама формула стосується будь-якого сигналу з двома станами."
---

## Short answer

Період `T = 1/f = 100 нс`. При номінальних 50 % високий і низький стани тривають по 50 нс, бо `D = 100*High/(High + Low)`.[^ti-sdaa032] Допуск ±50 ppm задає відносну похибку частоти: `Δf = f*ppm*10^-6 = 10^7*50*10^-6 = ±500 Гц`.[^ti-swra372]

## Detailed explanation

Період – обернена величина частоти: `T = 1/f = 1/(10*10^6 Гц) = 100 нс`. Це номінальне значення. Допуск ±50 ppm описує відносну похибку частоти: ppm – мільйонна частка, тож `50 ppm = 50*10^-6`. Для 10 МГц відхилення дорівнює `10*10^6*50*10^-6 = 500 Гц`, тобто частота може бути в межах від 9,9995 МГц до 10,0005 МГц.[^ti-swra372]

Період залежить від частоти обернено, тому його межі майже симетричні: при 10,0005 МГц `T = 99,995 нс`, а при 9,9995 МГц `T = 100,005 нс`. Отже, період відхиляється приблизно на ±5 пс, а частотна похибка ±500 Гц і зміна періоду – різні величини, які не порівнюються напряму.

Тривалість станів залежить від duty cycle. Якщо він точно 50 %, кожен стан триває `T/2 = 50 нс`. З ppm `T/2` лежить у межах від 49,9975 нс до 50,0025 нс, тобто ±2,5 пс. Важливо: ppm стосується частоти, а не співвідношення станів. Якщо обидва стани масштабуються однаково, `D` не змінюється, тож реальний duty cycle задає окремий параметр datasheet, а не допуск частоти.

**Типові помилки:**

- плутати ppm з відсотками: 50 ppm дорівнює 0,005 %, а не 50 %;
- вважати, що ±500 Гц означає ±500 Гц на період; період змінюється лише на ±5 пс;
- вважати 50 % duty cycle гарантованим для будь-якого генератора.

## Sources

<!-- generated from frontmatter -->
