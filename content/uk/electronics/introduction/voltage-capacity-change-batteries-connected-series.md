---
id: emb-elintro-0058
title: "Як змінюється напруга і ємність при послідовному з'єднанні батарей?"
description: "Як змінюється напруга і ємність при послідовному з'єднанні батарей?"
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
    applicability: "Правило для послідовного з'єднання: напруга зростає, ємність у Ah не змінюється; стосується конфігурації батареї з однакових елементів."
---

## Short answer

У послідовному ланцюжку напруги елементів додаються, а ємність у А·год для однакових елементів не зростає. Наприклад, чотири елементи по 1.5 В дають номінально 6 В; фактичні параметри залежать від елементів і навантаження.[^iata-lithium-guidance-2023]

## Detailed explanation

За послідовного з’єднання позитивний полюс одного елемента з’єднаний із негативним полюсом наступного. Напруги елементів додаються, бо напруга між крайніми виводами є сумою різниць потенціалів на кожному елементі. Для чотирьох однакових елементів з номіналом 1.5 В номінальна напруга батарейного ланцюжка дорівнює 6 В.[^iata-lithium-guidance-2023]

Через усі послідовно з’єднані елементи проходить той самий струм. Тому ланцюжок обмежений елементом, який першим досягне граничного стану розряду; додавання елементів не збільшує Ah так, як це робить паралельне з’єднання. Для однакових елементів номінальна ємність у Ah лишається ємністю одного елемента, тоді як сумарна номінальна напруга зростає.[^iata-lithium-guidance-2023]

Оскільки енергія приблизно дорівнює добутку заряду на напругу, додавання послідовних елементів збільшує Wh батареї, хоча Ah не змінюється. Це пояснює, чому вища напруга не означає більшої ємності в Ah. Реальні батареї також мають внутрішні втрати, а паспортні характеристики задаються умовами тесту; не слід розглядати номінальні числа як незмінні під будь-яким навантаженням.[^iata-lithium-guidance-2023]

**Типова помилка:** казати, що послідовне з’єднання збільшує ємність у мА·год. Воно збільшує напругу й сумарну енергію; ємність у Ah для однакових елементів залишається сталою.

## Sources

<!-- generated from frontmatter -->
