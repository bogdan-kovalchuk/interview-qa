---
id: emb-eldig-0026
title: "Що відбувається під час переповнення розрядної сітки беззнакового додавання n-бітових чисел?"
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

Якщо результат додавання перевищує максимальне значення <span class="formula">\(2^n - 1\)</span>, виникає переповнення (overflow). Наприклад, додавання 1 до 8-бітного числа 255 (11111111₂) формує перенос у дев'ятий розряд, а в 8-бітному регістрі залишається 0. Біт переносу Carry Out втрачається або записується в прапорець процесора, а безпосередній результат спотворюється.[^udemy-electronics-course]

## Detailed explanation

TODO
