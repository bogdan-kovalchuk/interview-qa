---
id: emb-elinteg-0067
title: "Які етапи включає формальний синтез послідовного автомата від діаграми переходу до таблиці станів?"
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

Синтез починається зі складання графа перехідних станів, де вузли задають стійкі стани, а спрямовані дуги позначають умови переходів від зовнішніх сигналів. Далі стани кодують двійковими векторами (наприклад, двійковим кодом або кодом One-Hot) та формують зведену таблицю переходових функцій. На основі таблиці для кожного тригера записують логічне рівняння наступного стану відносно поточних змінних.[^udemy-electronics-course]

## Detailed explanation

TODO
