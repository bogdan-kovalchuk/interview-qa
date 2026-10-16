---
id: emb-elee-0253
title: "Як працюють компаратори і вивід DISCH таймера 555?"
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

Компаратори порівнюють напруги з ≈ 1/3 і 2/3 <span class="formula">\(V_{CC}\)</span>. TRIG нижче 1/3 <span class="formula">\(V_{CC}\)</span> встановлює вихід у високий стан; THRES вище 2/3 <span class="formula">\(V_{CC}\)</span> скидає вихід, і DISCH відкриває шлях розряджання. Низький RESET примусово скидає вихід.[^udemy-electronics-course]

## Detailed explanation

TODO
