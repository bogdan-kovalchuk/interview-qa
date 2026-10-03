---
id: emb-elintro-0115
title: "Формула для розрахунку обмежувального резистора `LED`?"
description: "Формула для розрахунку обмежувального резистора `LED`?"
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
    applicability: "Походження питання: лекція 12, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: idec-led-current-limiting-resistor
    title: "IDEC: A1, A2, A8 Series Miniature Pilot Lights"
    url: https://media.digikey.com/pdf/Data%20Sheets/IDEC%20PDFs/A1%2CA2%2CA8_Miniature_Switches_Pilot_lights.pdf
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Вказує формулу послідовного резистора R = (operating voltage – Vf) / If та потребу в обмеженні струму; числові специфікації стосуються ламп IDEC."
---

## Short answer

Для послідовного резистора `R = (V_supply - V_f)/I_LED`. За `V_supply = 5 V`, `V_f = 2.1 V` і цільового струму `15 mA` розрахунок дає `193 Ω`; вибір `220 Ω` дає приблизно `13.2 mA` за цих припущень.[^idec-led-current-limiting-resistor]

## Detailed explanation

Послідовний резистор обмежує струм через LED, приймаючи на себе частину напруги джерела. У простому колі з одним світлодіодом закон напруги Кірхгофа дає `V_supply = V_f + V_R`, а закон Ома для резистора – `R = V_R/I_LED`. Звідси формула `R = (V_supply - V_f)/I_LED`. Вона передбачає джерело постійної напруги, один LED і резистор послідовно та струм, який у цій гілці однаковий через обидва компоненти.[^idec-led-current-limiting-resistor]

Одиниці мають бути узгоджені: струм у формулі задають в амперах, якщо напругу задають у вольтах, тоді опір виходить в омах. `V_f` не є точною константою, тому розрахунок за типовим значенням дає наближення. Для безпечного вибору перевірте в datasheet допустимий струм LED і повторіть оцінку для мінімального `V_f` та максимальної напруги живлення – ця комбінація дає найбільший струм.[^idec-led-current-limiting-resistor]

Приклад розрахунку для `5 V`, типового `V_f = 2.1 V` і цільового струму `15 mA`:
```text
R = (5 - 2.1)/0.015 = 193.3 Ω
I_LED при R = 220 Ω: (5 - 2.1)/220 = 0.0132 A
P_R = (5 - 2.1)*0.0132 ≈ 0.038 W
```
Тому `220 Ω` дає близько `13.2 mA`; для резистора потрібен номінал потужності вище за розраховані приблизно `0.038 W`, із запасом відповідно до температури й умов монтажу. За інших реальних меж живлення або `V_f` струм буде іншим.[^idec-led-current-limiting-resistor]

**Типові помилки:**
- Підставляти `15` замість `0.015` для струму `15 mA`.
- Ділити повну напругу джерела на струм, забуваючи відняти падіння на LED.
- Вважати обчислене число гарантованим струмом без перевірки розкиду параметрів.

## Sources

<!-- generated from frontmatter -->
