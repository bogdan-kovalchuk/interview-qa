---
id: emb-elcmproj-0035
title: "Як рівномірно темперована шкала визначає співвідношення частот сусідніх нот у музичному синтезаторі?"
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

У 12-ступеневій темперованій системі частота кожного наступного півтону зростає в однакове геометричне співвідношення: <span class="formula">\(f_{n+1} = f_n \cdot \sqrt[12]{2} \approx f_n \cdot 1{,}05946\)</span>. Повний інтервал октави з дванадцяти півтонів подвоює вихідну частоту звуку. Розрахунок точних номіналів резисторів у схемі спирається на цей логарифмічний розподіл.[^udemy-electronics-course]

## Detailed explanation

TODO
