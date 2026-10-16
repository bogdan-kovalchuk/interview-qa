---
id: emb-eldig-0013
title: "Навіщо в цифрових схемах потрібен тристабільний буфер і стан Hi-Z?"
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

Пряме з'єднання звичайних виходів призводить до короткого замикання, якщо один чіп видає 1, а інший 0. Тристабільний буфер має вхід дозволу (зазвичай активний низький /OE), за вимкнення якого вихід переходить у стан високого імпедансу Hi-Z. У стані Hi-Z опір виходу становить мегаоми, що дозволяє кільком мікросхемам почергово працювати на спільну шину даних.[^udemy-electronics-course]

## Detailed explanation

TODO
