---
id: emb-elintro-0251
title: "Які параметри MOSFET першими перевіряти в datasheet?"
track: electronics
section: introduction
sources:
  - source_id: ti-mosfet-selection
    title: "Texas Instruments: Avoid Common Mistakes When Selecting and Designing with Power MOSFETs"
    url: https://www.ti.com/lit/an/slpa021/slpa021.pdf
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

**Почніть із меж напруги та струму.** Перевірте `V_DS`, допустимий `I_D`, `R_DS(on)` саме за доступного `V_GS`, теплові умови корпусу й абсолютну межу `V_GS`. `V_GS(th)` означає початок малої провідності, а не гарантоване повне відкриття; для швидкого керування перевірте також `Q_g`.[^ti-mosfet-selection]

## Detailed explanation

Параметри MOSFET у datasheet перевіряють у контексті конкретної схеми: спершу напруги, струм і потрібний режим керування, а тоді втрати та нагрівання. `V_DS` має витримувати найбільшу напругу, яка реально може з’явитися між drain і source, включно з перехідними процесами. `I_D` не є самодостатньою обіцянкою струму: допустимий струм залежить від температури корпусу, охолодження, ширини імпульсу та меж корпусу.

Для ключового режиму критичне значення `R_DS(on)` за фактичного `V_GS` від вашого GPIO або драйвера. Не вибирайте його за `V_GS(th)`: цей поріг вимірюють за малого струму, де транзистор лише починає проводити. Наприклад, таблиця TI для CSD18541F5 задає `R_DS(on)` окремо при `V_GS = 4.5 V` і `10 V`; якщо керування дає меншу напругу, наведена межа опору може не діяти.[^ti-mosfet-selection]

Далі оцініть провідникові втрати за `P = I²*R_DS(on)` і перевірте тепловий опір, допустиму температуру переходу та реальний шлях відведення тепла. У таблиці абсолютних максимумів розрізняються, зокрема, струми з різними умовами охолодження; максимальне `I_D` не замінює теплового розрахунку.[^ti-mosfet-selection]

`Q_g` допомагає оцінити, чи здатен контролер заряджати й розряджати gate із потрібною швидкістю; більший заряд може вимагати сильнішого драйвера та збільшити switching losses. Перевірте також абсолютну межу `V_GS`, температурне зростання опору, safe operating area та параметри body diode, якщо вони важливі для топології. Значення з графіків і таблиць мають сенс лише разом з їхніми умовами тестування.[^ti-mosfet-selection]
