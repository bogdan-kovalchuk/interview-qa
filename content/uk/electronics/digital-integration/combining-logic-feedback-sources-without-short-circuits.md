---
id: emb-elinteg-0031
title: "Чому вихід регістра зсуву та кнопку введення даних не можна об'єднувати простим електричним з'єднанням?"
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

Пряме з'єднання двох джерел логічних сигналів створює коротке замикання, якщо одне джерело видає рівень 1 (VCC), а інше формує 0 (GND). Виникає надлишковий струм конфлікту шини, що викликає падіння логічних рівнів та перегрів мікросхем. Для безпечного об'єднання кількох сигналів зворотного зв'язку обов'язково використовують логічний елемент OR.[^udemy-electronics-course]

## Detailed explanation

TODO
