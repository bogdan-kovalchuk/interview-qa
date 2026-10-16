---
id: emb-elcmproj-0063
title: "Чому жоден із виводів динаміка з мостовим підсилювачем BTL не можна підключати до землі?"
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

У мостовому підсилювачі BTL обидва виводи динаміка підключені до активних протифазних виходів мікросхеми. Кожен контакт перебуває під постійною напругою зміщення на рівні половини живлення. Заземлення будь-якого контакту викликає пряме коротке замикання плеча підсилювача та миттєвий вихід мікросхеми з ладу.[^udemy-electronics-course]

## Detailed explanation

TODO
