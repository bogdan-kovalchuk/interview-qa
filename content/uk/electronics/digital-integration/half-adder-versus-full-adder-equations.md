---
id: emb-elinteg-0044
title: "Чим повний двійковий суматор відрізняється від напівсуматора та якими рівняннями він описується?"
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

Напівсуматор додає лише два однобітні операнди (<span class="formula">\(S = A \oplus B\)</span>, <span class="formula">\(C_{out} = A\cdot B\)</span>), не маючи входу для перенесення. Повний суматор враховує вхідне перенесення <span class="formula">\(C_{in}\)</span> від молодшого розряду. Його виходи описуються формулами <span class="formula">\(S = A \oplus B \oplus C_{in}\)</span> та <span class="formula">\(C_{out} = A\cdot B + C_{in}\cdot(A \oplus B)\)</span>, що дозволяє об'єднувати суматори в ланцюжки довільної розрядності.[^udemy-electronics-course]

## Detailed explanation

TODO
