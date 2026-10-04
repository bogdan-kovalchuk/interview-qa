---
id: emb-elee-0107
title: "Що спотворює вимірювання фільтра на високих частотах?"
description: "Що спотворює вимірювання фільтра на високих частотах?"
track: electronics
section: ee101
level: junior
type: pitfall
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
    applicability: "Походження питання: лекція 50, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: tek-probe-capacitive-loading
    title: "Tektronix: How Oscilloscope Probes Affect Your Measurement"
    url: https://www.tek.com/en/documents/application-note/how-oscilloscope-probes-affect-your-measurement
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: Вхідна ємність пробника зменшує його імпеданс на високих частотах і може навантажити вузол; вплив залежить від схеми та пробника.
---

## Short answer

Вхідна ємність пробника та паразитні параметри монтажу можуть навантажити вузол і змінити виміряну амплітуду, фазу або форму сигналу; на високій частоті ємнісний імпеданс пробника зменшується.[^tek-probe-capacitive-loading] Тому відхилення від простої моделі може бути властивістю вимірювального кола.

## Detailed explanation

Вимірювальний тракт на високих частотах сам стає частиною кола: пробник, кабель, макет і з’єднання додають ємність, індуктивність та опір. Зокрема, вхідна ємність пробника має менший реактивний опір зі зростанням частоти, тож вона сильніше навантажує вузол і може змінити амплітуду, фазу та фронти сигналу.[^tek-probe-capacitive-loading]

Для ідеального RC-фільтра достатньо одного полюса, але така модель не описує всіх деталей реального стенда. Паразитна ємність разом із вихідним опором вузла утворює додаткову часову сталу; індуктивність провідників і ємність можуть взаємодіяти та давати резонанс. Це не означає, що базова формула хибна: вона просто не включає ці компоненти. Їхній вплив помітний, коли паразитний імпеданс стає порівнянним з імпедансом досліджуваного вузла.

Наприклад, якщо пробник під’єднати до високоомного вузла, його ємність може суттєво зменшити виміряну смугу пропускання. Tektronix демонструє, що більша ємність пробника спотворює фронт і збільшує час наростання; отже, сам факт високого вхідного опору, наприклад 10 MΩ, не гарантує відсутності навантаження на високих частотах.[^tek-probe-capacitive-loading]

**Типові помилки:**
- Приписувати всю зміну АЧХ дефекту самого фільтра.
- Ігнорувати ємність пробника, бо на ньому вказано великий опір.

Щоб перевірити результат, використовуйте пробник із малою вхідною ємністю, коротке заземлення та компактний монтаж. Порівняйте вимірювання з під’єднаним і від’єднаним пробником або змініть тип пробника; якщо характеристика помітно змінюється, вимірювальне навантаження потрібно включити в модель.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
