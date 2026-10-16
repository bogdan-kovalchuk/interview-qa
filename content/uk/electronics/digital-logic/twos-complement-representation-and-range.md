---
id: emb-eldig-0027
title: "Як утворюється від'ємне число в доповненні до двох (two's complement) і який діапазон 8 бітів?"
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

Для отримання від'ємного числа інвертують усі біти вихідного додатного числа та додають до результату одиницю. Для <span class="formula">\(n\)</span> бітів допустимий діапазон значень становить від <span class="formula">\(-2^{n-1}\)</span> до <span class="formula">\(2^{n-1} - 1\)</span>. У 8-розрядній системі це відповідає числам від −128 до +127, причому одиниця в старшому біті (MSB) свідчить про від'ємний знак.[^udemy-electronics-course]

## Detailed explanation

TODO
