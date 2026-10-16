---
id: emb-elcmproj-0049
title: "Чому зворотний шлях струму динаміка відокремлюють від земляного контуру генератора 555?"
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

Потужні імпульсні струми навантаження динаміка викликають спади напруги на омічному опорі земляних провідників. Якщо цей струм проходить через спільну земляну шину таймера, виникає паразитний зворотний зв’язок. Це призводить до плавання висоти звуку, хрипів та низькочастотного самозбудження генератора.[^udemy-electronics-course]

## Detailed explanation

TODO
