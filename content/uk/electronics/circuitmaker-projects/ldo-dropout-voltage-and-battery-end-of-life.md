---
id: emb-elcmproj-0038
title: "Як величина падіння напруги dropout voltage визначає термін служби батареї пристрою?"
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

Мінімальна вхідна напруга стабілізації визначається сумою: <span class="formula">\(V_{in(min)} = V_{out} + V_{DO}\)</span>. Зменшення величини <span class="formula">\(V_{DO}\)</span> дозволяє пристрою працювати на пологій ділянці розрядної характеристики батареї нижче 7 В. Літієва батарея типу Крона забезпечує значно стабільнішу напругу порівняно зі звичайною лужною.[^udemy-electronics-course]

## Detailed explanation

TODO
