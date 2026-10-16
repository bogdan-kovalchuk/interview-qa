---
id: emb-elinteg-0068
title: "За якими правилами впорядковують карти Карно та як об'єднання клітинок спрощує логічну функцію?"
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

Рядки й стовпці карти Карно впорядковуються за кодом Грея (00, 01, 11, 10), щоб сусідні клітинки відрізнялися значенням рівно одного розряду. Суміжні одиниці об'єднують у прямокутні групи розміром <span class="formula">\(2^k\)</span> клітинок (1, 2, 4, 8, 16), враховуючи циклічність країв карти. При об'єднанні клітинок змінна, що приймає в групі як значення 0, так і 1, повністю виключається з виразу кон'юнкції.[^udemy-electronics-course]

## Detailed explanation

TODO
