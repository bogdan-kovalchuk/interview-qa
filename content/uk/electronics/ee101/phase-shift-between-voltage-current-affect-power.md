---
id: emb-elee-0053
title: "Як фазовий зсув між напругою і струмом впливає на потужність?"
description: "Як фазовий зсув між напругою і струмом впливає на потужність?"
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
    applicability: "Походження питання: лекція 40, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-ac-power
    title: "All About Circuits: True, Reactive, and Apparent Power"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-11/true-reactive-and-apparent-power/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтверджує формули потужності для однофазного синусоїдального режиму з RMS-значеннями та розрізнення P, Q і S."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

Для однофазного синусоїдального режиму з RMS-значеннями активна потужність `P = V*I*cos(φ)` вимірюється у W, реактивна `Q = V*I*sin(φ)` – у var, а повна `S = V*I` – у VA. Коефіцієнт потужності дорівнює `P/S`; ідеальне чисто реактивне навантаження має нульову середню активну потужність.[^aac-ac-power]

## Detailed explanation

У змінному колі миттєва потужність дорівнює добутку миттєвих напруги й струму, а її середнє за період залежить від фазового кута між синусоїдами. Для однофазного синусоїдального режиму, де `V` та `I` – RMS-значення, активна потужність дорівнює `P = V*I*cos(φ)`. Вона вимірюється у ватах і відповідає середній швидкості передавання енергії до навантаження. [^aac-ac-power]

Повна потужність `S = V*I` вимірюється у вольт-амперах. Реактивна потужність `Q = V*I*sin(φ)` вимірюється у var і описує обмін енергією з реактивними елементами. Для синусоїдального режиму ці величини утворюють співвідношення `S² = P² + Q²`; коефіцієнт потужності `P/S = cos(φ)`. Не слід називати `S` активною потужністю: одна й та сама напруга та струм можуть передавати різну активну потужність за різних фазових кутів. [^aac-ac-power]

У чистому резистивному навантаженні напруга й струм збігаються за фазою, тому `φ = 0°`, `P = S`, а `Q = 0`. В ідеальному індукторі або конденсаторі кут за модулем дорівнює 90°: елемент по черзі приймає енергію від джерела та повертає її, тому середня активна потужність за повний період нульова. Реальні котушки й конденсатори мають втрати, тож не є чисто реактивними. [^aac-ac-power]

**Приклад:** за `V = 120 V`, `I = 2 A` та `φ = 60°` маємо `S = 240 VA`, `P = 120 W`, `Q ≈ 208 var`. Значення є RMS-значеннями для синусоїдального однофазного режиму; підставляння амплітудних значень без відповідного перерахунку дало б неправильний результат.

**Типові помилки:**

- Обчислювати активну потужність як `V*I`, ігноруючи фазовий кут.
- Вважати, що ідеальний реактивний елемент споживає нульовий струм. Він може мати струм і повну потужність, хоча його середня активна потужність дорівнює нулю. [^aac-ac-power]

## Sources

<!-- generated from frontmatter -->
