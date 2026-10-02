---
id: emb-elintro-0043
title: "Чому напруга завжди \"відносна\"?"
description: "Чому напруга завжди \"відносна\"?"
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
  - source_id: aac-voltage-current-resistance
    title: "All About Circuits: Ohm’s Law - How Voltage, Current, and Resistance Relate"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/voltage-current-resistance-relate/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює, що напруга визначається між двома точками, та розрізняє опорну точку й абсолютний потенціал."
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
---

## Short answer

Напругу визначають між двома точками, а не відносно абсолютного нуля. У схемі можна вибрати опорну точку `GND` і домовитися вважати її потенціал `0 V`; це вибір відліку, а не твердження, що точка має універсальний нульовий потенціал.[^aac-voltage-current-resistance]

## Detailed explanation

Напруга є різницею електричних потенціалів між двома точками, тому числове значення завжди залежить від вибраної пари. Це схоже на висоту: твердження «точка розташована на висоті 10 m» потребує рівня відліку, тоді як різниця висот між двома точками може бути визначена без абсолютного нуля. Так само вимірювання напруги мультиметром порівнює потенціали двох щупів.[^aac-voltage-current-resistance]

У схемному аналізі одну точку часто призначають опорною і позначають `GND`; її потенціал за домовленістю записують як `0 V`. Після такого вибору напруга вузла означає різницю між ним і `GND`. Якщо змінити опорну точку, окремі вузлові напруги зміняться на спільну сталу величину, але напруга між будь-якою парою вузлів залишиться тією самою. Тому коректніше сказати «вузол має 5 V відносно `GND`», а не «вузол має абсолютні 5 V».[^aac-voltage-current-resistance]

`GND` не завжди означає фізичне з’єднання із землею. У пристрої на батареї це може бути лише спільний провід і зручна точка відліку; у заземленій системі зв’язок із захисним заземленням залежить від конкретної схеми. Позначення `0 V` не означає відсутності напруги між цим вузлом та іншою точкою, а також не доводить, що сам вузол безпечний для дотику.[^aac-voltage-current-resistance]

Приклад: якщо вузол A має `5 V` відносно `GND`, а вузол B має `2 V` відносно того самого `GND`, то напруга A відносно B дорівнює `3 V`. Якщо обрати B новим нулем, покази стануть `3 V` для A і `0 V` для B, але різниця між A та B не зміниться. Типова помилка – сприймати `GND` як фізичний абсолютний нуль або плутати його з обов’язковим з’єднанням із ґрунтом; завжди називайте обидві точки вимірювання.[^aac-voltage-current-resistance]

## Sources

<!-- generated from frontmatter -->
