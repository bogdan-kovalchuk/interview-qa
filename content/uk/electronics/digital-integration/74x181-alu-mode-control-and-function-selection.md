---
id: emb-elinteg-0049
title: "Як здійснюється вибір між логічними та арифметичними функціями в мікросхемі АЛП 74x181?"
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

Вибір режиму роботи 74x181 визначається керуючим входом M: коли M = 1 (HIGH), блок виконує одну з 16 побітових логічних функцій без участі внутрішнього перенесення. Коли M = 0 (LOW), схема виконує одну з 16 арифметичних операцій з урахуванням перенесення. Конкретна операція всередині обраного режиму кодується 4-бітним словом на селекторних входах S3–S0.[^udemy-electronics-course]

## Detailed explanation

TODO
