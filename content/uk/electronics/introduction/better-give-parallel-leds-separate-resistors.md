---
id: emb-elintro-0122
title: "Чому паралельним LED краще давати окремі резистори?"
description: "Чому паралельним LED краще давати окремі резистори?"
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
    applicability: "Походження питання: лекція 12, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
---

## Short answer

Навіть однакові LED мають розкид `V_f`, тому при паралельному підключенні струм може розподілитися нерівномірно. Окремий послідовний резистор у кожній гілці допомагає обмежити та вирівняти струм; для точного керування можна використати constant-current driver.[^aac-direct-current] Нагрівання може знижувати `V_f`, але саме по собі не означає неминучий thermal runaway: результат залежить від схеми та тепловідведення.[^aac-semiconductors]

## Detailed explanation

У паралельному з’єднанні на кожному LED майже однакова напруга, але їхні вольт-амперні характеристики та `V_f` не ідентичні. Через круту характеристику діода навіть невелика різниця прямої напруги може спричинити різницю струмів. LED із нижчим `V_f` може забирати більшу частину струму, тоді як інша гілка світитиме слабше.[^aac-semiconductors]

Окремий резистор у кожній гілці створює локальний негативний зворотний зв’язок: зі зростанням струму збільшується спад напруги на резисторі, що стримує подальше зростання. Один спільний резистор обмежує лише сумарний струм і не гарантує його розподілу між LED.[^aac-direct-current] Кожен резистор розраховують для відповідної напруги живлення, `V_f` та цільового струму, а потім перевіряють допуск і потужність.

Приклад: для двох гілок із джерелом 5 V, LED із приблизним `V_f = 2 V` і струмом 10 mA у кожній потрібні окремі резистори `R = (5 V - 2 V)/0.01 A = 300 Ω`. Спільний резистор 150 Ω дасть 20 mA сумарно лише за ідеально однакових компонентів, але не врівноважить різницю характеристик.

**Типова помилка:** вважати, що однакова напруга на паралельних LED означає однаковий струм. У послідовному ланцюжку струм однаковий через кожен компонент, а паралельні гілки потребують власного обмеження або окремих регульованих виходів.[^aac-semiconductors]

## Sources

<!-- generated from frontmatter -->
