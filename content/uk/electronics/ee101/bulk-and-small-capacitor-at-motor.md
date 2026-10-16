---
id: emb-elee-0261
title: "Навіщо біля двигуна ставлять і великий накопичувальний конденсатор, і конденсатор 0,1 мкФ?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Великий конденсатор (у лекції 2200 мкФ) віддає пусковий струм двигуна, тож шина не просідає і струм не тягнеться через усі провідники від стабілізатора. Малий 0,1 мкФ на виводах двигуна замикає високочастотні завади там, де вони виникають. Разом вони зменшили завади з кількох вольт до приблизно ±50 мВ.[^udemy-electronics-course]

## Detailed explanation

TODO
