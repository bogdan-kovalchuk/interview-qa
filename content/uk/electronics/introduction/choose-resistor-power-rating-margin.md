---
id: emb-elintro-0097
title: "Навіщо брати резистор із запасом по потужності?"
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
  - source_id: aac-resistor-power
    title: "Resistors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/resistors/
---

## Short answer

Номінальна потужність резистора має бути не нижчою за розраховану розсіювану потужність за фактичних умов монтажу. Універсального правила «завжди брати `2×`» немає: перевіряють температурне derating у datasheet і враховують температуру довкілля та охолодження.[^aac-resistor-power]

## Detailed explanation

Номінальна потужність резистора – це межа розсіювання тепла, визначена виробником за конкретних умов, а не гарантована потужність за будь-якого монтажу.[^aac-resistor-power] Електрична потужність перетворюється на тепло в резистивному елементі; для постійного струму її можна обчислити як `P = I^2*R` або `P = V^2/R`, де `V` – напруга саме на резисторі.[^aac-resistor-power]

Порівняння лише з цифрою на корпусі недостатнє. Datasheet може задавати зменшення допустимої потужності зі зростанням температури довкілля, граничну температуру елемента, умови монтажу на плату, а також окремі обмеження для імпульсного режиму. Для коротких імпульсів середня потужність не завжди описує ризик: енергія імпульсу та теплова маса резистора теж мають значення. Отже, потрібний запас визначають конкретним типом резистора, температурою, вентиляцією, допусками схеми й профілем навантаження, а не одним множником для всіх конструкцій.[^aac-resistor-power]

Приклад розрахунку: через резистор `100 Ω` протікає сталий струм `33 mA`. Ідеальна оцінка дає `P = I^2*R = 0.109 W`, тобто приблизно `0.11 W`. Це ще не доводить, що номіналу `0.125 W` достатньо: за підвищеної температури його допустима потужність може бути знижена. Треба перевірити графік derating у datasheet і вибрати найближчий номінал, допустимий саме в заданих умовах.[^aac-resistor-power]

**Типова помилка:** сприймати популярне правило запасу `2×` як вимогу стандарту. Воно може бути практичним початковим орієнтиром у певному дизайні, але не замінює перевірку datasheet, імпульсної стійкості та температурного режиму.
