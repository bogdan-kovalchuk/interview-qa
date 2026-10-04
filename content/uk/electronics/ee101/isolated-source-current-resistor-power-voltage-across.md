---
id: emb-elee-0088
title: "Ізольоване джерело 6 V RMS, R = 1 kΩ, `X_C` = 1 kΩ. Які струм, потужність резистора і напруга на C?"
description: "Ізольоване джерело 6 V RMS, R = 1 kΩ, X_C = 1 kΩ. Які струм, потужність резистора і напруга на C?"
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
    applicability: "Походження питання: лекція 47, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
---

## Short answer

Для послідовного RC-кола, якщо `R = X_C = 1 kΩ`, струм дорівнює `4.24 mA RMS`, а потужність R – `18 mW`.[^aac-alternating-current] Напруга на конденсаторі дорівнює `4.24 V RMS` (приблизно `6 V peak` для синусоїди).[^aac-alternating-current]

## Detailed explanation

В ізольованому послідовному RC-колі резистор і конденсатор ділять напругу джерела як фазори: напруга на R синфазна зі струмом, а напруга на C відстає від струму на 90 градусів.[^aac-alternating-current]

Тому не можна додавати `V_R` та `V_C` як звичайні скалярні величини. Для ідеальних елементів повний імпеданс має модуль `sqrt(R^2 + X_C^2)`, а струм RMS є напругою джерела RMS, поділеною на цей модуль. За заданих `R = 1 kΩ` і `X_C = 1 kΩ` модуль імпедансу приблизно `1.414 kΩ`, отже `I = 6/1414 = 4.24 mA RMS`.[^aac-alternating-current]

Потужність, що перетворюється на тепло в R, дорівнює `I_RMS^2*R`, тобто приблизно `18 mW`. Напруга на конденсаторі за модулем становить `I_RMS*X_C = 4.24 V RMS`. Якщо джерело синусоїдальне, пікове значення цієї напруги дорівнює RMS-значенню, помноженому на `sqrt(2)`, приблизно `6.0 V peak`.[^aac-alternating-current]

Цей розрахунок вважає джерело ідеальним, а R і C – ідеальними елементами із заданим реактивним опором на частоті джерела. Реальні допуски, ESR конденсатора й вихідний опір джерела змінять результат. Ізольоване джерело означає, що його вихід не має заданого зв’язку із землею; це не змінює фазорний розрахунок, але важливо для безпечного вимірювання.[^aac-alternating-current]

**Типова помилка:** складати падіння напруги `4.24 V` на R та `4.24 V` на C арифметично й робити висновок, що джерело має `8.48 V`. Оскільки складові ортогональні за фазою, їхній результуючий модуль дорівнює `sqrt(4.24^2 + 4.24^2)`, тобто приблизно 6 V RMS.[^aac-alternating-current]

## Sources

<!-- generated from frontmatter -->
