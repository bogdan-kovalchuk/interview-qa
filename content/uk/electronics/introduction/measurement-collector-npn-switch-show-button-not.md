---
id: emb-elintro-0221
title: "Що показує вимірювання колектора NPN-ключа, коли кнопка не натиснута?"
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
  - source_id: aac-bjt-switch
    title: "All About Circuits: The Bipolar Junction Transistor (BJT) as a Switch"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/transistor-switch-bjt/
---

## Short answer

Коли кнопка не натиснута й база не отримує струму, NPN-транзистор перебуває в `cutoff`, тож струм колектора практично відсутній. У типовій схемі з резистором між колектором і `V_CC` падіння на резисторі мале, а колектор має напругу, близьку до `V_CC` – не обов’язково 5 В.[^aac-bjt-switch]

## Detailed explanation

У типовому NPN-ключі емітер під’єднаний до спільної землі, а навантаження з’єднує живлення з колектором. Кнопка керує струмом бази: у розімкненому стані база не отримує достатнього прямого струму, тому транзистор переходить у `cutoff` і канал колектор–емітер поводиться приблизно як розімкнений вимикач.[^aac-bjt-switch]

Оскільки струм навантаження майже не тече, на послідовному резисторі навантаження майже немає падіння напруги. Тому напруга колектора наближається до напруги живлення. Її не можна автоматично називати 5 В: вона визначається джерелом у конкретній схемі. Реальний транзистор також не є ідеальним вимикачем, тож можливі невеликий leakage current і відхилення вимірювання.[^aac-bjt-switch]

**Приклад:** якщо колекторне навантаження є резистором від `V_CC` до колектора, а кнопка не подає струму на базу, майже вся напруга джерела вимірюється між колектором та емітером. Показ мультиметра буде близький до `V_CC`, якщо немає іншого шляху струму або навантаження, яке змінює стан вузла.[^aac-bjt-switch]

**Типова помилка:** сприймати рівень колектора як універсально фіксовані 5 В. Спершу визначте, до якого джерела під’єднано колекторний резистор і відносно якого вузла вимірюється напруга; `cutoff` описує стан транзистора, а не номінал джерела.[^aac-bjt-switch]
