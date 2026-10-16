---
id: emb-elcmproj-0069
title: "Що задають формат координат і режим придушення нулів у файлах Gerber і свердління NC Drill?"
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

Формат координат (наприклад, 2:4 у дюймах) визначає кількість розрядів, задаючи точність позиціонування <span class="formula">\(0{,}1\ \text{mil}\)</span>. Придушення нулів leading або trailing стискає текстовий файл числових векторів. Розбіжність налаштувань між САПР і CAM-системою призводить до масштабного спотворення розмірів або зсуву отворів.[^udemy-electronics-course]

## Detailed explanation

TODO
