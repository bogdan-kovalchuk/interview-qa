---
id: emb-elee-0219
title: "Навіщо зворотний (flyback) діод паралельно двигуну і як його підключити?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: fiore-bjt-switching
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.7 BJT Switching and Driver Applications"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.7:_BJT_Switching_and_Driver_Applications
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
  - source_id: libretexts-fiore-diode-models
    title: "Fiore: Semiconductor Devices, 2.4 Diode Circuit Models (Engineering LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.4:_Diode_Circuit_Models
---

## Short answer

Двигун – індуктивне навантаження: після вимкнення транзистора його струм не може миттєво зникнути, і виникає викид напруги. Діод катодом до плюса живлення, анодом до колектора дає шлях цьому струму; в нормальній роботі він закритий.[^fiore-bjt-switching]

## Detailed explanation

**Звідки викид.** Для котушки `v = L*di/dt`: що швидша зміна струму, то більша напруга.[^fiore-ac-circuit-analysis] Струм обмотки двигуна не може миттєво зникнути, тож після вимкнення транзистора обмотка створює напругу зворотної полярності, яка з’являється між колектором і емітером.[^fiore-bjt-switching] Умовний приклад: обмотка з `L = 10 мГн` несе `I = 1 А`, і струм спадає до нуля за `10 мкс`. Тоді `v = 0,01*1/(10*10^-6) = 1000 В`, що в десятки разів перевищує напругу живлення 12 В. Такий викид може пошкодити транзистор.[^fiore-bjt-switching]

**Куди ставити діод.** Діод ставлять паралельно двигуну: катод до плюса живлення, анод до колектора. Під час роботи транзистор відкритий, колектор майже на землі, тож катод на +12 В, а анод майже на землі: діод зворотно зміщений і не проводить.[^fiore-bjt-switching] Коли транзистор вимикається, колектор піднімається, і щойно його напруга перевищує `V_CC` приблизно на 0,7 В, діод відкривається.[^libretexts-fiore-diode-models] Далі струм обмотки тече через діод, а колектор обмежується приблизно рівнем `V_CC + 0,7 В` за моделлю з колінною напругою.

**Типові помилки:**

- Перевернути діод (анод на плюсі, катод на колекторі): при відкритому транзисторі він проводить від `+V` через транзистор на землю, і виникає коротке замикання.
- Вважати, що діод впливає на нормальну роботу: за нормальної роботи він зворотно зміщений і струму через себе не пропускає.[^fiore-bjt-switching]
