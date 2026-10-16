---
id: emb-elinteg-0057
title: "Як інтерпретується та чому спотворюється на десятковому індикаторі від'ємний результат віднімання в 4-бітному АЛП?"
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

При відніманні більшого числа з меншого результат формується у 4-бітному доповнювальному коді (наприклад, <span class="formula">\(5 - 9 = -4\)</span> кодується як 1100). Беззнаковий десятковий драйвер 7447 сприймає код 1100 як число 12. Оскільки мікросхема 7447 не підтримує відображення від'ємних чисел і шістнадцяткових знаків, вона виводить на дисплей спотворений службовий символ.[^udemy-electronics-course]

## Detailed explanation

TODO
