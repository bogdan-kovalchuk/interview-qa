---
id: emb-elee-0011
title: "Що таке потенціометр і яку роль виконує wiper?"
description: "Що таке потенціометр і яку роль виконує wiper?"
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
    applicability: "Походження питання: лекція 34, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: bourns-potentiometer
    title: "Bourns: 3386 Trimpot Trimming Potentiometer Datasheet"
    url: https://bourns.com/docs/Product-Datasheets/3386.pdf
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Підтверджує триконтактну конфігурацію, роботу voltage divider та характеристики конкретної серії; числові межі стосуються лише серії 3386."
---

## Short answer

Потенціометр – резистивний елемент із двома кінцевими виводами та рухомим контактом (wiper), який з’єднує вихід із вибраною точкою вздовж елемента. Між кінцевими виводами вимірюється повний опір, а wiper задає два часткові опори, сума яких приблизно дорівнює повному.[^bourns-potentiometer]

## Detailed explanation

Потенціометр має резистивну доріжку та контакт, який переміщується вздовж неї. Кінцеві виводи під’єднані до двох кінців доріжки; третій вивід з’єднаний із wiper. Коли вал обертається або повзунок рухається, контакт змінює точку дотику, тому опір від wiper до кожного кінця змінюється у протилежних напрямках.[^bourns-potentiometer]

Якщо вимірювати між крайніми виводами, опір `R_total` майже не залежить від положення wiper. Від wiper до одного кінця маємо `R_1`, а до другого – `R_2`; для ідеальної доріжки `R_1 + R_2 = R_total`. У реального компонента є допуск повного опору, контактний опір і невеликий залишковий опір біля кінців, тому рівність є моделлю, а не гарантією нульового опору в крайньому положенні.[^bourns-potentiometer]

У схемі як voltage divider підключають обидва кінці доріжки до опорних напруг, а сигнал знімають із wiper. Як rheostat використовують wiper і лише один кінець, тож компонент керує струмом або опором послідовної гілки. Вивід wiper має обмеження за струмом і потужністю, зазначені в даташиті; він не призначений для навантаження без перевірки рейтингу.[^bourns-potentiometer]

Приклад: у потенціометра 10 kΩ у середньому положенні лінійної доріжки опір від wiper до кожного кінця буде приблизно 5 kΩ без навантаження. Під’єднане коло може змінити фактичний поділ опорів і вихідну напругу, бо навантаження wiper включається паралельно частині доріжки.

**Типова помилка:** вважати wiper окремим джерелом напруги або очікувати, що вихідний опір дорівнює `R_total`. Потенціометр лише формує сигнал з наявної напруги, а його вихідний опір залежить від положення контакту та навантаження.

## Sources

<!-- generated from frontmatter -->
