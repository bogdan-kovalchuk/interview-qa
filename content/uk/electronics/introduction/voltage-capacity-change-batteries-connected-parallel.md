---
id: emb-elintro-0059
title: "Як змінюється напруга і ємність при паралельному з'єднанні батарей?"
description: "Як змінюється напруга і ємність при паралельному з'єднанні батарей?"
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
    applicability: "Походження питання: лекція 7, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: iata-lithium-guidance-2023
    title: "IATA Lithium Battery Guidance Document 2023"
    url: https://data.energizer.com/wp-content/uploads/2023/04/IATA-Lithium-Guidance-2023.pdf
    accessed: 2026-10-04
    kind: official
    version: "2023"
    applicability: "Правило для паралельного з'єднання: ємність у Ah зростає, номінальна напруга залишається; загальна формула передбачає узгоджені елементи."
---

## Short answer

За паралельного з’єднання однакових елементів напруга лишається тією самою, а ємності в А·год додаються. Підключення має бути спроєктоване для сумісних елементів: просте паралельне з’єднання не гарантує рівного розподілу струму чи безпечного заряджання.[^iata-lithium-guidance-2023]

## Detailed explanation

За паралельного з’єднання однойменні полюси елементів з’єднані між собою. Усі гілки мають спільну напругу на клемах, тому номінальна напруга комбінації відповідає напрузі одного елемента. Зарядові ємності в Ah додаються: два однакові елементи по 2 Ah утворюють номінально 4 Ah при тій самій напрузі.[^iata-lithium-guidance-2023]

Сумарна ємність не означає, що кожен елемент гарантовано віддасть однакову частину струму. Розподіл залежить від внутрішніх опорів, температури, з’єднань, стану та характеристик елементів. Виробник готової батареї може застосовувати підібрані елементи, захист і контроль; паралельне підключення саме по собі не є схемою заряджання або системою керування батареєю.[^iata-lithium-guidance-2023]

Розрахунок додає Ah лише для елементів, які можна безпечно експлуатувати разом і які мають спільну номінальну напругу та сумісні робочі межі. Наприклад, не можна робити висновок про придатність комбінації лише з однакової фізичної форми. Паспортна ємність вимірюється за визначених умов навантаження й порогової напруги, тож реальна доступна ємність залежить від режиму.[^iata-lithium-guidance-2023]

**Типова помилка:** припускати, що паралельні елементи автоматично розподілять струм порівну. Перевіряйте вимоги виробника до конфігурації, сумісності та захисту.

## Sources

<!-- generated from frontmatter -->
