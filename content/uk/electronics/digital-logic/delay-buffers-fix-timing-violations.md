---
id: emb-eldig-0018
title: "Як пара послідовних інверторів допомагає усунути порушення часу встановлення або утримання?"
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

Якщо сигнал надходить на вхід мікросхеми занадто рано відносно тактового фронту, його затримують за допомогою каскаду буферів. Два послідовні інвертори відновлюють вихідний логічний рівень сигналу, додаючи сумарну затримку поширення обох вентилів. Наприклад, два інвертори із затримкою по 5 нс забезпечують затримку 10 нс без зміни логічного змісту сигналу.[^udemy-electronics-course]

## Detailed explanation

TODO
