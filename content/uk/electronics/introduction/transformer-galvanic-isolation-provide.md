---
id: emb-elintro-0159
title: "Що дає гальванічна ізоляція трансформатора?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: aac-transformer-isolation
    title: "All About Circuits: Transformer Isolation"
    url: https://www.allaboutcircuits.com/technical-articles/transformer-isolation/
---

## Short answer

Між окремими первинною та вторинною обмотками немає прямого провідного шляху: енергія передається магнітним зв’язком.[^aac-transformer-isolation] Це може розірвати ground loop і зменшити ризик ураження, але безпека залежить від ізоляційних номіналів, конструкції та підключень системи.[^aac-transformer-isolation]

## Detailed explanation

Гальванічна ізоляція трансформатора означає, що первинна й вторинна обмотки не з’єднані прямим провідником. Енергія переходить між ними через змінний магнітний потік в осерді, а не через спільний провідний шлях між колами.[^aac-transformer-isolation]

Такий поділ дає змогу живити вторинне коло без спільної точки землі з первинним. Це корисно, наприклад, щоб уникнути небажаного ground loop або відокремити вимірювальне коло від іншого кола, яке має спільну землю.[^aac-transformer-isolation] Гальванічна ізоляція не означає, що сигнал чи енергія взагалі не проходять: вони передаються через магнітне поле, а трансформатор може одночасно змінювати рівень AC-напруги.

Ізоляція не гарантує автоматичного захисту від будь-якого ураження струмом. Вторинна сторона лишається електрично активною, а її напруга може бути небезпечною відносно землі чи між контактами; пробій, неправильне підключення або інший провідний зв’язок можуть зруйнувати очікуваний поділ.[^aac-transformer-isolation] Для захисної функції важливі відповідні ізоляційні проміжки, матеріали, робоча напруга та категорія застосування конкретного пристрою.

**Типова помилка:** вважати, що будь-який трансформатор автоматично забезпечує безпеку. Автотрансформатор має спільну обмотку для входу й виходу, отже не створює такого самого гальванічного розділення, як трансформатор з окремими обмотками.[^aac-transformer-isolation]

Практично треба перевіряти схему та документацію компонента, а не покладатися лише на слово «трансформатор» у назві. Якщо вторинну сторону додатково з’єднати з первинною через землю, екран, вимірювальний прилад або інше коло, цей шлях може змінити ізоляційну поведінку всієї системи.[^aac-transformer-isolation]
