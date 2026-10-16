---
id: emb-elee-0035
title: "Чому струм заряджання RC-кола максимальний на початку і спадає до нуля?"
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
  - source_id: aac-capacitor-transient
    title: "All About Circuits: Capacitor transient response"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-16/capacitor-transient-response/
---

## Short answer

Для ідеального джерела сталої напруги `V_0`, послідовного `R` і спочатку розрядженого `C` початковий струм дорівнює `V_0/R`. У міру заряджання конденсатора напруга на резисторі й струм спадають експоненційно з часовою сталою `τ = R*C`; в усталеному режимі струм прямує до нуля.[^aac-capacitor-transient]

## Detailed explanation

У послідовному RC-колі з ідеальним джерелом `V_0` закон Кірхгофа для напруг дає `V_0 = V_R + V_C`. Безпосередньо перед замиканням ключа конденсатор розряджений, тому його напруга дорівнює нулю. Якщо напруга на конденсаторі не має стрибка, то в початкову мить майже вся напруга джерела прикладена до резистора; за законом Ома початковий струм становить `I(0) = V_0/R`.[^aac-capacitor-transient]

Струм через конденсатор пов’язаний зі швидкістю зміни його напруги, а в резисторі – з миттєвою напругою на ньому. Коли заряд накопичується, `V_C` зростає, `V_R = V_0 - V_C` зменшується, і разом із ним спадає струм. Для цієї простої схеми розв’язок має експоненційну форму, а часова стала дорівнює `τ = R*C`: через один `τ` напруга конденсатора проходить приблизно 63.2% шляху до кінцевого значення, а струм лишається приблизно 36.8% від початкового.[^aac-capacitor-transient]

Це не означає, що конденсатор «перекриває» струм миттєво. Струм стає дедалі меншим упродовж перехідного процесу; математично він прямує до нуля, а на практиці через скінченний час може бути просто нижчим за точність вимірювання. Якщо конденсатор спочатку заряджений або джерело має інший профіль, початковий струм і весь перехід визначаються початковою напругою та повною схемою, а не формулою для розрядженого `C`.[^aac-capacitor-transient]

Приклад: для `V_0 = 5 V` і `R = 1 kΩ` початковий струм дорівнює `I(0) = 5 V / 1 kΩ = 5 mA`. Збільшення `C` подовжить перехід, але не змінить це початкове значення за тих самих ідеальних `V_0` та `R`.[^aac-capacitor-transient]

**Типова помилка:** називати `V_0/R` струмом усього процесу. Це лише початкове значення; надалі струм змінюється, бо змінюється напруга на резисторі.
