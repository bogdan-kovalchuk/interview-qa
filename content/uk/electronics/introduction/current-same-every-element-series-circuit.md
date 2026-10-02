---
id: emb-elintro-0103
title: "Чому струм однаковий у всіх елементах послідовного кола?"
description: "Чому струм однаковий у всіх елементах послідовного кола?"
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

У послідовному колі струм однаковий у кожному елементі, бо між ними є лише один шлях для руху заряду. За законом збереження заряду заряд не накопичується в проміжних вузлах у сталому режимі, тому за однаковий час через кожен елемент проходить однакова кількість заряду.[^aac-series-circuits]

## Detailed explanation

Послідовним називають з’єднання, у якому елементи утворюють один неперервний шлях без розгалужень. Струм показує, скільки заряду проходить через переріз провідника за одиницю часу. Якби через один елемент надходило більше заряду, ніж виходило до наступного, заряд накопичувався б на з’єднанні; у сталому режимі цього не відбувається. Тому струм перед і після кожного елемента однаковий, хоча напруга на елементах може відрізнятися.[^aac-series-circuits]

Це також видно із закону Кірхгофа для струмів: у вузлі алгебраїчна сума струмів дорівнює нулю. Для вузла послідовного кола, до якого входить один елемент і виходить інший, струм, що входить, мусить дорівнювати струму, що виходить. Повторивши це для кожного з’єднання, отримуємо однаковий струм у всьому колі. Правило стосується будь-яких компонентів, з’єднаних послідовно, а не лише резисторів.[^aac-series-circuits]

**Типові помилки:**
- Однаковий струм не означає однакову напругу. На резисторах із різними опорами падіння відрізняються відповідно до закону Ома.
- Якщо в колі є вузол, де струм може розділитися на гілки, усе коло вже не є одним послідовним шляхом. Струми гілок можуть відрізнятися, а їхня сума дорівнює струму до розгалуження.
- Перевіряйте з’єднання за схемою, а не лише за розташуванням компонентів на макетній платі: внутрішні контакти можуть створити паралельні гілки або коротке замикання.[^aac-series-circuits]

## Sources

<!-- generated from frontmatter -->
