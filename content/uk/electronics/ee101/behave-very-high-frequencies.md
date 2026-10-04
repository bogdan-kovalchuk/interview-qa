---
id: emb-elee-0061
title: "Як змінюються X_C і X_L на DC та зі зростанням частоти?"
description: "Частотна залежність ідеальних ємнісного та індуктивного реактивних опорів."
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
    applicability: "Походження питання: лекція 41, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-capacitor-reactance
    title: "All About Circuits: AC Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/ac-capacitor-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Частотна залежність ідеального X_C; не доводить, що реальний конденсатор є коротким замиканням на високій частоті."
  - source_id: aac-inductor-reactance
    title: "All About Circuits: AC Inductor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/ac-inductor-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Частотна залежність ідеального X_L; реальна котушка має паразитні параметри."
  - source_id: aac-inductor-quirks
    title: "All About Circuits: Inductor Quirks"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/inductor-quirks/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Втрати й неідеальності реальних котушок на високих частотах; не задає універсальну межу частоти."
---

## Short answer

В ідеальній моделі на DC після перехідного процесу конденсатор має нескінченний `X_C`, а котушка – нульовий `X_L`. Для синусоїдального сигналу `X_C = 1/(2π*f*C)` спадає зі зростанням частоти, тоді як `X_L = 2π*f*L` зростає.[^aac-capacitor-reactance] Реальні компоненти не стають ідеальними коротким замиканням чи розривом: паразитні параметри змінюють поведінку, зокрема поблизу власного резонансу.[^aac-inductor-quirks]

## Detailed explanation

Для ідеальних компонентів ємнісний реактивний опір визначається як `X_C = 1/(2π*f*C)`, а індуктивний – як `X_L = 2π*f*L`. Отже, зі збільшенням частоти `X_C` зменшується, а `X_L` збільшується; це описує синусоїдальний усталений режим, а не довільний сигнал чи реальну деталь на будь-якій частоті.[^aac-capacitor-reactance] [^aac-inductor-reactance]

На нульовій частоті, тобто для усталеного DC, формула ідеального конденсатора дає нескінченний реактивний опір, а формула ідеальної котушки – нульовий. У схемному наближенні це часто називають розривом для конденсатора та коротким замиканням для котушки. Це не описує перехід заряджання конденсатора або наростання струму котушки після перемикання: під час перехідного процесу напруги й струми змінюються.[^aac-capacitor-reactance] [^aac-inductor-reactance]

**Типова помилка:** переносити границі ідеальних формул на фізичні компоненти й вважати, що при дуже великій частоті конденсатор завжди є коротким замиканням, а котушка – розривом. У реальної котушки є опір обмотки, паразитна ємність і втрати; паразитні елементи можуть змінити характер імпедансу після власного резонансу. Тому високочастотну модель обирають за діапазоном частот і документацією конкретної деталі.[^aac-inductor-quirks]

Наприклад, для ідеальної котушки зі сталим `L`, подвоєння частоти подвоює `X_L`; для ідеального конденсатора зі сталим `C` воно вдвічі зменшує `X_C`. Це порівняння працює лише в межах застосовності зосередженої ідеальної моделі.[^aac-capacitor-reactance] [^aac-inductor-reactance]

Пастка проявляється, коли за цими асимптотами вибирають фільтр або пояснюють вимірювання на дуже високій частоті: розрахунок ідеальної реактивності може перестати узгоджуватися з реальною деталлю. Щоб уникнути помилки, відокремлюйте DC-усталений стан від перехідного процесу, а для високих частот перевіряйте паразитні параметри та власну резонансну частоту компонента.[^aac-inductor-quirks]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
