---
id: emb-elcmproj-0019
title: "Яку роль відіграє Engineering Change Order при синхронізації змін між схемою та платою?"
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

Механізм ECO зіставляє електричний netlist схеми з поточним станом розводки у документі друкованої плати. Він формує перелік точкових дій: додавання компонентів, оновлення footprint та перепризначення змінених ланцюгів. Це дозволяє гнучко переносити схемні правки на плату без видалення готових трас.[^udemy-electronics-course]

## Detailed explanation

TODO
