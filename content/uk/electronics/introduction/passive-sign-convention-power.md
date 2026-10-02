---
id: emb-elintro-0096
title: "Що таке passive sign convention для потужності?"
description: "Що таке passive sign convention для потужності?"
track: electronics
section: introduction
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
    applicability: "Походження питання: лекція 10, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-passive-power
    title: "Sinusoidal Steady-State Power Calculations"
    url: https://www.allaboutcircuits.com/technical-articles/sinusoidal-steady-state-power-calculations/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пасивна знакова домовленість, миттєва потужність p = v*i та знаки поглинання й віддавання; розгляд усталеного синусоїдального режиму."
---

## Short answer

Якщо струм входить у позитивно позначений вивід елемента, пасивна знакова домовленість задає `p = v*i`.[^aac-passive-power] Додатне значення означає, що елемент поглинає потужність, а від’ємне – що віддає її колу.[^aac-passive-power]

## Detailed explanation

Пасивна знакова домовленість визначає знак потужності через узгоджені напрямки напруги та струму: напрямок струму вважають додатним, коли він входить у вивід із позначкою «+», а напругу відлічують від цього виводу до «−».[^aac-passive-power]

За такого вибору миттєва потужність елемента дорівнює `p = v*i`. Якщо результат додатний, енергія в цей момент надходить до елемента; якщо від’ємний – елемент повертає енергію зовнішньому колу. Це правило не визначає, чи компонент фізично є лише споживачем або лише джерелом: батарея може поглинати потужність під час заряджання, а конденсатор або котушка періодично поглинають і віддають її.[^aac-passive-power]

Знак залежить від обраних опорних напрямків, а не від назви компонента. Якщо стрілку струму спрямовано з позитивного виводу, треба підставити від’ємне значення струму у визначення з пасивною домовленістю або явно змінити знак у формулі. Поширена помилка – назвати будь-яке додатне `v*i` потужністю, яку джерело «виробляє»: за цією домовленістю додатний знак означає поглинання. У балансі потужностей для всієї мережі алгебраїчна сума потужностей дорівнює нулю, якщо враховано всі елементи.[^aac-passive-power]

Приклад: джерело підтримує на навантаженні `v = 5 V`, а струм `i = 0.2 A` входить у його позитивний вивід. Тоді `p = 1 W`, отже навантаження поглинає один ват. Для джерела з тією самою напругою, але струмом, що виходить із позитивного виводу, значення буде `p = -1 W`: джерело віддає один ват.

**Типова помилка:** змінити полярність напруги або напрямок струму в середині обчислення, але залишити попередній знак. Спочатку позначте обидва напрямки на схемі, а потім послідовно використовуйте їх у рівняннях.

## Sources

<!-- generated from frontmatter -->
