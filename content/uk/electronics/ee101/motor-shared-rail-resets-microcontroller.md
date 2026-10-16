---
id: emb-elee-0260
title: "Чому двигун на спільній шині живлення може зависати мікроконтролер?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Двигун – індуктивне навантаження: під час обертання він створює імпульсні завади й зворотну ЕРС, які повертаються на шину живлення. У лекції на шині 3,3 В вони сягали 2–3 В від піку до піку і опускали напругу нижче землі. Такі викиди скидають або збивають логіку, і це легко прийняти за помилку в прошивці.[^udemy-electronics-course]

## Detailed explanation

TODO
