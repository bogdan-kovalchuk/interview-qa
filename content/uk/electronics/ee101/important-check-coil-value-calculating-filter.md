---
id: emb-elee-0124
title: "Чому важливо перевірити номінал котушки перед розрахунком RL-фільтра?"
description: "Чому важливо перевірити номінал котушки перед розрахунком RL-фільтра?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Походження питання: лекція 54, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
    accessed: 2026-10-06
    kind: book
    version: "1.1.2, 22 April 2021"
    applicability: "Розділ 1.5: напруга на ідеальній котушці випереджає струм на 90°, реактивний опір `X_L = j*2*pi*f*L`. Розділ 10.3: для RC lead-мережі зріз лежить на 3 dB нижче рівня смуги пропускання, `f_c = 1/(2*pi*R*C)`, фаза виходу +90° на низьких частотах і +45° на критичній. Фільтр RL там окремо не розглянуто: співвідношення для RL тут виведено з тих самих формул дільника напруги."
  - source_id: fontys-passive-hf
    title: "Fontys University of Applied Sciences: 1.2 Passive components at high frequency (LibreTexts)"
    url: https://eng.libretexts.org/Courses/Fontys_University_of_Applied_Sciences/Telecommunications/01:_Passive_Components/1.02:_Passive_components_at_high_frequency
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Еквівалентна схема реальної котушки: ідеальна індуктивність, послідовний опір обмотки `R_s` і паралельна паразитна ємність `C_d`; практична котушка придатна лише нижче власної резонансної частоти (self-resonant frequency), а skin effect підвищує опір обмотки. Загальна модель, а не параметри конкретної котушки курсу."
  - source_id: vishay-inductors-primer
    title: "Vishay: Inductors 101 – Primer Instructional Guide"
    url: https://www.vishay.com/docs/49782/49782.pdf
    accessed: 2026-10-06
    kind: official
    version: "VMN-SG2139-1203"
    applicability: "Визначення DCR, SRF і розподіленої ємності котушки: вище SRF переважає ємнісний реактанс, а менша розподілена ємність за тієї самої індуктивності дає вищу SRF. Числових значень для котушки курсу не дає; їх беруть з datasheet конкретної котушки."
---

## Short answer

Частота зрізу `f_c = R/(2*pi*L)` обернено пропорційна `L`, а мкГн і мГн різняться в 1000 разів, тому помилка в префіксі зсуває розрахунок на три порядки. Наприклад, для `R = 1 kΩ` зріз становить ≈ 482 кГц при 330 мкГн і ≈ 482 Гц при 330 мГн.[^fiore-ac-circuit-analysis]

## Detailed explanation

**Звідки залежність.** Зріз RL-фільтра лежить там, де реактивний опір котушки дорівнює опору `R`: `X_L = 2*pi*f*L = R`.[^fiore-ac-circuit-analysis] Звідси `f_c = R/(2*pi*L)`. Індуктивність стоїть у знаменнику, тому зріз змінюється обернено пропорційно до неї: у 1000 разів більша `L` дає у 1000 разів нижчий зріз за незмінного `R`. Префікси мкГн (`10^-6`) і мГн (`10^-3`) відрізняються саме на тисячу, тож одна переплутана літера в маркуванні, розрахунку чи введенні в калькулятор переносить зріз на три порядки.

**Приклад.** Нехай `R = 1 kΩ`. Для `L = 330 μH` маємо `f_c = 1000/(2*pi*330e-6) ≈ 482 kHz`, а для `L = 330 mH` – `≈ 482 Hz`, тобто рівно в 1000 разів менше. Наслідок для ФНЧ (вихід на резисторі): сигнал `1 kHz` у першому випадку проходить майже без ослаблення (`≈ 0 dB`), а в другому `|V_out/V_in| = 1/sqrt(1 + (1000/482)^2) ≈ 0.43`, тобто `≈ -7.2 dB`. Навіть без помилки в префіксі близькі номінали дають помітну різницю: для `2.2 mH` зріз `≈ 72 kHz`, що в 6.7 раза нижче, ніж для `330 μH`, бо `2200/330 ≈ 6.7`.

**Чого ще не покаже номінал.** Реальна котушка має допуск індуктивності й власний опір обмотки, який додається до `R`.[^fontys-passive-hf] Крім того, котушка придатна лише нижче власної резонансної частоти (SRF).[^fontys-passive-hf] Вище SRF переважає ємнісний реактанс паралельної розподіленої ємності, і котушка поводиться як конденсатор; менша розподілена ємність за тієї самої індуктивності дає вищу SRF.[^vishay-inductors-primer] Тому зріз у сотні кілогерц, як у прикладі на 330 μH, треба зіставити з частотою власного резонансу цієї котушки. Номінал варто звірити з маркуванням і datasheet, а за потреби виміряти LCR-метром, а опір обмотки – омметром, і лише потім рахувати фільтр.

**Типові помилки:**

- Плутати `μH` і `mH` (і `kΩ` та `Ω`) при підстановці в `f_c = R/(2*pi*L)`: результат зсувається на цілі порядки.
- Рахувати за номіналом без допуску й без опору обмотки: реальний зріз відрізняється.
- Не перевіряти розумність результату: зріз у сотні кілогерц для малої котушки або в десятки герц для великої має насторожити.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
