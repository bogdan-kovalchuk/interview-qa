---
id: emb-elintro-0046
title: "Як підключається вольтметр – паралельно чи послідовно і чому?"
description: "Як підключається вольтметр – паралельно чи послідовно і чому?"
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
    applicability: "Походження питання: лекція 6, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-voltmeter-loading
    title: 'All About Circuits: Voltmeter Impact on Measured Circuit'
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-8/voltmeter-impact-measured-circuit/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: 'Паралельне підключення, скінченний вхідний опір і навантаження вимірюваного кола; 10 MΩ наведено як поширений приклад, а не універсальну характеристику.'
---

## Short answer

Вольтметр підключають паралельно до ділянки, напругу на якій вимірюють. Його вхідний опір має бути значно більшим за опір цієї ділянки, щоб струм приладу мало змінював режим кола; реальний вплив залежить від обох опорів.[^aac-voltmeter-loading]

## Detailed explanation

Вольтметр вимірює різницю потенціалів між двома точками, тому його щупи ставлять на кінці досліджуваного елемента – тобто паралельно до нього. У паралельному з’єднанні напруга на приладі дорівнює напрузі на елементі. Ідеальний вольтметр мав би нескінченний вхідний опір і не забирав би струму, але реальний має скінченний опір, тому утворює додаткову гілку й трохи навантажує коло.[^aac-voltmeter-loading]

Наскільки помітним буде вплив, визначає співвідношення опорів, а не лише номінал приладу. Наприклад, цифровий мультиметр із входом близько `10 MΩ` мало змінить напругу на резисторі `10 kΩ`, але може суттєво спотворити вимірювання у дільнику з резисторами порядку мегаомів. Тому характеристику входу перевіряють у документації приладу, особливо для високого імпедансу або спеціального режиму вимірювання.[^aac-voltmeter-loading]

Підключення послідовно не є правильним способом виміряти напругу. Через великий послідовний опір вольтметра струм кола різко зменшиться; у деяких колах прилад може майже зупинити струм, але це не універсально «розриває» будь-яке коло. Амперметр, навпаки, вмикають послідовно, бо він вимірює струм гілки.

**Приклад:** для вихідної ділянки дільника `10 kΩ` паралельний вхід `10 MΩ` дає ефективний опір близько `9.99 kΩ`, тож зміна мала. Якщо ділянка сама має `10 MΩ`, той самий прилад уже істотно шунтує її. Отже, правило «паралельно» відповідає топології вимірювання, а правило «високий опір» зменшує похибку навантаження.

## Sources

<!-- generated from frontmatter -->
