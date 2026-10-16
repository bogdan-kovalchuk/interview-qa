---
id: emb-elinteg-0054
title: "Як постійний запам'ятовувальний пристрій (ПЗП) може замінити комбінаційну логіку декодування кнопок?"
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

Сигнали від кнопок вибору операції можна подати безпосередньо на адресні входи мікросхеми ПЗП чи Flash-пам'яті. У комірки пам'яті за адресами, що відповідають одиничним бітам (1, 2, 4, 8, 16...), записують готові двійкові коди операцій для АЛП. Пам'ять працює як гнучка таблиця пошуку (LUT), дозволяючи змінювати логіку перепризначення без паяння дискретних вентилів.[^udemy-electronics-course]

## Detailed explanation

TODO
