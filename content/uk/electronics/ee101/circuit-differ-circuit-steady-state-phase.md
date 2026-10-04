---
id: emb-elee-0047
title: "Чим RC-коло відрізняється від RL-кола в усталеному DC-режимі та за фазою?"
description: "Чим RC-коло відрізняється від RL-кола в усталеному DC-режимі та за фазою?"
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
    applicability: "Походження питання: лекція 39, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: phase-basics
    title: "Phase Relationships in Inductive and Capacitive Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/phase-relationships/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Фазові співвідношення ідеальних L та C у синусоїдальному усталеному режимі."
---

## Short answer

В усталеному DC-режимі ідеальний конденсатор є розривом, а ідеальний індуктор – коротким замиканням. Для синусоїдального AC струм у конденсаторі випереджає напругу на 90°, а в індукторі напруга випереджає струм на 90°.[^phase-basics]

## Detailed explanation

Конденсатор і індуктор зберігають енергію, тому не можуть миттєво змінити відповідно свою напругу чи струм. Їхні співвідношення `i = C*dv/dt` та `v = L*di/dt` пояснюють поведінку в часі. За усталеного DC напруга конденсатора не змінюється, отже струм через ідеальну ємність дорівнює нулю. Струм ідеального індуктора є сталим, отже напруга на ньому дорівнює нулю.[^phase-basics]

У синусоїдальному режимі похідна змінює фазу на чверть періоду. Для конденсатора струм випереджає напругу на 90°, а для індуктора напруга випереджає струм на 90°. Це твердження стосується ідеального реактивного елемента. У реальному колі наявний опір, інші компоненти й навантаження, тому сумарний фазовий кут залежить від частоти та топології й зазвичай не дорівнює рівно 90°.[^phase-basics]

Наприклад, за `f = 1 kHz` період становить `1 ms`, а чверть періоду – `0.25 ms`. У чистому індукторі максимум напруги настає на чверть періоду раніше за максимум струму. Усталений DC не має періоду чи фазового випередження: це інший режим, а не синусоїда нульової фази.[^phase-basics]

**Типова помилка:** плутати напрямок фазового зсуву. ELI означає, що в індукторі (`L`) електрорушійна сила/напруга (`E`) випереджає струм (`I`); ICE нагадує, що в конденсаторі (`C`) струм випереджає напругу. Перевіряйте це за рівняннями елементів і пам’ятайте про домовленість щодо полярності та фазорів.

## Sources

<!-- generated from frontmatter -->
