---
id: emb-elcmproj-0052
title: "Чому напругу шини USB не можна розглядати як стабільне й прецизійне джерело 5,0 В?"
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

Специфікація USB допускає коливання напруги живлення в діапазоні від <span class="formula">\(4{,}75\ \text{В}\)</span> до <span class="formula">\(5{,}25\ \text{В}\)</span> зі значними пульсаціями. До того ж довгі кабелі створюють динамічні спади напруги під навантаженням. Для точних вимірювань вбудованим АЦП обов’язково використовують стабілізовані джерела опорної напруги.[^udemy-electronics-course]

## Detailed explanation

TODO
