---
id: emb-elcmproj-0037
title: "Чому для живлення схеми від 9-вольтової батареї потрібен стабілізатор LDO замість LM7805?"
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

Класичний лінійний регулятор LM7805 вимагає різниці напруг між входом і виходом не менше <span class="formula">\(2{,}0\text{–}2{,}5\ \text{В}\)</span>. Стабілізатор LDO з падінням всього <span class="formula">\(0{,}65\ \text{В}\)</span> підтримує вихідні <span class="formula">\(5\ \text{В}\)</span> при розряді батареї аж до <span class="formula">\(5{,}65\ \text{В}\)</span>. Це дозволяє корисно вичерпати майже всю енергію джерела живлення.[^udemy-electronics-course]

## Detailed explanation

TODO
