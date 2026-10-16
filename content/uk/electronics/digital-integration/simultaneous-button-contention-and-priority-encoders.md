---
id: emb-elinteg-0055
title: "Чому одночасне натискання двох кнопок у простій схемі на вентилях OR вимагає застосування пріоритетного шифратора?"
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

Вентилі OR реалізують побітове логічне додавання вхідних сигналів. Якщо користувач одночасно натисне дві кнопки, схема сформує змішаний код, що призведе до виконання непередбаченої операції. Для усунення цієї невизначеності застосовують пріоритетний шифратор (наприклад, 74x148), який завжди вибирає сигнал із найвищим пріоритетом і блокує інші входи.[^udemy-electronics-course]

## Detailed explanation

TODO
