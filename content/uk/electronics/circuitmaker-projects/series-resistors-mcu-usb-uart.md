---
id: emb-elcmproj-0054
title: "Навіщо між мікроконтролером і мостом USB-UART послідовно встановлюють резистори 1 кОм?"
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

Резистори 1 кОм обмежують наскрізний струм при конфлікті передавачів або замиканні сигнальних ліній шини UART. Вони також дозволяють зовнішньому адаптеру або щиту перехоплювати лінії без відпаювання мікросхеми моста. Додатково опір гасить паразитний брязкіт імпульсів на крутих фронтах сигналів.[^udemy-electronics-course]

## Detailed explanation

TODO
