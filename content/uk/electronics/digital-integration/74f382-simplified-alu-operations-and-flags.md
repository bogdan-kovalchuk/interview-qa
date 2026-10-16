---
id: emb-elinteg-0052
title: "Які базові операції та статусні прапорці підтримує спрощене 4-бітне АЛП 74F382?"
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

Мікросхема 74F382 містить три адресні входи S2–S0, які кодують вісім найбільш затребуваних операцій: очищення (0), віднімання B – A, віднімання A – B, додавання A + B, а також побітові XOR, OR, AND та встановлення всіх одиниць. Окрім результату F3–F0, схема формує вихідні прапорці перенесення <span class="formula">\(C_{n+4}\)</span> та арифметичного переповнення знакового розряду OVR.[^udemy-electronics-course]

## Detailed explanation

TODO
