---
id: emb-elintro-0226
title: "Чим відрізняється LED в емітерній гілці від LED у колекторній гілці?"
description: "Чим відрізняється LED в емітерній гілці від LED у колекторній гілці?"
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
    applicability: "Походження питання: лекція 21, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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

У колекторній схемі NPN керує струмом LED як низькобічний ключ; LED в емітері працює з emitter follower, де напруга емітера залежить від бази та струму навантаження. В обох випадках потрібен послідовний резистор для обмеження струму LED.[^aac-semiconductors]

## Detailed explanation

LED у колекторній гілці під’єднують послідовно з обмежувальним резистором між живленням і колектором NPN; емітер заземлюють, а базу керують через резистор. Коли транзистор переходить у насичення, він стягує колектор до низької напруги, на LED і резисторі з’являється майже вся напруга живлення, тож LED світиться. Коли транзистор закритий, струм колектора малий і LED гасне. Це перемикач із низьким боком, а не гарантія ідеального нуля: насичений транзистор має ненульову напругу `V_CE(sat)`.[^aac-semiconductors]

Якщо поставити LED і резистор у емітерну гілку, струм емітера проходить через навантаження, а напруга емітера слідує за напругою бази приблизно на величину `V_BE`. Це emitter follower: вихід не стягується до землі, а керування навантаженням залежить від базового сигналу, струму та характеристик транзистора. Світіння в цій схемі також залежить від полярності LED, його прямої напруги й наявності обмеження струму; сама назва гілки не задає стан «увімкнено».[^aac-semiconductors]

Приклад: якщо емітерний вузол без навантаження має близько `0.7 V`, LED із прямою напругою понад цю величину може майже не проводити, хоча база вже керується. У колекторній схемі струм визначається живленням, прямою напругою LED, резистором і `V_CE(sat)`. Типова помилка – під’єднати LED без послідовного резистора або назвати різницю лише інверсією логіки, не вказавши топологію та полярність.[^aac-semiconductors]

## Sources

<!-- generated from frontmatter -->
