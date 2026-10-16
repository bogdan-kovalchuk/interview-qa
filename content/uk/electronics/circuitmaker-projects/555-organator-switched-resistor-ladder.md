---
id: emb-elcmproj-0036
title: "Як комутація ланцюжка резисторів у схемі генератора 555 формує звуковий ряд клавіатури?"
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

У таймері 555 частота прямо залежить від величини опору в ланцюзі скидання: <span class="formula">\(f \approx 1{,}44 / ((R_A + 2R_B)\,C)\)</span>. Кожна клавішна кнопка підключає свій прецизійний резистор <span class="formula">\(R_B\)</span>, задаючи точний час заряду конденсатора. Одночасне натискання кількох кнопок створює паралельне з’єднання резисторів, підвищуючи тон.[^udemy-electronics-course]

## Detailed explanation

TODO
