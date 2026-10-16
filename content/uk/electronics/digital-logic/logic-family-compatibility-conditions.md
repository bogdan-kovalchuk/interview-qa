---
id: emb-eldig-0031
title: "Які дві умови рівнів напруг необхідні для прямої сумісності логічних сімейств?"
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

Для передачі сигналу логічної 1 мінімальна вихідна напруга передавача має перевищувати поріг приймача: <span class="formula">\(V_{OH} \ge V_{IH}\)</span>. Для логічного 0 максимальна вихідна напруга передавача має бути нижчою за вхідний поріг приймача: <span class="formula">\(V_{OL} \le V_{IL}\)</span>. Окрім напруги, вихід передавача повинен забезпечувати необхідний вхідний струм навантаження в обох станах.[^udemy-electronics-course]

## Detailed explanation

TODO
