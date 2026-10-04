---
id: emb-elee-0052
title: "Чому в конденсаторі струм випереджає напругу?"
description: "Чому в конденсаторі струм випереджає напругу?"
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
  - source_id: aac-ac-capacitor
    title: "All About Circuits: AC Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/ac-capacitor-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтверджує співвідношення i = C*dv/dt та фазу ідеального конденсатора в синусоїдальному AC-колі."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

Для ідеального конденсатора `i = C*dv/dt`: струм пропорційний швидкості зміни напруги. У синусоїдальному усталеному режимі струм випереджає напругу на 90°; це фазовий зсув, а не універсальна послідовність подій для будь-якого сигналу.[^aac-ac-capacitor]

## Detailed explanation

Напруга конденсатора пов’язана з накопиченим зарядом, а струм змінює цей заряд. Для ідеального конденсатора `i = C*dv/dt`: що швидше змінюється напруга, то більший струм потрібний. Ємність `C` вимірюють у фарадах; при сталій напрузі її похідна дорівнює нулю, тому ідеальний конденсатор не проводить струм у сталому DC-режимі. Реальний компонент має витік та інші неідеальності. [^aac-ac-capacitor]

Якщо напругу змінюють, струм заряджає або розряджає конденсатор, тобто змінює заряд на його обкладках та енергію електричного поля. Тому миттєвий струм найбільший там, де напруга змінюється найшвидше. Саме це пояснює зв’язок між струмом і напругою без помилкової аналогії, ніби струм «спершу проходить» крізь діелектрик. [^aac-ac-capacitor]

У синусоїдальному сталому режимі похідна напруги зсуває струм уперед на 90°. Коли напруга досягає піка, її миттєва зміна дорівнює нулю, тому струм ідеального конденсатора в цей момент дорівнює нулю. Коли напруга проходить через нуль і змінюється найшвидше, струм має максимум. [^aac-ac-capacitor]

**Приклад:** якщо напруга змінюється за синусоїдою частотою 1 kHz, струм ідеального конденсатора випереджає напругу на чверть періоду, тобто на 0.25 ms. Цей розрахунок описує синусоїдальний усталений режим; для перехідного процесу важливі також початкова напруга й зовнішнє коло.

**Типові помилки:**

- Казати, що конденсатор блокує будь-який струм. Він блокує сталий струм після заряджання в ідеальній моделі, але пропускає змінний струм із частотно залежним реактивним опором.
- Переносити фазові 90° на повне RC-коло. Опір змінює загальний кут між напругою та струмом. [^aac-ac-capacitor]

## Sources

<!-- generated from frontmatter -->
