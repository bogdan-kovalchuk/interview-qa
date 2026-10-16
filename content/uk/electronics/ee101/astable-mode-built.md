---
id: emb-elee-0255
title: "Як побудований астабільний режим 555?"
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

<span class="formula">\(R_A\)</span> – від живлення до DISCH, <span class="formula">\(R_B\)</span> – від DISCH до спільного вузла TRIG/THRES, C – від цього вузла до землі. C заряджається через <span class="formula">\(R_A+R_B\)</span> і розряджається через <span class="formula">\(R_B\)</span>, коливаючись між 1/3 і 2/3 <span class="formula">\(V_{CC}\)</span>; вихід генерує імпульси без зовнішнього запуску.[^udemy-electronics-course]

## Detailed explanation

TODO
