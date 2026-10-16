---
id: emb-eldig-0034
title: "Чому невикористані входи мікросхем CMOS не можна залишати непідключеними (floating)?"
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

Входи польових транзисторів мають величезний опір і поводяться як антени, вловлюючи паразитні наведення. Плаваючий потенціал може потрапити в проміжну лінійну зону між 0 і 1, відкривши обидва комплементарні транзистори одночасно. Це викликає наскрізний струм короткого замикання через живлення, перегрів і вихід мікросхеми з ладу; тому входи з'єднують із VCC або GND.[^udemy-electronics-course]

## Detailed explanation

TODO
