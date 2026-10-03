---
id: emb-elintro-0159
title: "Що дає гальванічна ізоляція трансформатора?"
description: "Що дає гальванічна ізоляція трансформатора?"
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
    applicability: "Походження питання: лекція 15, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-transformer-isolation
    title: "All About Circuits: Transformer Isolation"
    url: https://www.allaboutcircuits.com/technical-articles/transformer-isolation/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Відсутність прямого провідного шляху між окремими обмотками та приклади ізоляції; рівень безпеки визначають конструкція, номінали й зовнішні з’єднання."
---

## Short answer

Між окремими первинною та вторинною обмотками немає прямого провідного шляху: енергія передається магнітним зв’язком.[^aac-transformer-isolation] Це може розірвати ground loop і зменшити ризик ураження, але безпека залежить від ізоляційних номіналів, конструкції та підключень системи.[^aac-transformer-isolation]

## Detailed explanation

Гальванічна ізоляція трансформатора означає, що первинна й вторинна обмотки не з’єднані прямим провідником. Енергія переходить між ними через змінний магнітний потік в осерді, а не через спільний провідний шлях між колами.[^aac-transformer-isolation]

Такий поділ дає змогу живити вторинне коло без спільної точки землі з первинним. Це корисно, наприклад, щоб уникнути небажаного ground loop або відокремити вимірювальне коло від іншого кола, яке має спільну землю.[^aac-transformer-isolation] Гальванічна ізоляція не означає, що сигнал чи енергія взагалі не проходять: вони передаються через магнітне поле, а трансформатор може одночасно змінювати рівень AC-напруги.

Ізоляція не гарантує автоматичного захисту від будь-якого ураження струмом. Вторинна сторона лишається електрично активною, а її напруга може бути небезпечною відносно землі чи між контактами; пробій, неправильне підключення або інший провідний зв’язок можуть зруйнувати очікуваний поділ.[^aac-transformer-isolation] Для захисної функції важливі відповідні ізоляційні проміжки, матеріали, робоча напруга та категорія застосування конкретного пристрою.

**Типова помилка:** вважати, що будь-який трансформатор автоматично забезпечує безпеку. Автотрансформатор має спільну обмотку для входу й виходу, отже не створює такого самого гальванічного розділення, як трансформатор з окремими обмотками.[^aac-transformer-isolation]

Практично треба перевіряти схему та документацію компонента, а не покладатися лише на слово «трансформатор» у назві. Якщо вторинну сторону додатково з’єднати з первинною через землю, екран, вимірювальний прилад або інше коло, цей шлях може змінити ізоляційну поведінку всієї системи.[^aac-transformer-isolation]

## Sources

<!-- generated from frontmatter -->
