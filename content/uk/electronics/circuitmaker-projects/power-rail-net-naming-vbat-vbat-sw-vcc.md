---
id: emb-elcmproj-0039
title: "Навіщо ланцюгам живлення батарейного пристрою дають різні імена VBAT, VBAT_SW і VCC?"
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

Роздільні назви ланцюгів запобігають випадковому помилковому об’єднанню ділянок живлення в один провідний netlist. Позначення VBAT належить прямим виводам батареї, VBAT_SW – колу після вимикача, а VCC – виходу стабілізатора напруги. Це ізолює вузли комутації й гарантує коректне трасування провідників.[^udemy-electronics-course]

## Detailed explanation

TODO
