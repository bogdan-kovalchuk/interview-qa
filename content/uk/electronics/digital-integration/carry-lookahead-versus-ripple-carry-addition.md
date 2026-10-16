---
id: emb-elinteg-0045
title: "У чому перевага суматорів із прискореним перенесенням над звичайними послідовними суматорами?"
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

У послідовному суматорі (ripple carry) кожен наступний розряд змушений чекати формування сигналу перенесення від усіх попередніх ступенів, через що затримка зростає лінійно з розрядністю. Суматор із прискореним перенесенням (carry look-ahead) містить додаткову комбінаційну схему генерації та розповсюдження перенесення. Вона обчислює всі перенесення одночасно безпосередньо з вхідних операндів за фіксований час.[^udemy-electronics-course]

## Detailed explanation

TODO
