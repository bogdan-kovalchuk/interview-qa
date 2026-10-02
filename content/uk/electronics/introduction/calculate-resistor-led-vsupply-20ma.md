---
id: emb-elintro-0048
title: "Як розрахувати резистор для `LED`, якщо `V_supply = 5 V`, `V_f = 2 V`, `I = 20 mA`?"
description: "Розрахунок послідовного резистора для LED: V_supply = 5 V, V_f = 2 V, I = 20 mA."
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
  - source_id: aac-led-resistor
    title: 'All About Circuits: Series LED Resistor Calculator'
    url: https://www.allaboutcircuits.com/tools/led-resistor-calculator
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: 'Формула послідовного обмежувального резистора та потреба обмежувати струм LED; конкретні Vf і допустимий струм треба брати з datasheet обраного LED.'
---

## Short answer

Для одного `LED` послідовний резистор у цьому номінальному прикладі дорівнює `R = (V_supply - V_f)/I = (5 V - 2 V)/0.020 A = 150 Ω`. На ньому розсіюється `P = I²*R = 0.060 W`; фактичні `V_f` і допустимий струм слід перевірити за datasheet LED.[^aac-led-resistor]

## Detailed explanation

Послідовний резистор обмежує струм через `LED`: решта напруги джерела падає на резистор. Для заданої робочої точки застосовують закон Ома до цієї частини кола. Формула передбачає один LED, джерело постійної напруги й приблизно сталу пряму напругу діода; сам `LED` не є лінійним резистором і без обмеження струму його робоча точка не визначається лише номіналом живлення.[^aac-led-resistor]

**Приклад розрахунку:**

```text
V_R = 5 V - 2 V = 3 V
R = V_R / I = 3 V / 0.020 A = 150 Ω
P_R = V_R * I = 3 V * 0.020 A = 0.060 W
```

Отже, `150 Ω` дає розрахункові `20 mA` за припущених `5 V` живлення та `2 V` прямої напруги. Резистор `180 Ω` зменшить номінальний струм приблизно до `16.7 mA`, що може бути доречним для меншої яскравості чи запасу; перевіряють також допуск джерела, розкид `V_f` та граничний струм конкретного LED за його datasheet.[^aac-led-resistor]

Потужність у резисторі становить `60 mW` у цих ідеалізованих умовах. Номінал потужності компонента має перевищувати розсіювану потужність з урахуванням температури, охолодження й рекомендацій виробника; отже `1/4 W` тут має запас, але це не універсальна вимога до всіх таких кіл.[^aac-led-resistor]

Важливо не змішувати одиниці: `20 mA = 0.020 A`. Підставляння числа 20 замість `0.020 A` занижує розрахований опір у тисячу разів. Для кількох послідовних LED у формулі віднімають суму їхніх прямих напруг; для потужного LED простий резистор може бути непридатним, і потрібен стабілізатор струму.[^aac-led-resistor]

## Sources

<!-- generated from frontmatter -->
