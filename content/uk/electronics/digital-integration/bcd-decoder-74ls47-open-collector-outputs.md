---
id: emb-elinteg-0009
title: "Чому виходи дешифратора 74LS47 виконані за схемою з відкритим колектором?"
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

Виходи з відкритим колектором не мають верхнього підтягувального транзистора і здатні лише замикати вивід на землю. Це дозволяє безпечно вбирати струм до 24 мА на сегмент та комутувати індикатори з напругою живлення вищою за 5 В. Для нормальної роботи кожного сегмента індикатора зі спільним анодом обов'язково встановлюють зовнішній струмообмежувальний резистор.[^udemy-electronics-course]

## Detailed explanation

TODO
