---
id: emb-elintro-0044
title: "Закон Ома – запишіть три його форми?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-voltage-current-resistance
    title: "All About Circuits: Ohm’s Law - How Voltage, Current, and Resistance Relate"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/voltage-current-resistance-relate/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Для омічного елемента за сталих фізичних умов: `V = I*R`, `I = V/R`, `R = V/I`. У кожній формі напруга й струм мають стосуватися того самого елемента; закон не є універсальною моделлю нелінійних компонентів.[^aac-voltage-current-resistance]

## Detailed explanation

Закон Ома пов’язує напругу `V` на елементі, струм `I` через нього та його опір `R`: `V = I*R`. Перенесення множників дає ще дві форми: `I = V/R` і `R = V/I`. Усі три записи описують одне співвідношення, а вибір форми залежить від невідомої величини. Узгодьте одиниці: вольти, ампери й оми дають відповідно ампери або оми після ділення.[^aac-voltage-current-resistance]

Важливе обмеження – закон Ома в такому вигляді застосовують до омічного елемента, для якого співвідношення напруги й струму є лінійним за заданих фізичних умов. Для звичайного резистора опір змінюється з температурою, тому значне нагрівання може змінити значення `R`; для діода або лампи розжарювання проста стала величина опору може бути непридатною моделлю. Напруга має бути виміряна саме на тому елементі, а струм – через нього, а не взятий з іншої частини кола.[^aac-voltage-current-resistance]

Приклад: на резисторі `2 kΩ` виміряно `6 V`. Тоді струм через нього `I = V/R = 6 V/2000 Ω = 0.003 A = 3 mA`. Для цього розрахунку припускаємо, що опір резистора дорівнює `2 kΩ` під час вимірювання та він поводиться омічно. Після обчислення корисно перевірити розмірність: вольт, поділений на ом, дорівнює амперу.[^aac-voltage-current-resistance]

**Типова помилка:** казати, що будь-які два числа з кола можна підставити у формулу. Спершу встановіть, що напруга, струм і опір стосуються одного елемента, і перевірте, чи його поведінка відповідає омічній моделі.[^aac-voltage-current-resistance]
