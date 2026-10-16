---
id: emb-elinteg-0038
title: "Чим прозора засувка 74x373 відрізняється від звичайного шинного буфера 74x244?"
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

Буфер 74x244 є чисто комбінаційною схемою, яка лише транслює поточний стан входів на виходи з посиленням струму. Прозора засувка 74x373 містить внутрішні елементи пам'яті: поки сигнал LE дорівнює 1, вона пропускає дані (прозорий режим), а при спаді LE в 0 фіксує останній стан. Це дозволяє звільнити шину процесора для передачі інших сигналів.[^udemy-electronics-course]

## Detailed explanation

TODO
