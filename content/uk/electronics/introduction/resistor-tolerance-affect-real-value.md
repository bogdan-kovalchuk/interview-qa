---
id: emb-elintro-0136
title: "Як допуск резистора впливає на реальне значення?"
description: "Як допуск резистора впливає на реальне значення?"
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
  - source_id: fda-resistor-tolerance
    title: "FDA: Electronic Components – Resistors"
    url: https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/inspection-technical-guides/electronic-components-resistors
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Визначення допуску як дозволеного відхилення від номіналу та вплив умов довкілля; числовий приклад 1 kΩ ±5% є прямим обчисленням."
---

## Short answer

Допуск задає дозволене відхилення фактичного опору від номіналу за визначених умов. Для `1 kΩ ±5%` межі становлять `950 Ω` і `1050 Ω`; це діапазон, а не обіцянка, що виміряне значення буде рівно на одній із меж.[^fda-resistor-tolerance]

## Detailed explanation

Допуск резистора – це максимально дозволене відхилення його опору від номінального значення за умов, визначених виробником. Номінал є маркованим значенням, а допуск задає інтервал можливих значень нового компонента; він не означає, що резистор обов’язково має помилку саме такого розміру.[^fda-resistor-tolerance]

Для `1 kΩ ±5%` обчислюємо п’ять відсотків від 1000 Ω: `0.05*1000 Ω = 50 Ω`. Отже, допустимий інтервал становить від `1000 Ω - 50 Ω = 950 Ω` до `1000 Ω + 50 Ω = 1050 Ω`. Це початковий допуск за зазначених умов, а не повна гарантія стабільності в будь-якому режимі.[^fda-resistor-tolerance]

Температурний коефіцієнт, нагрівання від власної потужності, старіння та вологість можуть додатково змінювати опір. Для точного розрахунку схеми важливо перевірити в документації не лише допуск, а й інші параметри компонента та робочі умови. У подільнику напруги крайні значення обох резисторів можуть разом змістити вихід, тому аналізують найгірше поєднання, а не лише номінальні числа.[^fda-resistor-tolerance]

Приклад: якщо виміряний опір дорівнює `1030 Ω`, він усе ще потрапляє в наведений інтервал і відповідає допуску. Значення `1060 Ω` вийшло б за межу для нового резистора за тих самих умов, але перед висновком слід перевірити точність вимірювача, температуру компонента та чи від’єднаний резистор від паралельних шляхів у схемі.

**Типова помилка:** трактувати ±5% як точність вимірювання або вважати, що кожен резистор відхиляється рівно на 5%. Допуск описує прийнятні граничні значення; фактичне значення може бути будь-де всередині діапазону.

## Sources

<!-- generated from frontmatter -->
