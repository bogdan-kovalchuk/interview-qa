---
id: emb-eldig-0020
title: "Яка послідовність сигналів потрібна для коректного циклу запису в мікросхему статичної пам'яті (SRAM)?"
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

Спершу на шині встановлюється стабільна адреса комірки пам'яті. Потім активуються сигнал вибору кристала /CE (/CS) та строб запису /WE, а дані виставляються на двонаправлену шину. Шина даних має утримуватися стабільною протягом визначеного вікна встановлення до закінчення імпульсу запису, після чого строб знімається.[^udemy-electronics-course]

## Detailed explanation

TODO
