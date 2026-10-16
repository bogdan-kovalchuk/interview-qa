---
id: emb-elcmproj-0016
title: "Чому біля кожного корпусу цифрової мікросхеми обов’язково ставлять керамічний конденсатор 0,1 мкФ?"
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

Під час логічного перемикання цифрові мікросхеми створюють короткі високочастотні імпульси струму споживання. Індуктивність доріжок живлення викликає паразитне просідання напруги та взаємні збої сусідніх мікросхем. Керамічний конденсатор упритул до виводів живлення служить джерелом локального заряду, шунтуючи перешкоди.[^udemy-electronics-course]

## Detailed explanation

TODO
