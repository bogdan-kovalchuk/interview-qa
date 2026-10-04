---
id: emb-elee-0117
title: "Чому реальний RL-ФНЧ послаблює сигнал навіть на DC?"
description: "Чому реальний RL-ФНЧ послаблює сигнал навіть на DC?"
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
    applicability: "Послідовний опір обмотки, фактичне низькочастотне передавання, навантаження та визначення зрізу відносно рівня смуги пропускання."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

Опір обмотки `r_L` послідовно з R зменшує передавання навіть на DC: `H(0) = R/(R + r_L)`. За R = 100 Ω і `r_L` = 20 Ω коефіцієнт дорівнює `100/120 ≈ 0.833`. Для цієї моделі полюс розташований на `f_p = (R + r_L)/(2π*L)`, а частоту зрізу на 3 dB визначають відносно фактичного низькочастотного рівня.[^aac-low-pass-filters]

## Detailed explanation

Реальний RL-ФНЧ із виходом на опорі R має опір обмотки котушки `r_L`, послідовно з’єднаний із її індуктивністю та навантаженням. На DC ідеальна індуктивність є коротким замиканням, але мідний провід обмотки лишається резистивним. Тому утворюється дільник R та `r_L`, і вихід нижчий за вхід навіть після завершення перехідного процесу.[^aac-low-pass-filters]

Для ідеального джерела й резистивного навантаження передавальна функція дорівнює `H(jω) = R/(R + r_L + jωL)`. На нульовій частоті її модуль `R/(R + r_L)`. Отже, частотну характеристику не можна трактувати як таку, що починається з одиничного підсилення: рівень смуги пропускання нижчий. Частота полюса цієї моделі дорівнює `(R + r_L)/(2π*L)`. Якщо зріз визначено за спадом на 3 dB від низькочастотного рівня, саме ця частота відповідає межі; вимірювання від вхідного рівня дало б інше значення через втрати.[^aac-low-pass-filters]

Приклад розрахунку:

```text
R = 100 Ω
r_L = 20 Ω
|H(0)| = R/(R + r_L) = 100/120 ≈ 0.833
```

Типова помилка – виміряти вихід лише далеко нижче полюса, побачити постійне заниження і назвати його частотною втратою котушки. Це резистивне ділення напруги, яке існує і на DC; частотна складова реактивного опору додає спад зі зростанням частоти. Щоб перевірити модель, виміряйте вхід і вихід на дуже низькій частоті, оцініть опір обмотки мультиметром при знеструмленій схемі, а потім порівнюйте спад на 3 dB саме з низькочастотним рівнем. Під’єднаний прилад або наступний каскад також навантажує вихід, тому для точної оцінки включіть його в еквівалентне коло.[^aac-low-pass-filters]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
