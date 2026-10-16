---
id: emb-elcmproj-0006
title: "Чому цифрову схему на серії 74HC можна живити від трьох батарейок без стабілізатора?"
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

Логічні мікросхеми серії 74HC стабільно працюють у широкому діапазоні живильної напруги від <span class="formula">\(2{,}0\ \text{В}\)</span> до <span class="formula">\(6{,}0\ \text{В}\)</span>. Три свіжі батарейки AAA забезпечують <span class="formula">\(4{,}5\ \text{В}\)</span>, спадаючи при розряджанні до безпечних <span class="formula">\(3{,}0\ \text{В}\)</span>. Відмова від стабілізатора усуває падіння напруги й береже заряд.[^udemy-electronics-course]

## Detailed explanation

TODO
