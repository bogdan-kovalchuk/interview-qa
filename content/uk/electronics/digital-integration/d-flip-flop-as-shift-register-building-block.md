---
id: emb-elinteg-0024
title: "Як послідовно з'єднані D-тригери утворюють базову комірку регістра зсуву?"
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

D-тригер зберігає значення входу D і передає його на вихід Q за кожним активним фронтом тактового сигналу. Якщо з'єднати вихід Q першого тригера із входом D наступного і подати на них спільний тактовий сигнал, стан просуватиметься на один тригер праворуч за кожен такт. Ланцюжок із n таких тригерів утворює повноцінний n-бітний регістр зсуву.[^udemy-electronics-course]

## Detailed explanation

TODO
