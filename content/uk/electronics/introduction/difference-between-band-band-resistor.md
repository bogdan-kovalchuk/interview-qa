---
id: emb-elintro-0127
title: "Яка різниця між 4-смужковим і 5-смужковим резистором?"
description: "Яка різниця між 4-смужковим і 5-смужковим резистором?"
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
    applicability: "Структура чотири- та п'ятисмугового коду, значення кольорів і приклади допусків; фактичні допуски залежать від компонента."
---

## Short answer

У чотирисмуговому коді дві перші смуги задають цифри, третя – множник, четверта – допуск; у п’ятисмуговому перші три задають цифри, а четверта й п’ята – множник і допуск.[^vishay-resistor-color-code] П’ятисмуговий формат додає значущу цифру, але кількість смуг сама по собі не гарантує точність: допуск читають за останньою смугою та документацією компонента.[^vishay-resistor-color-code]

## Detailed explanation

Кількість смуг визначає, скільки цифр використано для номіналу та де розташовані множник і допуск. У типовому чотирисмуговому коді перші дві смуги – значущі цифри, третя – множник, четверта – допуск. У п’ятисмуговому коді значущих цифр три: четверта смуга є множником, п’ята – допуском.[^vishay-resistor-color-code]

Додаткова цифра дає змогу записати номінал з більшою кількістю значущих цифр. Проте не слід визначати допуск лише за числом смуг. У таблиці виробника золотий відповідає ±5%, срібний ±10%, а інші кольори мають інші значення; конкретну комбінацію звіряють з відповідною схемою маркування та документацією деталі.[^vishay-resistor-color-code]

Наприклад, у п’ятисмуговому коді коричнева, червона й фіолетова смуги можуть означати цифри 1, 2 і 7; наступна задає множник, а остання – допуск. Для чотирьох смуг коричневий, червоний, помаранчевий, золотий означає `12*1000 Ом` із допуском ±5%. Це пояснює роль позицій, але реальний компонент потрібно читати за його фактичними кольорами.[^vishay-resistor-color-code]

**Типові помилки:**

- Вважати, що всі п’ятисмугові резистори мають допуск ±1% або кращий.
- Застосувати послідовність для чотирьох смуг до п’ятисмугового компонента.
- Прийняти четверту смугу п’ятисмугового резистора за допуск, хоча це множник.[^vishay-resistor-color-code]

## Sources

<!-- generated from frontmatter -->
