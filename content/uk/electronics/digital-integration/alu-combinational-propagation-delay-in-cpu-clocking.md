---
id: emb-elinteg-0051
title: "Чому комбінаційна затримка АЛП визначає мінімальну тривалість такту процесорної команди?"
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

Мікросхема 74x181 є асинхронним комбінаційним пристроєм і не містить внутрішніх тригерів чи синхросигналів. Сигнал проходить крізь до 6–7 каскадів вентилів, перш ніж на виході з'явиться достовірний результат. Період тактового генератора процесора повинен із запасом перевищувати найдовшу затримку найповільнішої арифметичної операції, або на виконання операції слід виділяти кілька тактів.[^udemy-electronics-course]

## Detailed explanation

TODO
