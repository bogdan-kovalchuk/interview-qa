---
id: emb-elintro-0292
title: "Як перетворити mil у міліметри?"
description: "Як перетворити mil у міліметри?"
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
    applicability: "Походження питання: лекція 26, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: nist-inch
    title: "NIST: SI Units – Length"
    url: https://www.nist.gov/pml/owm/si-units-length
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "NIST визначає міжнародний дюйм як рівно 25.4 мм; це дає точний коефіцієнт для mil."
---

## Short answer

Один mil дорівнює 0.001 дюйма, а міжнародний дюйм – точно 25.4 мм, тому 1 mil = 0.0254 мм.[^nist-inch] Для перетворення множте кількість mil на 0.0254; наприклад, 25 mil = 0.635 мм.

## Detailed explanation

Один mil дорівнює одній тисячній міжнародного дюйма, тобто рівно 0.0254 мм; щоб перевести mil у міліметри, значення множать на 0.0254.[^nist-inch] Тут mil – одиниця довжини, а не міліметр і не мілілітр.

Міжнародний дюйм визначений точно як 25.4 мм. Оскільки один mil – це 0.001 дюйма, множення дає 0.001 × 25.4 мм = 0.0254 мм. Зворотне перетворення ділить значення в міліметрах на 0.0254. В електроніці mil часто трапляється у ширині доріжок і відстанях між виводами, тоді як креслення можуть задавати ті самі розміри в міліметрах.[^nist-inch]

Приклад: 25 mil × 0.0254 мм/mil = 0.635 мм. Отже, доріжка шириною 25 mil має ширину 0.635 мм. Це точне перетворення одиниць; допуски виробництва враховуються окремо.[^nist-inch]

**Типові помилки:**

- плутати mil з millimeter; один mil дорівнює лише 0.0254 мм;
- використовувати коефіцієнт 25.4 замість 0.0254 при множенні mil;
- плутати mil із позначенням міліметра в документації.

Перед розрахунком перевірте початкові одиниці. Наприклад, 10 mil – це 0.254 мм, а 10 мм – приблизно 393.7 mil. Така перевірка запобігає помилці у тисячу разів через плутанину між mil і дюймом.[^nist-inch]

## Sources

<!-- generated from frontmatter -->
