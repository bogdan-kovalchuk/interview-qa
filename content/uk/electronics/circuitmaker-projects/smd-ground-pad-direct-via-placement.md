---
id: emb-elcmproj-0065
title: "Чому біля земляної контактної площадки SMD-компонента необхідно ставити власне перехідне отвір?"
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

Довга доріжка до віддаленої точки заземлення має розподілену паразитну індуктивність. На високих частотах перемикання це викликає сплески напруги та локальне тремтіння земляного потенціалу під компонентом. Встановлення перехідного отвору поруч із площадкою спрямовує струм найкоротшим шляхом у суцільний опорний шар.[^udemy-electronics-course]

## Detailed explanation

TODO
