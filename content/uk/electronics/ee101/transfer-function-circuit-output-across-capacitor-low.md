---
id: emb-elee-0073
title: "Яка передавальна функція RC-кола з виходом на конденсаторі і чому це ФНЧ?"
description: "Яка передавальна функція RC-кола з виходом на конденсаторі і чому це ФНЧ?"
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
  - source_id: aac-rc-lowpass
    title: "All About Circuits: Low-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/low-pass-filters/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтримує поведінку RC low-pass, частоту зрізу та застереження щодо впливу опору навантаження."
---

## Short answer

Для ідеального ненавантаженого RC-кола з виходом на конденсаторі передавальна функція `H_C = V_C/V_in = 1/(1 + j*2π*f*R*C)`. Із частотою імпеданс конденсатора зменшується, тому більша частина сигналу падає на резистор і вихід слабшає; частота зрізу `f_c = 1/(2π*R*C)` відповідає модулю передавання `1/sqrt(2)`.[^aac-rc-lowpass]

## Detailed explanation

У послідовному RC-колі вихід знімають із конденсатора, підключеного від вихідного вузла до землі. Використовуючи `Z_C = 1/(j*2π*f*C)` і подільник комплексних імпедансів, маємо `H_C = V_C/V_in = Z_C/(R + Z_C) = 1/(1 + j*2π*f*R*C)`. Це співвідношення припускає ідеальні компоненти, нульовий опір джерела та відсутність навантаження, яке змінює вихідний вузол.[^aac-rc-lowpass]

На низьких частотах `|Z_C|` значно перевищує `R`, тож більша частина вхідної напруги з’являється на конденсаторі. На високих частотах `|Z_C|` стає малою, вихідний вузол сильніше шунтується на землю, і напруга на конденсаторі зменшується. Саме тому коло пропускає низькочастотну складову краще за високочастотну. Частота зрізу `f_c = 1/(2π*R*C)` – це точка, де модуль передавання дорівнює приблизно 0.707, а фаза виходу дорівнює −45° відносно входу.[^aac-rc-lowpass]

**Приклад:** для `R = 1 kΩ` і `C = 100 nF` отримуємо `f_c ≈ 1.592 kHz`. На цій частоті реактивний опір конденсатора за модулем приблизно дорівнює `1 kΩ`, тому модулі резистивного й ємнісного падінь однакові, але їхні фази різняться. Вище цієї частоти вихідна амплітуда спадає; для ідеальної мережі першого порядку спад у далекій смузі затримання наближається до 20 dB на декаду.[^aac-rc-lowpass]

Реальне навантаження має значення: вхідний опір наступного каскаду паралельно конденсатору змінює передавальну функцію й може зсунути частоту зрізу. Так само опір джерела додається до послідовного опору. Перед застосуванням формули перевірте, чи відповідає схема припущенню ненавантаженого RC-кола.[^aac-rc-lowpass]

## Sources

<!-- generated from frontmatter -->
