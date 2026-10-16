---
id: emb-eldig-0014
title: "Як розраховується сумарна затримка поширення сигналу в багатокаскадній комбінаційній схемі?"
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

Затримка комбінаційної мережі дорівнює сумі затримок поширення всіх послідовних каскадів логічних вентилів уздовж найдовшого шляху. Якщо сигнал проходить через вентиль із затримкою 15 нс, а потім через вентиль із затримкою 10 нс, сумарний час формування результату становить приблизно 25 нс. Цей час визначає мінімальний інтервал між зміною входів і стабільністю вихідних даних.[^udemy-electronics-course]

## Detailed explanation

TODO
