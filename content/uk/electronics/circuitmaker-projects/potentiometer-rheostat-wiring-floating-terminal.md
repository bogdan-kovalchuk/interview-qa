---
id: emb-elcmproj-0014
title: "Чому вільний крайній вивід підлаштовного потенціометра обов’язково з’єднують із повзунком?"
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

Якщо залишити вільний вивід резистивної доріжки відкритим, будь-яка вібрація або окиснення повзунка викличе миттєвий обрив ланцюга. Схема генератора зафіксує нескінченний опір і тактування повністю зірветься. З’єднання повзунка з краєм обмежує опір аварійного розриву максимальним значенням номіналу.[^udemy-electronics-course]

## Detailed explanation

TODO
