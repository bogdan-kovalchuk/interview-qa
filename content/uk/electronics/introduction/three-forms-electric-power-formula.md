---
id: emb-elintro-0045
title: "Формула електричної потужності (три форми)?"
description: "Формула електричної потужності (три форми)?"
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
  - source_id: aac-electric-power
    title: "All About Circuits: Power in Electric Circuits"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/power-electric-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Визначає електричну потужність як добуток напруги на струм і одиницю ват; разом із законом Ома обґрунтовує форми для омічного опору."
  - source_id: aac-voltage-current-resistance
    title: "All About Circuits: Ohm’s Law - How Voltage, Current, and Resistance Relate"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/voltage-current-resistance-relate/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Формулювання закону Ома для омічного провідника та його межі; джерело для виведення інших форм потужності."
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

Електрична потужність дорівнює `P = V*I` і вимірюється у ватах (W). Для омічного резистора закон Ома дає еквівалентні форми `P = I²*R` та `P = V²/R`; останні дві потребують саме відповідного опору.[^aac-electric-power]

## Detailed explanation

Електрична потужність показує швидкість передавання або перетворення енергії. Для елемента, на якому є напруга `V` і через який тече струм `I`, потужність дорівнює `P = V*I`; одиниця – ват, де `1 W = 1 J/s`. Знак залежить від вибраних напрямків напруги та струму: додатне значення за пасивною домовленістю означає, що елемент споживає потужність.[^aac-electric-power]

Для резистора, який підкоряється закону Ома `V = I*R`, підстановка напруги або струму в початкову формулу дає `P = I²*R` і `P = V²/R`. Ці вирази зручні, коли відомі інші пари величин, але не є незалежними універсальними законами для будь-якого компонента: виведення використовує саме омічну залежність. У нелінійному елементі напруга й струм можуть не бути пов’язані одним сталим опором, тож спершу визначають його робочу точку або використовують безпосереднє співвідношення потужності.[^aac-voltage-current-resistance]

Приклад: резистор `10 Ω` пропускає `0.2 A`. За ідеалізованого сталого опору падіння напруги дорівнює `2 V`, а розсіювана потужність – `0.4 W` за формулами `V = I*R` і `P = I²*R`. Результат узгоджується з `P = V*I = 2 V*0.2 A = 0.4 W`. Вибираючи реальний резистор, враховують допустиму потужність і температурні умови; обчислене значення описує розсіювання, а не автоматично потрібний номінал компонента.[^aac-electric-power]

**Типова помилка:** використовувати `P = V²/R` або `P = I²*R`, підставляючи напругу чи струм не того самого елемента. Перевірте, що величини задані на резисторі, і що його опір можна вважати сталим у розглянутому режимі.[^aac-voltage-current-resistance]

## Sources

<!-- generated from frontmatter -->
