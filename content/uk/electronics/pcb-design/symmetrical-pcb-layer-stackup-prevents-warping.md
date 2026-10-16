---
id: emb-elpcb-0015
title: "Чому стек шарів друкованої плати має бути симетричним і містити парну кількість шарів?"
track: electronics
section: pcb-design
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
---

## Short answer

Плати виготовляють із парною кількістю шарів (2, 4, 6, 8), симетрично розташованих відносно центру, для запобігання деформаціям (вигину та скручуванню). Несиметричний розподіл шарів міді або непарна кількість шарів створюють різницю коефіцієнтів теплового розширення й механічних напружень при гарячому пресуванні та паянні. Це призводить до короблення плати, через що компоненти поверхневого монтажу тріскаються або відриваються від площадок.[^udemy-electronics-course]

## Detailed explanation

TODO
