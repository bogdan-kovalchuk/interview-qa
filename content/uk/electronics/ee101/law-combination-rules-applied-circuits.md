---
id: emb-elee-0059
title: "Як застосовують закон Ома і правила з’єднань у AC-колах?"
description: "Як застосовують закон Ома і правила з’єднань у AC-колах?"
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
    applicability: "Походження питання: лекція 41, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-ac-series-parallel-laws
    title: "All About Circuits: Series-parallel R, L, and C"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-5/series-parallel-r-l-and-c/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Закон Ома для AC і послідовне та паралельне зведення комплексних імпедансів на спільній частоті."
---

## Short answer

У синусоїдальному усталеному режимі на спільній частоті закон Ома для фазорів має вигляд `V = I*Z`, де `V`, `I` та `Z` – комплексні величини. Послідовні імпеданси додають: `Z_total = ΣZ`; паралельні обчислюють як `1/Z_total = Σ(1/Z)`. Усі обчислення ведуть у комплексній формі, щоб зберегти фазу.[^aac-ac-series-parallel-laws]

## Detailed explanation

Правила аналізу AC-кіл зберігають знайомий вигляд, якщо напруги й струми подати фазорами, а кожен компонент замінити його імпедансом для потрібної частоти. Тоді закон Ома записують як `V = I*Z`, а закони Кірхгофа застосовують до комплексних величин. Цей підхід працює для лінійного кола в синусоїдальному усталеному режимі, коли всі величини належать одній частоті.[^aac-ac-series-parallel-laws]

Для послідовного з’єднання струм спільний, а імпеданси додаються комплексно. Для паралельного з’єднання напруга спільна, струми гілок додаються; еквівалентний імпеданс можна знайти через суму обернених імпедансів. Такі співвідношення подібні до правил для резисторів, але числа містять дійсну та уявну частини, а тому фазовий кут не можна відкидати під час обчислень.[^aac-ac-series-parallel-laws]

Приклад: нехай джерело має фазор `V = 10∠0° V`, а дві послідовні складові мають `Z_1 = 3 + j*4 Ω` та `Z_2 = 2 - j*1 Ω`. Тоді `Z_total = 5 + j*3 Ω`, а `I = V/Z_total`. Для ділення зручно перейти до полярної форми: `|Z_total| ≈ 5.83 Ω`, `∠Z_total ≈ 31.0°`, отже `I ≈ 1.72∠-31.0° A`. Просте додавання модулів дало б інший, хибний результат, бо реактивні складові частково компенсуються.[^aac-ac-series-parallel-laws]

Після обчислень корисно перевірити баланс: сума падінь напруг у послідовному контурі має дорівнювати джерельній напрузі, а сума струмів паралельних гілок – струму до вузла. Якщо результат має неочікуваний кут, перевірте обраний напрямок фазорів, знак ємнісної реактивності та градусний чи радіанний режим калькулятора. Для сигналу з кількома частотами аналіз повторюють окремо для кожної частотної складової.[^aac-ac-series-parallel-laws]

**Типові помилки:**

- Зводити імпеданси за їх модулями як звичайні опори.
- Змішувати фазори різних частот в одному простому зведенні.
- Застосовувати послідовну формулу до паралельної топології або навпаки.[^aac-ac-series-parallel-laws]

## Sources

<!-- generated from frontmatter -->
