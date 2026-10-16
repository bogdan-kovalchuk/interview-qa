---
id: emb-eldig-0028
title: "Чому використання доповнення до двох дозволяє замінити операцію віднімання додаванням?"
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

Віднімання числа <span class="formula">\(A - B\)</span> математично еквівалентне додаванню протилежного значення <span class="formula">\(A + (-B)\)</span>. Оскільки від'ємне число формується як <span class="formula">\(\overline{B} + 1\)</span>, процесор використовує той самий апаратний суматор для обох дій. Будь-який вихідний біт переносу за межі розрядної сітки під час віднімання просто відкидається.[^udemy-electronics-course]

## Detailed explanation

TODO
