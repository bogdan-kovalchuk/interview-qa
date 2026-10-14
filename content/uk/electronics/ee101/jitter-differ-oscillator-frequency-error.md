---
id: emb-elee-0246
title: "Чим jitter відрізняється від похибки частоти генератора?"
description: "Чим jitter відрізняється від похибки частоти генератора?"
track: electronics
section: ee101
level: junior
type: pitfall
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
  - source_id: abracon-quartz-glossary
    title: "Abracon: Quartz Crystal Oscillators Glossary of Terms (глосарій кварцових генераторів)"
    url: https://abracon.com/Support/qtzcryoscil_glossary.pdf
    accessed: 2026-10-14
    kind: official
    version: null
    applicability: "Визначення термінів для кварцових генераторів: частотна похибка в ppm при 25 °C, стабільність у діапазоні температур, вихідна логіка, вивід tristate enable і jitter. Опис одного виробника, а не загальна норма для всіх модулів."
  - source_id: ti-snaa285
    title: "TI SNAA285: Time-Domain Jitter Measurement Considerations for Low-Noise Oscillators"
    url: https://www.ti.com/lit/an/snaa285/snaa285.pdf
    accessed: 2026-10-14
    kind: official
    version: "SNAA285, October 2015"
    applicability: "Визначення period jitter і cycle-to-cycle jitter за JEDEC JESD65B, рекомендована кількість циклів для вимірювання та приклад із 62 пс і –65 пс. Не визначає похибку середньої частоти в ppm."
---

## Short answer

Похибка частоти – відхилення від номінальної частоти при кімнатній температурі, яке задають у ppm (наприклад, ±50 ppm).[^abracon-quartz-glossary] Jitter – відхилення тривалості окремих періодів від ідеального значення, які змінюються від циклу до циклу.[^ti-snaa285]

## Detailed explanation

Похибка частоти і jitter описують різні властивості. Похибка частоти – це зсув середньої частоти від номіналу. Виробники задають її в ppm, тобто в мільйонних частках номіналу, а визначення Abracon стосується відхилення при кімнатній температурі (25 ± 5 °C).[^abracon-quartz-glossary] Приклад: для генератора 8 МГц з допуском ±50 ppm `8*10^6 * 50*10^-6 = 400 Гц`, тож середня частота лежить між 7 999 600 Гц і 8 000 400 Гц.

Той самий зсув можна виразити через період. Період номінального генератора 8 МГц дорівнює 125 нс. При +50 ppm період стає близько 124,99375 нс, тобто коротший приблизно на 6,25 пс у кожному циклі. Це систематична величина: вона однакова для кожного періоду, тому різниця між сусідніми періодами дорівнює нулю.

Jitter описує інше. За TI, period jitter – це відхилення тривалості циклу від ідеального періоду, а cycle-to-cycle jitter – зміна тривалості між сусідніми циклами.[^ti-snaa285] Постійний зсув на 6,25 пс не змінює різниці між сусідніми періодами, тому cycle-to-cycle jitter від нього дорівнює нулю. Приклад із джерела: найбільша позитивна зміна +62 пс і найбільша негативна зміна –65 пс дають cycle-to-cycle jitter 65 пс, бо беруть більше з абсолютних значень.[^ti-snaa285]

Jitter вимірюють на достатній вибірці: TI рекомендує від 1000 до 10 000 циклів, щоб результат був надійним.[^ti-snaa285] Похибку частоти, навпаки, перевіряють за середньою частотою, а не за розкидом окремих фронтів.

**Типові помилки:**

- Плутати постійний зсув частоти з jitter: зсув однаковий на кожному періоді, а jitter змінюється від циклу до циклу.
- Оцінювати jitter за кількома циклами; TI рекомендує від 1000 до 10 000.[^ti-snaa285]
- Вважати, що ±50 ppm при 25 °C гарантує таку саму похибку в усьому діапазоні температур; стабільність у діапазоні температур Abracon задає окремо.[^abracon-quartz-glossary]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
