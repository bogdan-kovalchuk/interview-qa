---
id: emb-elcmproj-0015
title: "Що необхідно робити з входами невикористаної половини мікросхеми КМОН-лічильника 74HC393?"
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

Вхідні каскади КМОН мають колосальний вхідний опір і легко вловлюють електростатичні перешкоди з навколишнього середовища. Вільний вхід зміщується в проміжну зону, викликаючи відкриття обох транзисторів і наскрізні струми споживання. Для запобігання паразитній генерації всі вільні входи жорстко садять на землю.[^udemy-electronics-course]

## Detailed explanation

TODO
