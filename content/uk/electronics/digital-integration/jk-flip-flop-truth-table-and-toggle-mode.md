---
id: emb-elinteg-0062
title: "Які стани формує універсальний JK-тригер і чому режим J = 1, K = 1 є фундаментальним для лічильників?"
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

JK-тригер усуває заборонений стан SR-тригера: при J = 0, K = 0 стан зберігається, при 10 – встановлюється 1, при 01 – скидається в 0. Комбінація J = 1, K = 1 переводить тригер у режим лічильного перемикання (toggle), коли кожен тактовий імпульс інвертує вихід на протилежний. Завдяки цьому JK-тригер є ідеальним дільником частоти на 2 і базовою коміркою двійкових лічильників.[^udemy-electronics-course]

## Detailed explanation

TODO
