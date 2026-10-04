---
id: emb-elee-0093
title: "Чи зникає сигнал вище частоти зрізу ФНЧ?"
description: "Чи зникає сигнал вище частоти зрізу ФНЧ?"
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
    applicability: "Походження питання: лекція 48, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-rc-low-pass-transfer
    title: "All About Circuits: Understanding Low-Pass Filter Transfer Functions"
    url: https://www.allaboutcircuits.com/technical-articles/understanding-transfer-functions-for-low-pass-filters/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Частота зрізу як точка −3 dB та асимптотичний спад однополюсного пасивного RC-ФНЧ."
---

## Short answer

Ні. Для однополюсного RC-ФНЧ `f_c` є точкою, де амплітуда падає до `1/sqrt(2)` від смугового рівня, тобто приблизно на `3.01 dB`; це не жорстка межа. Вище зрізу амплітуда продовжує плавно спадати, наближаючись до нахилу `-20 dB` на декаду, тому на `10*f_c` вона близька до однієї десятої смугової амплітуди.[^aac-rc-low-pass-transfer]

## Detailed explanation

Частота зрізу не є перемикачем, який пропускає всі нижчі частоти й повністю відтинає всі вищі. Для однополюсного RC-ФНЧ амплітуда змінюється плавно відповідно до `|H| = 1/sqrt(1 + (f/f_c)^2)`. На самій частоті зрізу вона дорівнює приблизно `0.707` від значення на низьких частотах, що відповідає `-3.01 dB` для амплітудного відношення. Навіть на частотах набагато вищих за зріз вихід залишається ненульовим в ідеальній моделі.[^aac-rc-low-pass-transfer]

Далеко вище `f_c` величина `f/f_c` домінує в знаменнику, тому модуль приблизно дорівнює `f_c/f`. Якщо частота збільшується вдесятеро, амплітуда стає приблизно вдесятеро меншою. У логарифмічному графіку це спад близько `20 dB` на декаду для одного полюса. Наприклад, сигнал на `10*f_c` має амплітуду близько `0.1` від низькочастотної, а не нуль; точне значення становить `1/sqrt(101) ≈ 0.0995`.[^aac-rc-low-pass-transfer]

Реальний сигнал може здаватися зниклим, якщо вихід опустився нижче шуму, роздільної здатності вимірювача або чутності, але це обмеження системи вимірювання чи сприйняття, а не абсолютне відсікання фільтром. Навантаження та додаткові каскади також змінюють характеристику; наведений спад стосується одного полюса без істотного навантаження.[^aac-rc-low-pass-transfer]

**Типові помилки:**
- Трактувати «зріз» як частоту, вище якої вихід дорівнює нулю.
- Плутати спад `20 dB` на декаду з лінійним зменшенням до нуля.
- Не вказувати, що нахил стосується одного полюса та асимптотичної області вище зрізу.

Уникайте цих помилок, оцінюючи `|H|` у конкретній точці та відрізняючи математичну характеристику від порога шуму приладу.[^aac-rc-low-pass-transfer]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
