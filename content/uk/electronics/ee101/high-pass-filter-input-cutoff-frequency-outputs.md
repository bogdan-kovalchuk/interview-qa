---
id: emb-elee-0110
title: "RC-ФВЧ: R = 10 kΩ, C = 100 nF, вхід 1 V RMS. Яка частота зрізу і виходи на 15.9 Hz, 159 Hz і 1.59 kHz?"
description: "RC-ФВЧ: R = 10 kΩ, C = 100 nF, вхід 1 V RMS. Яка частота зрізу і виходи на 15.9 Hz, 159 Hz і 1.59 kHz?"
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
    applicability: "Походження питання: лекція 51, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-high-pass-filters
    title: "All About Circuits: High-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/high-pass-filters/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Модель пасивного capacitive high-pass, частота зрізу на рівні -3 dB та залежність виходу від частоти; розрахунок передбачає ідеальне джерело й ненавантажене RC-коло."
---

## Short answer

`f_c` ≈ 159.15 Hz. Для ідеального ненавантаженого RC-ФВЧ виходи становлять приблизно 0.0995 V, 0.707 V і 0.995 V RMS відповідно.[^aac-high-pass-filters]

## Detailed explanation

RC-ФВЧ пропускає сигнал краще зі зростанням частоти, бо послідовний конденсатор має менший модуль імпедансу на вищій частоті. Для ідеального джерела з нульовим вихідним опором, послідовного C і R на спільний провід вихід знімають із R. Передавальна функція має модуль `|H| = 1/sqrt(1 + (f_c/f)^2)`, а частота зрізу дорівнює `f_c = 1/(2π*R*C)`.[^aac-high-pass-filters]

У цій задачі `R*C = 10 kΩ*100 nF = 1 мс`, отже `f_c ≈ 159.15 Hz`. На частоті зрізу модуль передачі становить `1/sqrt(2) ≈ 0.707`, або близько −3 dB. Нижче зрізу напруга швидко зменшується, а значно вище наближається до вхідної. Це частотна характеристика для синусоїди в усталеному режимі; вона не описує форму перехідного процесу сама по собі.[^aac-high-pass-filters]

Приклад розрахунку для вхідних 1 V RMS: на 15.9 Hz відношення `f/f_c` близьке до 0.1, тому вихід приблизно 0.0995 V RMS; на 159 Hz воно близьке до 1 і вихід приблизно 0.707 V RMS; на 1.59 kHz воно близьке до 10 і вихід приблизно 0.995 V RMS. Значення округлені, а номінали компонентів вважаються точними.[^aac-high-pass-filters]

Реальна схема може відхилятися від цих чисел через опір джерела, навантаження виходу, допуски R і C та паразитні параметри. Навантаження, підключене паралельно R, зменшує ефективний опір і змінює частоту зрізу, тому формулу не можна застосовувати, не перевіривши топологію та вимірювальний прилад.[^aac-high-pass-filters]

## Sources

<!-- generated from frontmatter -->
