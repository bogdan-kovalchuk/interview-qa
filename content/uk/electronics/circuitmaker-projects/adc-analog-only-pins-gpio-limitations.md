---
id: emb-elcmproj-0060
title: "Чому виводи ADC6 і ADC7 мікроконтролера ATmega328P не можна використовувати для керування світлодіодами?"
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

В архітектурі ATmega328P у корпусі TQFP-32 виводи ADC6 і ADC7 є виключно аналоговими входами мультиплексора. Вони апаратно позбавлені цифрових вихідних транзисторів і регістрів керування портом GPIO. Спроба сконфігурувати їх на вихід не працюватиме, тому світлодіоди підключають до інших ліній.[^udemy-electronics-course]

## Detailed explanation

TODO
