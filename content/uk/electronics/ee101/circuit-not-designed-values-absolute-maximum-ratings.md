---
id: emb-elee-0158
title: "Чому не можна розраховувати схему на значення з розділу absolute maximum ratings?"
description: "Чому не можна розраховувати схему на значення з розділу absolute maximum ratings?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Походження питання: лекція 61, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: ti-tps752q1-datasheet
    title: "Texas Instruments TPS752-Q1 datasheet"
    url: https://www.ti.com/lit/ds/symlink/tps752-q1.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Datasheet конкретного LDO: примітка до absolute maximum ratings (це stress ratings, перевищення може спричинити пошкодження, функціонування поза recommended operating conditions не гарантоване, тривала робота біля меж може вплинути на надійність), значення V_I (absolute maximum від -0.3 до 6 V, recommended 2.7–5.5 V) і те, що електричні характеристики задано для recommended operating junction temperature range. Значення стосуються лише TPS752-Q1."
---

## Short answer

Це граничні стресові умови: їх перевищення може пошкодити мікросхему, а тривала робота біля цих меж – вплинути на надійність. Функціонування поза recommended operating conditions datasheet не гарантує, тож розрахунок ведуть за ними.[^ti-tps752q1-datasheet] Запас до абсолютних меж закладає сам розробник.

## Detailed explanation

Розділ absolute maximum ratings у datasheet описує стресові межі, а не режим роботи. TI прямо пише, що це stress ratings: перевищення може спричинити постійне пошкодження, функціонування за цих умов або за будь-яких умов поза recommended operating conditions не гарантується, а тривала робота за абсолютних максимумів може вплинути на надійність.[^ti-tps752q1-datasheet] Отже, абсолютний максимум – це межа, яку не можна перетинати, а не цільове значення, до якого схему можна «дотиснути».

Гарантії виробника зосереджені в іншому місці. Електричні характеристики (точність виходу, line і load regulation, quiescent current тощо) у datasheet наведено для recommended operating junction temperature range та за вказаних умов випробувань.[^ti-tps752q1-datasheet] Між верхньою межею recommended і абсолютним максимумом пристрій може не зламатися, але жодна з цих характеристик там не обіцяна. Проєктуючи на абсолютний максимум, розробник фактично будує схему в області, де datasheet нічого не гарантує.

Є й практична причина: реальне живлення не дорівнює номіналу. Допуск джерела, пульсації, перехідні процеси під час вмикання й викиди роблять реальну напругу вищою за номінальну, і саме для таких випадків залишають зазор між робочою точкою та абсолютним максимумом. Якщо розрахувати схему на самий максимум, цей зазор зникає, і будь-який викид виводить деталь за межу.

**Приклад (за даними TPS752-Q1):** для входу `V_I` absolute maximum дорівнює `6 V`, а recommended – `2.7–5.5 V`.[^ti-tps752q1-datasheet] Рейка `5 V ±5%` дає `4.75–5.25 V`: до верхньої межі recommended лишається `5.5 - 5.25 = 0.25 V`, а до абсолютного максимуму `6 - 5.25 = 0.75 V`. Якщо ж «розрахувати на 6 V» і подати, наприклад, `5.8 V`, пристрій формально не перевищує абсолютний максимум, але працює поза recommended: характеристики не гарантовані, а запасу до пошкодження практично немає.

**Типові помилки:**

- Читати absolute maximum як допустимий робочий режим або як номінал, до якого можна наближатися.
- Вважати, що відсутність пошкодження в межах абсолютних максимумів означає виконання параметрів із таблиці електричних характеристик.
- Не враховувати допуск живлення, пульсації й перехідні процеси під час порівняння з максимумом.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
