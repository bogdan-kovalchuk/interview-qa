---
id: emb-elintro-0126
title: "Який опір має резистор зі смугами коричневий, червоний, помаранчевий і золотий?"
description: "Який опір має резистор зі смугами коричневий, червоний, помаранчевий і золотий?"
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
    applicability: "Походження питання: лекція 13, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: vishay-resistor-color-code
    title: "Vishay: Color Code and Standard Resistance Series"
    url: https://www.vishay.com/doc/?20143=
    accessed: 2026-10-04
    kind: official
    version: "Revision 28-Aug-09"
    applicability: "Таблиця коду смуг: коричневий 1, червоний 2, помаранчевий множник 10^3, золотий допуск ±5%; правила для чотирьох смуг."
---

## Short answer

B1 і B2 задають цифри 1 і 2, B3 задає множник ×1000, а золота B4 – допуск ±5%.[^vishay-resistor-color-code] Номінал дорівнює `12*1000 = 12 000 Ом`, тобто 12 кОм. За цим допуском фактичний опір може бути від 11.4 кОм до 12.6 кОм.[^vishay-resistor-color-code]

## Detailed explanation

Це чотирисмугове маркування: перші дві смуги кодують значущі цифри, третя – степінь множника, а четверта, зазвичай віддалена від інших, задає допуск. У таблиці коду коричневому відповідає 1, червоному – 2, помаранчевому – множник `10^3`, а золотому – допуск ±5%.[^vishay-resistor-color-code]

Отже, перші дві смуги утворюють число 12, після чого множник дає `12*1000 = 12 000 Ом`. Золотий допуск означає відхилення від номіналу на п’ять відсотків, а не додаткову цифру. Межі для цього номіналу становлять 11 400 Ом і 12 600 Ом; обчислення показує діапазон, а не гарантує, що виміряне значення буде рівно посередині.[^vishay-resistor-color-code]

Приклад розрахунку:

```text
12 000 Ом * 0.05 = 600 Ом
12 000 Ом - 600 Ом = 11 400 Ом
12 000 Ом + 600 Ом = 12 600 Ом
```

Під час читання починайте з боку, де перші смуги згруповані щільніше; смуга допуску часто відділена проміжком. Якщо напрямок або колір важко розрізнити, перевірте опір мультиметром на знеструмленій схемі, бажано ізолювавши один вивід: паралельні компоненти можуть вплинути на показання. Вимірювання перевіряє компонент у конкретних умовах, тоді як кольоровий код задає номінал і допуск.[^vishay-resistor-color-code]

**Типові помилки:**

- Читати смуги у зворотному напрямку й отримати інший номінал.
- Сприймати золоту смугу як цифру, хоча тут вона позначає допуск.
- Вважати, що будь-який екземпляр має рівно 12 кОм, і трактувати значення в межах допуску як несправність.[^vishay-resistor-color-code]

## Sources

<!-- generated from frontmatter -->
