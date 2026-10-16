---
id: emb-elintro-0226
title: "Чим відрізняється LED в емітерній гілці від LED у колекторній гілці?"
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
---

## Short answer

У колекторній схемі NPN керує струмом LED як низькобічний ключ; LED в емітері працює з emitter follower, де напруга емітера залежить від бази та струму навантаження. В обох випадках потрібен послідовний резистор для обмеження струму LED.[^aac-semiconductors]

## Detailed explanation

LED у колекторній гілці під’єднують послідовно з обмежувальним резистором між живленням і колектором NPN; емітер заземлюють, а базу керують через резистор. Коли транзистор переходить у насичення, він стягує колектор до низької напруги, на LED і резисторі з’являється майже вся напруга живлення, тож LED світиться. Коли транзистор закритий, струм колектора малий і LED гасне. Це перемикач із низьким боком, а не гарантія ідеального нуля: насичений транзистор має ненульову напругу `V_CE(sat)`.[^aac-semiconductors]

Якщо поставити LED і резистор у емітерну гілку, струм емітера проходить через навантаження, а напруга емітера слідує за напругою бази приблизно на величину `V_BE`. Це emitter follower: вихід не стягується до землі, а керування навантаженням залежить від базового сигналу, струму та характеристик транзистора. Світіння в цій схемі також залежить від полярності LED, його прямої напруги й наявності обмеження струму; сама назва гілки не задає стан «увімкнено».[^aac-semiconductors]

Приклад: якщо емітерний вузол без навантаження має близько `0.7 V`, LED із прямою напругою понад цю величину може майже не проводити, хоча база вже керується. У колекторній схемі струм визначається живленням, прямою напругою LED, резистором і `V_CE(sat)`. Типова помилка – під’єднати LED без послідовного резистора або назвати різницю лише інверсією логіки, не вказавши топологію та полярність.[^aac-semiconductors]
