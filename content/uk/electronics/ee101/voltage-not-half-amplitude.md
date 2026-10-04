---
id: emb-elee-0101
title: "Чому −3 dB за напругою – це не половина амплітуди?"
description: "Чому −3 dB за напругою – це не половина амплітуди?"
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
    applicability: "Походження питання: лекція 49, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-decibels
    title: "All About Circuits: Decibels for Voltage and Power Ratios"
    url: https://www.allaboutcircuits.com/textbook/designing-analog-chips/analog-measurements/db-for-voltage-add-power-ratios/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтримує формули перетворення відношень напруги й потужності у дБ; формула напруги припускає однакові опори."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

−3 dB відповідає відношенню амплітуд `10^(-3/20) ≈ 0.708`, тобто приблизно 70.8%, а не половині. Половина напруги становить близько −6.02 dB; половина потужності відповідає −3 dB за однакових опорів.[^aac-decibels]

## Detailed explanation

Значення в децибелах для відношення напруги обчислюють за формулою `G_dB = 20*log10(V_out/V_in)`. Тому −3 dB дають `V_out/V_in = 10^(-3/20) ≈ 0.708`: вихідна амплітуда становить близько 70.8% вхідної, а не 50%. Формула для напруги спирається на однакові опори; саме тоді відношення потужностей дорівнює квадрату відношення напруг.[^aac-decibels]

Число 3 dB походить від потужності: `10*log10(0.5) ≈ -3.01 dB`, тобто половина потужності. Коли опори однакові, потужність пропорційна квадрату напруги, отже половині потужності відповідає напруга `sqrt(0.5) ≈ 0.707` від початкової. Для половини напруги розрахунок інший: `20*log10(0.5) ≈ -6.02 dB`.[^aac-decibels]

Приклад для сигналу з початковою амплітудою 2 V: після ослаблення на 3 dB амплітуда буде приблизно `2*0.708 = 1.416 V`, а не 1 V. Якщо ж джерело й навантаження мають однаковий опір, потужність сигналу становитиме приблизно половину початкової.[^aac-decibels]

**Типова помилка:** сприйняти «половина потужності» як «половина напруги». Вона проявляється у вимірюванні −6 dB замість −3 dB для точки зрізу простого RC-фільтра. Щоб уникнути цього, спершу визначте, чи порівнюєте напругу, струм або потужність, а для відношення напруг перевірте, чи однакові опори на обох вимірюваннях.[^aac-decibels]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
