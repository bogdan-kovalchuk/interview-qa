---
id: emb-elcmproj-0005
title: "Чому катоди світлодіодів підключають до виходів дешифратора 74HC138, а аноди до живлення?"
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

Дешифратор 74HC138 має інверсні виходи з активним низьким рівнем напруги. При виборі адреси канал переходить у нуль і замикає втікаючий струм світлодіода на землю. Підключення анодів через резистори до шини живлення вмикає вибраний світлодіод саме при появі нуля.[^udemy-electronics-course]

## Detailed explanation

TODO
