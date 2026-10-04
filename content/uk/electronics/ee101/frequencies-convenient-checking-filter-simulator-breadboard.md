---
id: emb-elee-0086
title: "Які частоти зручно вибрати для перевірки RL-фільтра в симуляторі та на макеті?"
description: "Які частоти зручно вибрати для перевірки RL-фільтра в симуляторі та на макеті?"
track: electronics
section: ee101
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Походження питання: лекція 46, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
---

## Short answer

Перевірте RL-фільтр на частотах `0.1*f_c`, `f_c` і `10*f_c`; на кожній виміряйте `V_in`, `V_out`, відношення амплітуд і фазу.[^aac-alternating-current] Реальна котушка має опір обмотки, тож результат відрізнятиметься від ідеальної моделі.[^aac-alternating-current]

## Detailed explanation

Частота зрізу `f_c` визначається номіналами R і L; для послідовного RL-кола вона відповідає точці, де модулі резистивного й індуктивного опорів рівні. Вихідна напруга залежить від того, з якого елемента її знімають, тому перед вимірюванням уточніть схему та вихідний вузол.[^aac-alternating-current]

Точки `0.1*f_c`, `f_c` і `10*f_c` лежать нижче зрізу, біля нього й вище. Вони швидко показують, чи змінюється передавання сигналу в очікуваному напрямку. Для фільтра першого порядку амплітуда на зрізі відносно граничного рівня дорівнює приблизно `1/sqrt(2)`, тобто 0.707 або −3 dB; біля цієї області змінюється також фаза.[^aac-alternating-current]

У симуляторі задайте AC sweep або окремі синусоїдальні сигнали. На макетці перевірте реальні номінали, опір обмотки та навантаження вимірювального приладу: вони змінюють характеристику порівняно з ідеальним розрахунком. Сама трійка частот не є універсальним набором герц, а масштабується відносно власного `f_c` схеми.[^aac-alternating-current]

**Типові помилки:**
- Підставляти довільні частоти, не розрахувавши `f_c`.
- Ігнорувати опір котушки та навантаження виходу.

Наприклад, за `R = 1 kΩ` і `L = 100 mH`, `f_c = R/(2*pi*L)`, приблизно 1.59 kHz. Тоді перевіряють близько 159 Hz, 1.59 kHz і 15.9 kHz, якщо генератор і компоненти працюють у цьому діапазоні.[^aac-alternating-current]

## Sources

<!-- generated from frontmatter -->
