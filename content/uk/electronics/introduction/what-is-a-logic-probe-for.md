---
id: emb-elintro-0267
title: "Для чого потрібен логічний пробник?"
description: "Для чого потрібен логічний пробник?"
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
    applicability: "Походження питання: лекція 24, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: tek-logic-probe
    title: "Tektronix: Logic Probe"
    url: https://www.tek.com/en/products/oscilloscopes/oscilloscope-probes/logic-probe
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Призначення логічного пробника для діагностики станів цифрових сигналів; це не гарантує вимірювання форми хвилі або відповідності будь-якій напрузі логічного рівня."
---

## Short answer

Він швидко допомагає перевірити, чи цифровий сигнал розпізнається як `HIGH` або `LOW`, і деякі моделі також виявляють імпульси.[^tek-logic-probe] Пороги розпізнавання та доступність індикації імпульсів залежать від пробника і сімейства логіки; для форми сигналу потрібен осцилограф.[^tek-logic-probe]

## Detailed explanation

Логічний пробник – це вимірювальний інструмент для швидкого визначення логічного стану цифрової лінії, зазвичай як `HIGH` або `LOW`. Його застосовують під час перевірки цифрових схем, зокрема TTL і CMOS, щоб з’ясувати, чи перемикається потрібний вузол або чи застряг він в одному стані.[^tek-logic-probe]

Пробник під’єднують до спільного reference/ground і живлення згідно з інструкцією саме до цієї моделі, а його вхід торкається потрібної сигнальної точки. Внутрішній вхідний каскад порівнює напругу з порогами логічних рівнів, після чого світлодіод, звуковий індикатор або дисплей показує розпізнаний стан. У проміжній зоні між гарантованими `LOW` і `HIGH` результат може бути невизначеним або нестабільним; пороги не є універсальними для TTL та CMOS.[^tek-logic-probe]

Приклад: якщо вихід логічного елемента має залишатися `HIGH`, але пробник показує `LOW`, це підказує перевірити живлення елемента, його вхідні сигнали, з’єднання та коротке замикання виходу. Деякі пробники мають окрему індикацію переходів або імпульсів, але короткий імпульс може бути пропущений залежно від смуги пропускання та способу відображення. Звичайна проста індикація рівня не показує точну амплітуду, тривалість фронту чи форму хвилі.[^tek-logic-probe]

**Типові помилки:**

- Вважати, що `HIGH` завжди дорівнює певній напрузі на кшталт 5 V: поріг визначає сумісність пробника з логічним сімейством.
- Використовувати пробник як заміну осцилографу, коли важливі амплітуда, шум, час фронту чи ширина імпульсу.
- Забути про спільну землю або дозволену вхідну напругу, визначену інструкцією приладу.

## Sources

<!-- generated from frontmatter -->
