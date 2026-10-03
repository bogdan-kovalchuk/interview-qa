---
id: emb-elintro-0203
title: "Умова насичення для `NPN`-транзистора?"
description: "Умова насичення для `NPN`-транзистора?"
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
    applicability: "Походження питання: лекція 19, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-bjt-active-mode
    title: "Active-mode Operation (BJT), All About Circuits"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/active-mode-operation-bjt/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Визначає saturation як стан, обмежений джерелом живлення та навантаженням; не задає універсального значення V_CE(sat)."
---

## Short answer

У saturation обидва переходи NPN, база–емітер і база–колектор, прямо зміщені; для звичайного включення це дає `V_B > V_E` і `V_B > V_C`. Струм колектора тоді обмежує коло живлення та навантаження, а не наближене співвідношення `I_C ≈ β*I_B`; `V_CE(sat)` залежить від транзистора й умов вимірювання.[^aac-bjt-active-mode]

## Detailed explanation

Saturation у BJT – це режим, у якому обидва p-n переходи NPN-транзистора прямо зміщені: база–емітер і база–колектор. Для поширеної схеми з емітером на нижчому потенціалі це означає, що база має вищий потенціал за емітер і колектор. На відміну від active, колекторний струм уже не може зростати пропорційно базовому: його задають джерело живлення та опір навантаження.[^aac-bjt-active-mode]

Для ключового кола з резистором колектора доступний струм приблизно визначається різницею напруг живлення та падіння на транзисторі, поділеною на опір навантаження. Якщо базовий струм недостатній, транзистор лишається в active, а падіння на ньому більше; коли керування вимагає від нього більшого струму, ніж може дати навантаження, робоча точка доходить до saturation. Збільшення базового струму після цього переважно додає надлишковий заряд і може збільшити час вимкнення, а не помітно збільшити струм навантаження.[^aac-bjt-active-mode]

`V_CE(sat)` – не універсальне число 0.1 V чи 0.2 V. У документації транзистора його наводять для конкретних колекторного та базового струмів; значення залежить від типу компонента і рівня примусового підсилення струму. Для проєктування ключа треба користуватися відповідною таблицею datasheet, а не переносити типовий приклад на будь-який транзистор.[^aac-bjt-active-mode]

**Приклад:** нехай є джерело 5 V, резистор колектора 1 kΩ, а падіння saturation для обраної моделі за заданого струму становить 0.2 V. Тоді струм навантаження буде близько `(5 V - 0.2 V)/1 kΩ = 4.8 mA`; більший базовий струм не змусить резистор пропустити значно більше за цих умов.[^aac-bjt-active-mode]

**Типова помилка:** стверджувати, що при saturation `V_CE` завжди дорівнює рівно 0.1 V. Перевіряйте умови, за яких datasheet задає `V_CE(sat)`, і не використовуйте active-модель для розрахунку ключа в насиченні.

## Sources

<!-- generated from frontmatter -->
