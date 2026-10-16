---
id: emb-elcmproj-0056
title: "Навіщо на платі залишають роз’єм ISP за наявності інтерфейсу завантаження через USB?"
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

Програмування через USB можливе лише після початкового запису спеціального коду bootloader у пам’ять мікроконтролера. Нові мікросхеми постачаються чистими й записуються виключно через інтерфейс SPI роз’єму ISP. Також цей роз’єм дозволяє конфігурувати fuse-біти та відновлювати процесор після збоїв.[^udemy-electronics-course]

## Detailed explanation

TODO
