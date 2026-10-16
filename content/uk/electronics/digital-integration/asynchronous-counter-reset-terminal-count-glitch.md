---
id: emb-elinteg-0072
title: "Чому скидання лічильника 7493 на заданому коді породжує короткочасний паразитний імпульс (глітч)?"
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

Асинхронні входи скидання R0(1) і R0(2) спрацьовують лише тоді, коли дешифратор виявляє код кінцевого стану (наприклад, 13 при рахунку до 12). Отже, код 13 мусить фізично з'явитися на виходах лічильника на кілька наносекунд, перш ніж сигнал через вентиль обнулить тригери. Цей короткий перехідний імпульс (глітч) може бути помилково сприйнятий швидкими зовнішніми мікросхемами як дійсний стан.[^udemy-electronics-course]

## Detailed explanation

TODO
