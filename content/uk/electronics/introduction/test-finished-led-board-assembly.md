---
id: emb-elintro-0302
title: "Як тестувати готову LED-плату після монтажу?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: fluke-continuity-test
    title: "Fluke: A Guide to Continuity Testing with a Multimeter"
    url: https://www.fluke.com/en-us/learn/blog/digital-multimeters/how-to-test-for-continuity
---

## Short answer

На знеструмленій платі перевірте можливе коротке замикання та огляньте пайку; режим continuity використовуйте тільки без живлення. Потім подайте живлення через передбачений вхід і перевірте напругу та роботу LED, вимикаючи плату перед перевіркою полярності й з’єднань.[^fluke-continuity-test]

## Detailed explanation

Готову LED-плату спершу оглядають і перевіряють без живлення, а потім контрольовано вмикають та вимірюють у робочому режимі. Переконайтеся, що компоненти відповідають схемі, полярний LED орієнтований правильно, а на площадках немає очевидних містків припою чи незмочених з’єднань. У режимі continuity або опору перевіряйте плату лише зі знятим живленням; мультиметр подає власний тестовий струм, тому зовнішня напруга може спотворити результат або пошкодити прилад.[^fluke-continuity-test]

Після цього підключіть лабораторне джерело з обмеженням струму, якщо воно є, або батарею через штатний роз’єм, перевіривши полярність і номінал напруги. Увімкніть вимикач і спостерігайте за струмом споживання та очікуваними ознаками: має світитися саме той LED, який передбачений станом схеми. За потреби виміряйте напругу живлення й падіння напруги на резисторі; у послідовному колі однаковий струм проходить через резистор і LED, а резистор обмежує його.[^udemy-electronics-course] [^aac-direct-current]

Якщо LED не світиться, спочатку вимкніть живлення. Далі перевірте полярність LED і джерела, цілісність доріжки, пайку та наявність потрібної напруги, рухаючись від входу живлення до LED. Якщо джерело переходить в обмеження струму або компонент нагрівається, не залишайте плату увімкненою: це ознака можливої помилки монтажу чи неправильного навантаження. Базовий функціональний тест підтверджує лише перевірений режим, а не надійність плати за будь-якої напруги чи температури.
