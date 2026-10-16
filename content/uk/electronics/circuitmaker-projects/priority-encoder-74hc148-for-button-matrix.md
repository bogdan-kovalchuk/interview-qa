---
id: emb-elcmproj-0051
title: "Як пріоритетний шифратор 74HC148 оптимізує підключення восьми кнопок до мікроконтролера?"
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

Шифратор кодує вісім вхідних сигналів від кнопок у компактний 3-бітний двійковий код: <span class="formula">\(n = \lceil \log_2 8 \rceil = 3\)</span>. Це вивільняє п’ять цінних ліній порту вводу-виводу процесора для іншої периферії. Додатковий груповий вихід GS фіксує факт натискання будь-якої кнопки, формуючи переривання.[^udemy-electronics-course]

## Detailed explanation

TODO
