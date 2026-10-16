---
id: emb-elinteg-0061
title: "Як двоступенева архітектура Master-Slave усуває явище перегонів в імпульсних тригерах?"
track: electronics
section: digital-integration
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
---

## Short answer

Конструкція Master-Slave складається з двох послідовних тригерів, тактованих протифазними тактовими сигналами. Поки тактовий імпульс високий, відкритий вхідний тригер Master, який фіксує значення входу, тоді як вихідний Slave заблокований. При переході такту в низький рівень Master від'єднується від входів, а Slave переписує зафіксований стан на вихід Q, унеможливлюючи наскрізне проходження перешкод.[^udemy-electronics-course]

## Detailed explanation

TODO
