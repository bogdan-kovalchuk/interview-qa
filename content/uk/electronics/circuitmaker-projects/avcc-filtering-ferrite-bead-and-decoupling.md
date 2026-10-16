---
id: emb-elcmproj-0055
title: "Чому лінію аналогового живлення AVCC мікроконтролера підключають через LC-фільтр?"
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

Комутація цифрових блоків ядра мікроконтролера створює значний високочастотний шум на загальній шині живлення VCC. Фільтр із феритової намистинки або дроселя <span class="formula">\(10\ \text{мкГн}\)</span> та конденсатора затримує ці перешкоди. Чисте живлення AVCC забезпечує високу точність і стабільність оцифрування аналогових сигналів.[^udemy-electronics-course]

## Detailed explanation

TODO
