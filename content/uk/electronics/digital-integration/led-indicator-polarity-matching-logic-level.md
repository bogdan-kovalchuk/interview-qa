---
id: emb-elinteg-0058
title: "Чому невідповідність підключення світлодіодного індикатора виходу перенесення призводить до хибного відображення переповнення?"
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

Якщо світлодіод увімкнено катодом до виходу мікросхеми, а анодом через резистор до VCC, він світиться при низькому рівні LOW. Якщо вихід перенесення АЛП є активним високим (HIGH при перенесенні), індикатор світитиметься за відсутності перенесення і згасатиме при його виникненні. Полярність увімкнення індикаторів повинна завжди узгоджуватися з активним рівнем конкретного сигналу за даташитом.[^udemy-electronics-course]

## Detailed explanation

TODO
