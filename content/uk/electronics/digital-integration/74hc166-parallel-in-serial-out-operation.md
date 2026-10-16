---
id: emb-elinteg-0026
title: "Як здійснюється паралельне завантаження та послідовний зсув даних у мікросхемі 74HC166?"
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

У 74HC166 режим визначається входом дозволу паралельного завантаження <span class="formula">\(\overline{PE}\)</span>. За низького рівня <span class="formula">\(\overline{PE}=0\)</span> за тактовим фронтом у регістр одночасно записуються 8 бітів із входів D0–D7. При поверненні входу до високого рівня <span class="formula">\(\overline{PE}=1\)</span> кожен наступний тактовий імпульс виштовхує біти по черзі через вихід Q7.[^udemy-electronics-course]

## Detailed explanation

TODO
