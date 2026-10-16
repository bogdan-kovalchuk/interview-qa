---
id: emb-elinteg-0034
title: "Чому в регістрах зсуву на макетних платах виникають помилкові спрацьовування та зайві біти?"
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

Безпайкові макетні плати та довгі сполучні дроти мають високу паразитну ємність (до 2–5 пФ на контакт) і паразитну індуктивність. Швидкі фронти перемикання світлодіодних навантажень створюють стрибки напруги по шинах живлення та землі, що наводяться на тактовий вхід. У результаті регістр сприймає перешкоду як додатковий тактовий імпульс і записує зайві одиниці.[^udemy-electronics-course]

## Detailed explanation

TODO
