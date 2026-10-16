---
id: emb-eldig-0005
title: "Як вентиль AND використовується в ролі керованого ключа (gate) для проходження сигналу?"
track: electronics
section: digital-logic
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
---

## Short answer

Вентиль AND підпорядковується законам множення <span class="formula">\(X \cdot 1 = X\)</span> та <span class="formula">\(X \cdot 0 = 0\)</span>. Якщо подати сигнал на один вхід, а сигнал дозволу (enable) на інший, за рівня 1 сигнал проходить на вихід без змін. Подання рівня 0 примусово блокує вихід, утримуючи на ньому логічний 0.[^udemy-electronics-course]

## Detailed explanation

TODO
