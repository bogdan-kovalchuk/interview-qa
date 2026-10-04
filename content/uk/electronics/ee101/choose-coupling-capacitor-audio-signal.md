---
id: emb-elee-0022
title: "Як вибрати ємність розділового конденсатора для аудіосигналу (20 Гц–20 кГц) при R = 10 кОм?"
description: "Як вибрати ємність розділового конденсатора для аудіосигналу (20 Гц–20 кГц) при R = 10 кОм?"
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
    applicability: "Походження питання: лекція 35, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-capacitor-highpass
    title: "All About Circuits: High-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/high-pass-filters/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Формула та амплітудна характеристика RC high-pass; для заданого граничного загасання треба обрати бажану частоту зрізу."
---

## Short answer

Для заданої межі загасання оберіть частоту зрізу RC high-pass нижче 20 Hz і розрахуйте `C = 1/(2*π*R*f_c)`. Якщо припустити `R = 10 kΩ` і `f_c = 2 Hz`, отримаємо `C ≈ 8.0 µF`; стандартний номінал 8.2 µF дає близьке значення.[^aac-capacitor-highpass]

## Detailed explanation

Ємність coupling capacitor для аудіо визначають із бажаної нижньої частоти зрізу, а не лише з повної смуги 20 Hz–20 kHz. У найпростішій RC-моделі capacitor послідовно з навантаженням утворює high-pass filter: його опір для низьких частот більший, тому саме нижній край смуги задає вимогу до ємності. Частота зрізу – це точка приблизно −3 dB для простого фільтра першого порядку, а не частота, нижче якої сигнал раптово зникає.[^aac-capacitor-highpass]

Для цієї моделі застосовують `f_c = 1/(2*π*R*C)`, звідки `C = 1/(2*π*R*f_c)`. Якщо вибрати `f_c = 2 Hz` при `R = 10 kΩ`, розрахунок дає близько `7.96 µF`, тобто номінал `8.2 µF` є практичним наближенням. На 20 Hz такий простий фільтр має частоту вдесятеро вище зрізу, тому його загасання невелике, але не нульове. Для іншої цільової характеристики потрібно вибрати інше `f_c` та перерахувати ємність.[^aac-capacitor-highpass]

Ключове обмеження – значення `R`. Це має бути ефективний опір, який бачить capacitor, а не автоматично будь-який резистор у схемі. У підсилювачі на нього можуть впливати вихідний опір джерела й вхідний опір наступного каскаду; якщо структура має декілька coupling capacitor, їхні фільтрувальні ефекти можуть сумарно підняти нижню межу. Також слід врахувати допуск ємності та, для деяких ceramic capacitor, зменшення ефективної ємності від DC bias.[^aac-capacitor-highpass]

**Типова помилка:** називати `8 µF` єдино правильною відповіддю без зазначення критерію. Це результат лише за `R = 10 kΩ` та вибраного `f_c = 2 Hz`; задані у питанні 20 Hz–20 kHz описують аудіосмугу, але самі по собі не встановлюють допустиме загасання на 20 Hz.

## Sources

<!-- generated from frontmatter -->
