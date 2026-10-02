---
id: emb-elintro-0042
title: "Що таке електрична напруга і яка її одиниця?"
description: "Що таке електрична напруга і яка її одиниця?"
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
    applicability: "Визначення напруги як різниці потенціалів між двома точками та вольта як джоуля на кулон; навчальний текст, не стандарт SI."
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

Напруга між двома точками – це зміна електричної потенціальної енергії на одиницю заряду: `V = ΔW/Q`. Одиниця – вольт (V): `1 V = 1 J/C`. Напруга має сенс лише для пари точок, а аналогія з «висотою» є лише спрощеною моделлю.[^aac-voltage-current-resistance]

## Detailed explanation

Напруга характеризує різницю електричних потенціалів між двома точками. Її можна розуміти як роботу або зміну потенціальної енергії на одиницю заряду під час перенесення заряду між цими точками: `V = ΔW/Q`. Вольт дорівнює джоулю на кулон, тобто різниця `1 V` відповідає `1 J` енергії на кожен кулон перенесеного заряду.[^aac-voltage-current-resistance]

Напруга не є кількістю заряду і сама по собі не означає, що заряд рухається: у розімкненому колі між клемами джерела може бути напруга, хоча струм у розриві не протікає. Щоб описати напругу, завжди потрібні дві точки – наприклад, клеми резистора або вузол і опорний вузол. У формулах і вимірюваннях знак залежить від порядку, в якому вибрано ці точки; перестановка щупів змінює знак показу, але не фізичну пару точок.[^aac-voltage-current-resistance]

Приклад: якщо між клемами джерела `9 V`, то для заряду `2 C` відповідна зміна енергії за модулем становить `18 J`. Це не означає, що будь-який заряд автоматично отримає саме стільки енергії: потрібно, щоб він пройшов між цими клемами, а реальна передача залежить від кола та напрямку руху. Аналогія з висотою допомагає уявити різницю потенціалів, але не слід тлумачити струм буквально як воду, що завжди «тече вниз» – у колі джерело підтримує рух зарядів, а напрямок визначають полярність і домовленість про умовний струм.[^aac-voltage-current-resistance]

**Типова помилка:** називати `GND` абсолютним нулем напруги. `GND` у схемі зазвичай є обраною опорною точкою, якій для зручності присвоїли `0 V`; інша точка, зокрема земля, може мати інший потенціал відносно неї.

## Sources

<!-- generated from frontmatter -->
