---
id: emb-elee-0079
title: "RL-коло: R = 200 Ω, L = 2.2 mH, f = 100 Hz, вхід 7 V RMS. Чому напруга на котушці лише близько 48 mV?"
description: "RL-коло: R = 200 Ω, L = 2.2 mH, f = 100 Hz, вхід 7 V RMS. Чому напруга на котушці лише близько 48 mV?"
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
    applicability: "Походження питання: лекція 45, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
---

## Short answer

За ідеальної котушки `X_L = 2π*f*L ≈ 1.38 Ω`, що набагато менше за `R = 200 Ω`; тому майже вся напруга джерела падає на резисторі. Розрахунок дає приблизно `35.0 mA RMS` і `48.4 mV RMS` на котушці, причому її напруга випереджає струм на 90°.[^aac-alternating-current]

## Detailed explanation

У цьому послідовному RL-колі реактивний опір котушки визначається частотою та індуктивністю: `X_L = 2π*f*L`. Для наведених значень `f = 100 Hz` і `L = 2.2 mH` він становить приблизно `1.38 Ω`, значно менше за `200 Ω` резистора. Тому модуль повного імпедансу майже дорівнює опору резистора, а струм близький до `7 V/200 Ω = 35 mA`.[^aac-alternating-current]

Напруга на котушці є добутком струму на її реактивний опір: `V_L = I*X_L ≈ 35 mA*1.38 Ω = 48.3 mV`. Це RMS-значення за умови, що 7 V – RMS і компоненти ідеальні. Напруга на котушці не дорівнює напрузі джерела: послідовні напруги додаються як фазори. Напруга резистора майже співфазна зі струмом, а напруга котушки випереджає його на 90°.[^aac-alternating-current]

Приклад повної перевірки:
```text
X_L = 2π*100*0.0022 ≈ 1.382 Ω
|Z| = √(200² + 1.382²) ≈ 200.005 Ω
I = 7/|Z| ≈ 0.0350 A RMS
V_L = I*X_L ≈ 0.0484 V RMS
```
Отже, результат близько 48 mV не є парадоксом: на цій частоті котушка має дуже малий реактивний опір порівняно з резистором. Якщо підвищити частоту або індуктивність, `X_L` зросте й більша частина напруги може припасти на котушку.[^aac-alternating-current]

**Типові помилки:**
- Вважати, що послідовна котушка завжди отримує більшість напруги.
- Додавати `R` і `X_L` скалярно замість векторно.
- Плутати mH з H або RMS із peak.

Реальна котушка має опір обмотки, а вимірювальний прилад має скінченні смугу й точність. Для цих параметрів їхній вплив може бути помітним відносно очікуваних десятків мілівольтів; виміряйте напругу безпосередньо на виводах котушки та врахуйте фактичний опір обмотки.[^aac-alternating-current]

## Sources

<!-- generated from frontmatter -->
