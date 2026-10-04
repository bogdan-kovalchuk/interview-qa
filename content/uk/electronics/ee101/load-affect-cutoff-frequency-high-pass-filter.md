---
id: emb-elee-0112
title: "Як навантаження R_L впливає на частоту зрізу RC-ФВЧ?"
description: "Як навантаження R_L впливає на частоту зрізу RC-ФВЧ?"
track: electronics
section: ee101
level: junior
type: pitfall
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
    applicability: "Формула частоти зрізу capacitive high-pass із опором навантаження в простому каскаді; складніший source impedance треба включити в розрахунок."
---

## Short answer

Навантаження `R_L`, підключене паралельно вихідному R, зменшує ефективний опір до `R_eff = R || R_L`, тому частота зрізу `f_c = 1/(2π*R_eff*C)` зростає. Для `R = R_L = 10 kΩ` та `C = 100 nF` вона змінюється приблизно з 159 Hz до 318 Hz.[^aac-high-pass-filters]

## Detailed explanation

Для RC-ФВЧ із послідовним конденсатором та резистором на вихідному вузлі опір, який визначає полюс, залежить від усього кола, підключеного до цього вузла. Якщо джерело ідеальне, його вихідний опір нульовий, а додаткове резистивне навантаження `R_L` стоїть паралельно вихідному R, то `R_eff = R || R_L`. Оскільки паралельне з’єднання не може мати опір більший за жодну гілку, `R_eff` менший за R, а частота зрізу `f_c = 1/(2π*R_eff*C)` вища.[^aac-high-pass-filters]

Це не означає, що будь-який резистор у схемі треба механічно додавати паралельно R. Формула передбачає саме цю топологію, ідеальне джерело та резистивне навантаження. Ненульовий опір джерела, вхідна ємність приладу або наступний каскад можуть вимагати повного аналізу імпедансів. У загальному випадку слід знайти еквівалентний опір, який бачить C після занулення незалежних ідеальних джерел, або прямо вивести передавальну функцію всієї схеми.[^aac-high-pass-filters]

Приклад розрахунку: без навантаження, за `R = 10 kΩ` і `C = 100 nF`, маємо `f_c = 1/(2π*10 kΩ*100 nF) ≈ 159 Hz`. Якщо підключити `R_L = 10 kΩ`, паралельне з’єднання становить `5 kΩ`; тоді `f_c ≈ 318 Hz`. Тобто та сама ємність у навантаженій схемі перестає відповідати попередньому розрахунку частоти зрізу.[^aac-high-pass-filters]

**Типова помилка:** брати тільки номінал резистора, надрукований на схемі фільтра, і ігнорувати вхід наступного пристрою. Це може змінити і частоту зрізу, і коефіцієнт передачі у смузі пропускання. Щоб уникнути цього, вкажіть, між якими вузлами підключено навантаження, врахуйте його вхідний імпеданс і перевірте результат аналізом або вимірюванням усієї зібраної схеми.[^aac-high-pass-filters]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
