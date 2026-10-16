---
id: emb-elcmproj-0004
title: "Як побудовано каскад керування світлодіодами у схемі бігучого вогника магічної палички?"
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

Генератор на таймері 555 виробляє тактові імпульси частотою кілька герц для двійкового лічильника 74HC393. Три старші біти лічильника надходять на входи дешифратора 74HC138, який по черзі активує один із восьми каналів. Активний низький рівень виходу запалює відповідний світлодіод, створюючи ефект вогника.[^udemy-electronics-course]

## Detailed explanation

TODO
