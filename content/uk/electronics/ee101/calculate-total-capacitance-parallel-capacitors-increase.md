---
id: emb-elee-0024
title: "Як обчислити загальну ємність паралельних конденсаторів і чому вона зростає?"
description: "Як обчислити загальну ємність паралельних конденсаторів і чому вона зростає?"
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
    applicability: "Походження питання: лекція 36, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-parallel-capacitors
    title: "All About Circuits: Series and Parallel Capacitors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/series-and-parallel-capacitors/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Еквівалентна ємність паралельного з’єднання та модель сумарної площі пластин."
  - source_id: aac-capacitor-factors
    title: "All About Circuits: Factors Affecting Capacitance"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/factors-affecting-capacitance/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Зв’язок ємності з площею пластин, відстанню та permittivity."
---

## Short answer

Для паралельно з’єднаних конденсаторів `C_total = C_1 + C_2 + ... + C_n`, якщо їхні виводи підключені до тих самих двох вузлів. Наприклад, `10 µF + 22 µF = 32 µF` в ідеальній моделі. Еквівалентність пояснюється тим, що всі компоненти мають однакову напругу, а їхні заряди додаються.[^aac-parallel-capacitors]

## Detailed explanation

Паралельне з’єднання означає, що кожен конденсатор підключений до тієї самої пари вузлів, отже напруга на кожному однакова. Для кожного компонента `Q_i = C_i*V`; сумарний заряд вузла є сумою зарядів гілок. Якщо записати `Q_total = C_total*V`, то після скорочення спільної напруги отримуємо `C_total = C_1 + C_2 + ... + C_n`. Це правило не залежить від того, чи однакові номінали компонентів.[^aac-parallel-capacitors]

Інтуїтивно для ідеальних плоских конденсаторів паралельне з’єднання поводиться як більша сумарна площа пластин за тієї самої відстані та dielectric. Ємність зростає з площею перекриття та permittivity й зменшується зі збільшенням відстані; саме площі діють адитивно в такій моделі. У реальних деталях геометрія корпусу, допуск і паразитні параметри обмежують точність цієї картини, але сума номінальних ємностей лишається базовим розрахунком для паралельного еквівалента.[^aac-parallel-capacitors] [^aac-capacitor-factors]

Приклад: для `10 µF` і `22 µF`, з’єднаних паралельно, `C_total = 10 µF + 22 µF = 32 µF`. Обидва компоненти мають спільну напругу на клемах, а джерело під час заряджання постачає сумарний заряд. Це не означає, що допустима робоча напруга набору автоматично зростає: паралельне з’єднання збільшує ємність, а не рейтинг напруги; напругу обмежує рейтинг кожного компонента та умови роботи.[^aac-parallel-capacitors]

Формула передбачає справжнє паралельне підключення до однакових двох вузлів. Якщо деталі з’єднані послідовно, напруга між вузлами розподіляється, а еквівалентну ємність рахують інакше. Також реальна схема може мати опір доріжок і ESR, тож на високих частотах простий скалярний номінал не описує весь імпеданс мережі.[^aac-parallel-capacitors]

**Типова помилка:** застосувати формулу паралельних резисторів або додати ємності елементів, що фактично стоять послідовно. Спершу простежте вузли: лише компоненти, підключені до тієї самої пари вузлів, дають безпосередню суму ємностей.[^aac-parallel-capacitors]

## Sources

<!-- generated from frontmatter -->
