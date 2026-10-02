---
id: emb-elintro-0050
title: "Чому вольтметр повинен мати дуже великий внутрішній опір?"
description: "Чому вольтметр повинен мати дуже великий внутрішній опір?"
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

Вольтметр має високий вхідний опір, щоб брати мало струму й менше навантажувати коло. Значення близько `10 MΩ` є поширеним прикладом для цифрового мультиметра, але не універсальною характеристикою; похибка залежить від опору вимірюваної ділянки.[^aac-voltmeter-loading]

## Detailed explanation

Вольтметр підключають паралельно, а його великий вхідний опір потрібен для зменшення струму, який відбирається від досліджуваної схеми. Ідеальний прилад мав би нескінченний опір і не впливав би на напругу; реальний має скінченний опір, тому утворює додаткову паралельну гілку. Це називають навантаженням вимірювання.[^aac-voltmeter-loading]

Важливе не абстрактно «велике» число, а співвідношення між опором приладу та опором джерела або ділянки, на якій вимірюють напругу. Вхід `10 MΩ` майже не вплине на низькоомне коло, але може помітно змінити дільник, побудований із опорів у мегаомах. Тому навіть справний мультиметр іноді показує напругу, відмінну від напруги ненавантаженого вузла: під час вимірювання саме він стає частиною кола.[^aac-voltmeter-loading]

**Приклад:** дільник із двох резисторів `10 MΩ` має вихідний опір у кілька мегаомів. Підключений паралельно до виходу вольтметр `10 MΩ` уже не є набагато більшим за цей опір і відчутно змінює співвідношення дільника. Натомість на резисторі `10 kΩ` той самий вольтметр має значно менший вплив. Щоб оцінити ефект, можна замінити вихідну ділянку її еквівалентним опором і розглянути паралельне з’єднання з опором входу приладу.[^aac-voltmeter-loading]

Значення вхідного опору перевіряють у специфікації мультиметра для обраного режиму й діапазону: воно не обов’язково однакове для всіх функцій. Вимірювання високого імпедансу також може залежати від витоків, забруднення плати й довгих проводів. Отже, великий опір зменшує похибку навантаження, але не гарантує нульової похибки чи того, що будь-який прилад підійде до будь-якого кола.[^aac-voltmeter-loading]

## Sources

<!-- generated from frontmatter -->
