---
id: emb-elintro-0238
title: "Що означає N-канальний MOSFET?"
description: "Що означає N-канальний MOSFET?"
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
    applicability: "Походження питання: лекція 22, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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

N-channel MOSFET формує канал, у якому основними носіями заряду є електрони. Для типового enhancement-приладу потрібна достатньо позитивна напруга gate відносно source, але підключення source до нижчого потенціалу – поширена схема, а не визначення N-канального типу.[^aac-semiconductors]

## Detailed explanation

Назва N-channel описує тип каналу та основних носіїв заряду: у провідному каналі такого MOSFET струм переноситься електронами. У типовому enhancement-приладі канал не є повністю сформованим за нульової напруги gate-source. Достатньо позитивне `V_GS` притягує електрони до ділянки під ізоляційним шаром і створює провідний шлях між source та drain.[^aac-semiconductors]

Це не означає, що source завжди має бути під’єднаний до землі або до найнижчого потенціалу в усіх схемах. Важлива напруга gate відносно source, а не відносно землі: якщо потенціал source змінюється, змінюється і потрібний потенціал gate. Для N-channel depletion-приладу поведінка за нульового `V_GS` буде іншою, тому слово «N-channel» саме по собі не визначає нормально вимкнений стан.[^aac-semiconductors]

У типовому низькобічному ключі source з’єднують із низьким потенціалом, навантаження ставлять між живленням і drain, а gate піднімають вище source. Електрони рухаються в каналі від source до drain за умовами поля та прикладених напруг; умовний напрямок струму протилежний руху електронів. У високобічних схемах source може перебувати біля шини живлення, тож простого логічного рівня відносно землі може бути недостатньо.[^aac-semiconductors]

**Типові помилки:**
- Визначати N-channel лише як «source обов’язково на землі».
- Плутати напрямок руху електронів із напрямком умовного струму.
- Припускати, що всі MOSFET є enhancement-приладами.

## Sources

<!-- generated from frontmatter -->
