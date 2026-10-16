---
id: emb-elcmproj-0057
title: "Як конденсатор 0,1 мкФ у колі DTR забезпечує автоматичне скидання мікроконтролера при прошивці?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
---

## Short answer

Коли комп’ютер відкриває COM-порт, лінія DTR переходить у нуль і залишається низькою весь час обміну. Послідовний конденсатор разом із підтяжкою лінії RESET утворює диференціюючий RC-ланцюг. Він генерує короткий негативний імпульс скидання, запускаючи завантажувач у потрібний момент.[^udemy-electronics-course]

## Detailed explanation

TODO
