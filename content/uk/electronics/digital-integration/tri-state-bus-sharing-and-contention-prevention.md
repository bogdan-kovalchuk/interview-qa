---
id: emb-elinteg-0036
title: "Що таке стан високого імпедансу (Hi-Z) і чому конфлікт шини є небезпечним явищем?"
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

У стані високого імпедансу Hi-Z обидва вихідні транзистори закриті, і вивід не передає струм, електрично від'єднуючись від лінії. Конфлікт шини (bus contention) виникає тоді, коли два або більше драйверів одночасно намагаються видати різні рівні на спільну шину. Це спричиняє протікання великих наскрізних струмів, просідання напруги живлення та можливий тепловий пробій мікросхем.[^udemy-electronics-course]

## Detailed explanation

TODO
