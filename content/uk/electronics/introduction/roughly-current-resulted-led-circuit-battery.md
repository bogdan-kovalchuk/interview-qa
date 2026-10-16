---
id: emb-elintro-0304
title: "Який струм приблизно вийшов у LED-схемі з 9 В батареєю і 220 Ом?"
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
  - source_id: adafruit-led-forward-voltage-kvl
    title: "Adafruit Learning System: Forward Voltage and KVL"
    url: https://learn.adafruit.com/all-about-leds/forward-voltage-and-kvl
---

## Short answer

За виміряного падіння 6.55 V на резисторі 220 Ω струм дорівнює приблизно 29.8 mA за законом Ома. Значення близько 30 mA – результат прикладу лекції; лише батарея 9 V і номінал резистора не задають точний струм, бо треба знати фактичну напругу батареї та LED.[^udemy-electronics-course] [^adafruit-led-forward-voltage-kvl]

## Detailed explanation

У послідовному колі батареї, LED і резистора той самий струм проходить через обидва компоненти. Напруга джерела розподіляється між LED та резистором, тому струм резистора можна оцінити законом Ома: напругу на ньому ділять на його опір. Саме падіння на резисторі, а не повні 9 V батареї, треба підставляти у формулу.[^adafruit-led-forward-voltage-kvl]

У наведеному вимірюванні на резисторі було близько 6.55 V, а його номінал становив 220 Ω. Розрахунок дає приблизно 0.0298 A, тобто близько 29.8 mA; округлено це близько 30 mA, як і повідомляється для прикладу лекції.[^udemy-electronics-course] Для перевірки потужності резистора оцініть `P = V*I`: за цих виміряних значень це близько 0.195 W, тож резистор 0.25 W працюватиме з малим запасом за ідеальних умов; у реальному монтажі враховують температурне derating та фактичний номінал.[^aac-direct-current]

Не можна обчислити точний струм лише як `9 V/220 Ω`, бо частина напруги припадає на LED. Так само результат не є універсальним для будь-якої 9 V батареї: її напруга під навантаженням залежить від заряду та внутрішнього опору, а forward voltage LED – від типу, струму й температури. Тому виміряні 6.55 V і приблизно 30 mA належать до конкретного стендового прикладу, а для власної схеми слід виміряти напругу на резисторі або обчислити її з фактичних параметрів.[^adafruit-led-forward-voltage-kvl]
