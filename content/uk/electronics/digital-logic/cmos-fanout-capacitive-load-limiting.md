---
id: emb-eldig-0012
title: "Чому навантажувальна здатність мікросхем CMOS обмежується ємністю, а не струмом?"
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

Входи польових транзисторів CMOS мають величезний вхідний опір і мізерний статичний струм витоку. Проте кожен вхід створює паразитну ємність <span class="formula">\(C_I \approx 1\text{–}10\text{ pF}\)</span>, яка навантажує вихід. Максимальний fanout визначається як <span class="formula">\(C_L / C_I\)</span>; перевищення паспортної ємності навантаження C_L затягує фронти сигналів і порушує часові параметри.[^udemy-electronics-course]

## Detailed explanation

TODO
