---
id: emb-elinteg-0030
title: "Чому послідовні логічні схеми обов'язково потребують початкового скидання після ввімкнення живлення?"
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

При подачі напруги живлення внутрішні тригери та регістри переходять у випадкові стани, обумовлені асиметрією порогів окремих транзисторів. Без примусової ініціалізації цифрова система починає виконання з невизначеного або забороненого стану. Спеціальне асинхронне коло скидання (POR) утримує сигнал скидання активним до повної стабілізації напруги живлення.[^udemy-electronics-course]

## Detailed explanation

TODO
