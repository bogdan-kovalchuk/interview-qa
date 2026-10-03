---
id: emb-elintro-0129
title: "Формула заряду конденсатора?"
description: "Формула заряду конденсатора?"
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
  - source_id: aac-capacitance-charge
    title: "All About Circuits: Electric Fields and Capacitance"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/electric-fields-capacitance/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Зв’язок заряду, напруги й ємності та накопичення й витікання заряду; реальний конденсатор може втрачати заряд через leakage."
---

## Short answer

Для лінійного конденсатора заряд пов’язаний з ємністю й напругою співвідношенням `Q = C*V`, де Q вимірюють у кулонах, C у фарадах, а V у вольтах.[^aac-capacitance-charge] Наприклад, 1000 мкФ при 12 В відповідають `0.001*12 = 0.012 Кл`.[^aac-capacitance-charge] Реальний від’єднаний конденсатор може зберігати заряд певний час, але згодом розряджається через внутрішній leakage або підключене навантаження.[^aac-capacitance-charge]

## Detailed explanation

Заряд конденсатора – це розділення електричних зарядів на його обкладках, пов’язане з напругою між ними. Для лінійної ємності їхня величина пропорційна напрузі: `Q = C*V`. У цьому записі `Q` – заряд у кулонах, `C` – ємність у фарадах, `V` – напруга у вольтах; один фарад означає один кулон заряду на один вольт.[^aac-capacitance-charge]

Формулу застосовують, якщо відомі ємність компонента та напруга саме на його виводах. Переводьте одиниці перед підстановкою: мікрофарад дорівнює `10^-6 Ф`. Наприклад, для 1000 мкФ, тобто 0.001 Ф, за напруги 12 В отримуємо 0.012 Кл. Це розрахунок запасеного заряду за заданої напруги, а не оцінка енергії: енергія в конденсаторі визначається окремо і залежить квадратично від напруги.[^aac-capacitance-charge]

Приклад розрахунку:

```text
C = 1000 мкФ = 0.001 Ф
Q = C*V = 0.001 Ф*12 В = 0.012 Кл
```

Після від’єднання джерела заряд не зобов’язаний зникнути миттєво. Ідеальна модель без шляху струму зберігала б напругу, але практичний конденсатор має leakage, а зовнішній резистор чи інше навантаження відбирає заряд. Швидкість розряду залежить від компонентів і схеми, тому перед дотиком або вимірюванням треба перевірити напругу, а не припускати, що від’єднаний компонент уже безпечний.[^aac-capacitance-charge]

**Типові помилки:**

- Підставляти 1000 мкФ як число 1000, не перевівши його у 0.001 Ф.
- Плутати заряд у кулонах з енергією у джоулях.
- Вважати, що заряд після відключення зберігається назавжди або зникає відразу.[^aac-capacitance-charge]

## Sources

<!-- generated from frontmatter -->
