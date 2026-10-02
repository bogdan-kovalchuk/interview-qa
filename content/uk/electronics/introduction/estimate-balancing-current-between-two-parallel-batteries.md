---
id: emb-elintro-0073
title: "Як оцінити вирівнювальний струм між двома паралельними батареями?"
description: "Як оцінити вирівнювальний струм між двома паралельними батареями?"
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
    applicability: "Походження питання: лекція 8, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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

Оціни початковий струм як `I = ΔV/(R_int1 + R_int2 + R_wires)`, де `ΔV` – різниця напруг холостого ходу, а `R_wires` включає проводи й контакти. Наприклад, за `ΔV = 0.5 V` і сумарного опору `0.1 Ω` проста резистивна модель дає `5 A`; це наближення, а не точний прогноз поведінки батарей.[^aac-direct-current]

## Detailed explanation

Вирівнювальний струм – це струм, який тече від батареї з вищою напругою холостого ходу до батареї з нижчою після паралельного з’єднання. Для першої оцінки батареї моделюють як ідеальні джерела напруги з послідовними внутрішніми опорами. Контур струму проходить крізь опір обох батарей і з’єднувальні проводи, тому повний опір у знаменнику є сумою цих складників.[^aac-direct-current]

Приклад розрахунку для спрощеної моделі:

```text
ΔV = 12.8 V - 12.3 V = 0.5 V
R_total = 0.04 Ω + 0.05 Ω + 0.01 Ω = 0.10 Ω
I ≈ ΔV/R_total = 0.5 V/0.10 Ω = 5 A
```

Отже, оцінка початкового струму становить `5 A`. Значення внутрішнього опору не є сталою характеристикою на всі випадки: вимірювання залежить від стану заряду, температури, частоти або тривалості імпульсу та методу тестування. Електрохімічна поляризація також робить батарею складнішою за ідеальне джерело з одним резистором, тому струм змінюється з часом. Для проєктування захисту потрібні дані виробника або вимірювання для конкретної батареї, а не лише ця формула.[^aac-direct-current]

**Типова помилка:** ділити різницю напруг лише на опір однієї батареї або забувати опір проводів і контактів. Це дає хибну оцінку струму, тому потрібно врахувати весь контур і пам’ятати про обмеження простої резистивної моделі.[^aac-direct-current]

## Sources

<!-- generated from frontmatter -->
