---
id: emb-elinteg-0039
title: "Як здійснюється керування напрямком і станом шини в двонапрямленому трансивері 74x245?"
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

Мікросхема 74x245 містить зустрічно-паралельні пари тристабільних буферів для кожної з 8 ліній шини. Вхід DIR задає напрямок передачі: при DIR = 1 дані передаються з порту A на порт B, а при DIR = 0 – з B на A. За високого рівня на вході дозволу <span class="formula">\(\overline{OE}=1\)</span> обидва порти ізолюються та переходять у стан високого імпедансу Hi-Z.[^udemy-electronics-course]

## Detailed explanation

TODO
