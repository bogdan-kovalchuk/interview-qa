---
id: emb-elintro-0031
title: "Що таке конвенційний струм і чим він відрізняється від руху електронів?"
description: "Що таке конвенційний струм і чим він відрізняється від руху електронів?"
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
  - source_id: aac-conventional-electron-flow
    title: "All About Circuits: Conventional Versus Electron Flow"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-1/conventional-versus-electron-flow/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює conventional flow як напрямок позитивного заряду, протилежність electron flow у металі та застосування домовленості в аналізі кіл."
---

## Short answer

У металевому провіднику електрони дрейфують проти conventional current: цей напрямок визначено так, ніби рухається позитивний заряд. Обидві домовленості дають узгоджений аналіз кола, якщо не змінювати її посеред розрахунку; у схемах зазвичай використовують conventional current.[^aac-conventional-electron-flow]

## Detailed explanation

Conventional current – це умовний напрямок струму, у якому рухався б позитивний заряд; у металевому дроті електрони рухаються в протилежний бік.[^aac-direct-current]

Знак струму задає домовленість, а не траєкторію конкретних носіїв. Для заряду `q` рух зі швидкістю в один бік дає внесок у conventional current відповідно до знака `q`: для електрона він має протилежний напрямок, а для позитивного носія – той самий. Тому визначення через позитивний заряд працює і в середовищах, де носіями є не тільки електрони.[^aac-conventional-electron-flow][^aac-semiconductors]

У розрахунку гілки довільно задають стрілку струму, а потім послідовно застосовують закон Ома й закони Кірхгофа до обраних знаків напруги та струму. Від’ємна відповідь означає, що реальний conventional current іде проти стрілки; це не означає, що розрахунок зламався. Перехід на electron flow вимагав би узгоджено переосмислити напрямки в усіх позначеннях, тому зазвичай це лише додає плутанини.[^aac-conventional-electron-flow]

Приклад: якщо в зовнішній гілці батареї умовно позначити струм від плюсового виводу до мінусового, електрони в металевому дроті дрейфуватимуть у зворотному напрямку. У розчині струм можуть переносити іони обох знаків, а в напівпровіднику – електрони й дірки; conventional current описує сумарний напрямок перенесення заряду, а не рух одного наперед визначеного виду частинок.[^aac-conventional-electron-flow][^aac-semiconductors]

## Sources

<!-- generated from frontmatter -->
