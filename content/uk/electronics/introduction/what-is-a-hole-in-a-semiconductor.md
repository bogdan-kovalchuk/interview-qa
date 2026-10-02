---
id: emb-elintro-0035
title: "Що таке \"дірка\" у напівпровіднику?"
description: "Що таке \"дірка\" у напівпровіднику?"
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
    applicability: "Походження питання: лекція 5, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-electrons-and-holes
    title: "All About Circuits: Electrons and Holes"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-2/electrons-and-holes/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює електронно-діркові пари та ефективний рух дірок у напівпровіднику; охоплює якісну модель, а не повний квантовий опис."
---

## Short answer

Дірка – незаповнений стан у валентній зоні, який у моделі напівпровідника поводиться як рухливий носій із зарядом `+e`. Її видимий рух протилежний переходам електронів, що заповнюють сусідні незайняті стани.[^aac-electrons-and-holes]

## Detailed explanation

Дірка – це відсутність електрона в доступному валентному стані кристала, яку зручно описувати як рухомий носій із позитивним зарядом.[^aac-semiconductors]

У ковалентному кристалі, наприклад кремнії, валентні електрони беруть участь у зв’язках і займають стани валентної зони. Якщо електрон отримує достатньо енергії й переходить до стану провідності, у валентній зоні лишається незаповнений стан. Електрон із сусіднього зв’язку може перейти на це місце, залишивши нове незаповнене місце позаду; повторення таких переходів створює ефективне переміщення дірки через кристал.[^aac-electrons-and-holes]

Дірка не є окремим протоном чи частинкою, що фізично рухається між атомами: це квазічастинка, тобто корисний опис колективного руху електронів. Вона має ефективний позитивний заряд `+e`, а відповідний електронний рух має протилежний напрямок. У p-типі акцепторне легування сприяє появі дірок; у такому матеріалі вони є основними носіями, хоча електрони також можуть переносити заряд як неосновні носії.[^aac-electrons-and-holes][^aac-semiconductors]

Приклад: у ланцюжку сусідніх зв’язків нехай електрон щоразу переходить на порожнє місце ліворуч. Після кожного переходу вакансія лишається праворуч від попереднього місця, отже послідовність електронних переходів відповідає руху дірки праворуч. Такий опис спрощує аналіз струму й p-n переходів: можна відстежувати позитивний носій, не стверджуючи, що в кристалі рухається окрема позитивна частинка.[^aac-electrons-and-holes]

## Sources

<!-- generated from frontmatter -->
