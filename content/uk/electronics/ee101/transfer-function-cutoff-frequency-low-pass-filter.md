---
id: emb-elee-0115
title: "Яка передавальна функція і частота зрізу RL-ФНЧ?"
description: "Яка передавальна функція і частота зрізу RL-ФНЧ?"
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
    applicability: "Походження питання: лекція 52, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-low-pass-filters
    title: "All About Circuits: Low-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/low-pass-filters/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "RL-ФНЧ: топологія, частотна поведінка, реальні втрати та роль навантаження; формули відповіді припускають ідеальне джерело, ідеальні L та R без додаткового навантаження."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

Для послідовного RL-ФНЧ із виходом на R передавальна функція `H(jω) = R/(R + jωL)`, а частота зрізу `f_c = R/(2π*L)`; стала часу `τ = L/R`. За R = 1 kΩ і L = 330 µH маємо `f_c ≈ 482 kHz`. За сталого R подвоєння L зменшує частоту зрізу вдвічі.[^aac-low-pass-filters]

## Detailed explanation

RL-ФНЧ утворюють послідовні індуктивність і опір навантаження, причому вихідну напругу вимірюють на опорі. Імпеданс котушки `jωL` зростає зі збільшенням частоти, тож на низьких частотах більша частина вхідної напруги припадає на R, а на високих – на L. Це дільник напруги з комплексними імпедансами, тому результат залежить і від того, де саме знято вихід.[^aac-low-pass-filters]

Для ідеального джерела та ненавантаженого виходу модуль передавання дорівнює `|H| = R/sqrt(R² + (2π*f*L)²)`. На частоті зрізу реактивний опір L дорівнює R, і вихід має `1/sqrt(2)` від низькочастотного рівня, тобто приблизно 70.7 %. Кутова частота зрізу `ω_c = R/L`; ділення на `2π` переводить її з радіанів за секунду в герци. Стала часу `τ = L/R` описує перехідний процес того самого RL-кола, і `f_c = 1/(2π*τ)`.[^aac-low-pass-filters]

Приклад розрахунку:

```text
R = 1000 Ω
L = 330 µH = 0.000330 H
f_c = R/(2π*L) = 1000/(2π*0.000330) ≈ 482 kHz
```

Це значення передбачає відсутність додаткового навантаження та втрат обмотки. У реальній схемі опір обмотки, вхід наступного каскаду та паразитні параметри змінюють передавання й частоту зрізу; тому номінальну формулу варто застосовувати до еквівалентного кола, а не лише до маркування котушки. Типова помилка – вважати `f_c` сталою тільки для L: вона залежить від ефективного R та L. Якщо R лишається незмінним, збільшення L удвічі зменшує `f_c` удвічі.[^aac-low-pass-filters]

## Sources

<!-- generated from frontmatter -->
