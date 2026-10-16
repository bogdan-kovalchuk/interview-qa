---
id: emb-elinteg-0053
title: "Як за допомогою логічних вентилів OR перетворити вісім окремих кнопок на 3-бітний код команди для АЛП?"
track: electronics
section: digital-integration
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
---

## Short answer

Кожна кнопка відповідає одній математичній операції, генеруючи рівень 1 при натисканні. Кожен розряд вихідного коду S0, S1, S2 формується вентилем OR, на входи якого підключаються лише ті кнопки, у двійковому номері яких відповідний розряд дорівнює 1. Наприклад, біт S0 формується об'єднанням кнопок із непарними кодами 1, 3, 5 та 7.[^udemy-electronics-course]

## Detailed explanation

TODO
