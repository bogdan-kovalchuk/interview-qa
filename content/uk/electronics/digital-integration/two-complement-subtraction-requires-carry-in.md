---
id: emb-elinteg-0056
title: "Чому при виконанні віднімання в АЛП на основі доповнювального коду необхідно примусово подавати вхідне перенесення?"
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

Операція віднімання в апаратному забезпеченні реалізується як додавання доповнення: <span class="formula">\(B - A = B + \overline{A} + 1\)</span>. Інверсія операнда <span class="formula">\(\overline{A}\)</span> формує лише зворотний (одиничний) код. Для перетворення його на справжній доповнювальний код необхідно додати одиницю через вхід перенесення <span class="formula">\(C_n = 1\)</span>, інакше отриманий результат буде рівно на 1 меншим за правильний.[^udemy-electronics-course]

## Detailed explanation

TODO
