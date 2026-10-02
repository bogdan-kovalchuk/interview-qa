---
id: emb-elintro-0101
title: "Формула загального опору для послідовних резисторів?"
description: "Формула загального опору для послідовних резисторів?"
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
    applicability: "Походження питання: лекція 11, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-series-circuits
    title: "All About Circuits: Series Circuits and the Application of Ohm’s Law"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-5/simple-series-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтверджує правила послідовних кіл; числа залежать від заданих номіналів."
---

## Short answer

Еквівалентний опір послідовно з’єднаних резисторів дорівнює сумі їхніх опорів: `R_total = R_1 + R_2 + ... + R_n`. Через усі елементи такого кола тече однаковий струм, бо для нього є лише один шлях.[^aac-series-circuits]

## Detailed explanation

Еквівалентний опір замінює кілька послідовно з’єднаних резисторів одним резистором, який має таке саме співвідношення між загальною напругою та струмом кола. У послідовному з’єднанні вихід одного резистора з’єднаний із входом наступного, тому струм не має альтернативної гілки. За законом Кірхгофа напруга джерела дорівнює сумі падінь напруги на елементах; оскільки струм однаковий, закон Ома для кожного резистора дає `V_total = I*R_1 + I*R_2 + ...`. Винесення спільного струму показує, що `R_total = R_1 + R_2 + ... + R_n`.[^aac-series-circuits]

Наприклад, якщо послідовно з’єднати резистори 100 Ω і 330 Ω, еквівалентний опір становитиме `R_total = 100 Ω + 330 Ω = 430 Ω`. За джерела 3 V це відповідає струму `I = 3 V/430 Ω ≈ 6.98 mA` для ідеального джерела та номінальних значень резисторів. Падіння напруги на кожному елементі різне: більший опір за того самого струму має більше падіння, а сума падінь дорівнює напрузі джерела.[^aac-series-circuits]

**Типові помилки:**
- Не застосовуйте суму опорів до паралельного з’єднання: там резистори мають спільні два вузли, а струм розгалужується.
- Не додавайте номінали, якщо між елементами є відгалуження або інші з’єднання, що створюють додатковий шлях. Спершу визначте топологію кола.
- Формула описує базову модель; опір проводів, допуски компонентів і нагрів можуть вплинути на виміряний результат.[^aac-series-circuits]

## Sources

<!-- generated from frontmatter -->
