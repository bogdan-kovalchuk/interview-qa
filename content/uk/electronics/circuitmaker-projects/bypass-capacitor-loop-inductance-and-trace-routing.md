---
id: emb-elcmproj-0034
title: "Чому провідник живлення повинен проходити через контакт блокувального конденсатора до виводу мікросхеми?"
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

Підключення конденсатора через довге бічне відгалуження збільшує паразитну індуктивність контуру фільтрації живлення. Прокладання траси живлення безпосередньо через площадку конденсатора змушує високочастотний шум замикатися на землю в точці входу. Це забезпечує ефективне фільтрування завад на виводі мікросхеми.[^udemy-electronics-course]

## Detailed explanation

TODO
