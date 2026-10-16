---
id: emb-elinteg-0007
title: "Чому логічний сигнал не можна знімати у вузлі між світлодіодом та обмежувальним резистором?"
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

Світлодіод у прямому напрямку фіксує спад напруги близько 1,8–2,2 В. Якщо зняти логічний сигнал у вузлі між світлодіодом і резистором, напруга потрапляє в невизначену зону логічних рівнів замість повного розмаху VCC або землі. Для надійного зчитування логічний сигнал необхідно підключати безпосередньо до вихідного виводу мікросхеми до резистора.[^udemy-electronics-course]

## Detailed explanation

TODO
