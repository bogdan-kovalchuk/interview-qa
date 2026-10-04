---
id: emb-elee-0072
title: "Яка послідовність фазорного аналізу послідовного RC-кола?"
description: "Яка послідовність фазорного аналізу послідовного RC-кола?"
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
    applicability: "Походження питання: лекція 44, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-series-rc-analysis
    title: "All About Circuits: Series Resistor-Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/series-resistor-capacitor-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтримує обчислення єдиного струму, сумарного комплексного імпедансу та фазорних напруг у послідовному RC-колі."
---

## Short answer

Візьміть фазу джерела за 0° і обчисліть `Z_C = 1/(j*2π*f*C) = -j/(2π*f*C)`, а сумарний імпеданс – `Z = R + Z_C`. Знайдіть струм `I = V_in/Z`, тоді напруги `V_R = I*R` і `V_C = I*Z_C`; перевірте комплексну рівність `V_R + V_C = V_in`.[^aac-series-rc-analysis]

## Detailed explanation

Фазорний аналіз послідовного RC-кола починається з однієї заданої частоти й вибору фазового відліку, зазвичай напруги джерела з кутом 0°. За цієї частоти резистор має імпеданс `Z_R = R`, а конденсатор – `Z_C = 1/(j*2π*f*C) = -j/(2π*f*C)`. У послідовному колі імпеданси додаються як комплексні числа, тому `Z = R + Z_C`; модулі окремих імпедансів додавати не можна.[^aac-series-rc-analysis]

Далі застосуйте AC-форму закону Ома: `I = V_in/Z`. Струм однаковий у послідовних елементах, отже `V_R = I*R`, а `V_C = I*Z_C`. Оскільки множення та ділення виконуються комплексно, полярні подання зручні для знаходження фаз, тоді як прямокутні – для підсумовування. Закон Кірхгофа вимагає, щоб комплексна сума падінь дорівнювала напрузі джерела.[^aac-series-rc-analysis]

**Приклад розрахунку:** для `R = 1 kΩ`, `C = 100 nF`, `f = 1 kHz` і джерела `1 V RMS` реактивний опір становить приблизно `1.592 kΩ`. Сумарний імпеданс – `1000 - j1592 Ω`, його модуль близько `1.880 kΩ`, а струм – приблизно `0.532 mA` з додатною фазою близько 58°. Напруга на резисторі має фазу струму, а напруга конденсатора відстає від нього на 90°; у сумі вони повертають фазор джерела.[^aac-series-rc-analysis]

Модель передбачає лінійні ідеальні елементи та синусоїдальний усталений режим. Паразитний ESR конденсатора, опір джерела й навантаження можуть змінити результат реального кола. Не підміняйте комплексний баланс скалярною сумою модулів: фазова різниця означає, що довжини векторів не складаються арифметично.[^aac-series-rc-analysis]

## Sources

<!-- generated from frontmatter -->
