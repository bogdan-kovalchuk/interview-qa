---
id: emb-elintro-0045
title: "Формула електричної потужності (три форми)?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-electric-power
    title: "All About Circuits: Power in Electric Circuits"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/power-electric-circuits/
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

Електрична потужність дорівнює `P = V*I` і вимірюється у ватах (W). Для омічного резистора закон Ома дає еквівалентні форми `P = I²*R` та `P = V²/R`; останні дві потребують саме відповідного опору.[^aac-electric-power]

## Detailed explanation

Електрична потужність показує швидкість передавання або перетворення енергії. Для елемента, на якому є напруга `V` і через який тече струм `I`, потужність дорівнює `P = V*I`; одиниця – ват, де `1 W = 1 J/s`. Знак залежить від вибраних напрямків напруги та струму: додатне значення за пасивною домовленістю означає, що елемент споживає потужність.[^aac-electric-power]

Для резистора, який підкоряється закону Ома `V = I*R`, підстановка напруги або струму в початкову формулу дає `P = I²*R` і `P = V²/R`. Ці вирази зручні, коли відомі інші пари величин, але не є незалежними універсальними законами для будь-якого компонента: виведення використовує саме омічну залежність. У нелінійному елементі напруга й струм можуть не бути пов’язані одним сталим опором, тож спершу визначають його робочу точку або використовують безпосереднє співвідношення потужності.[^aac-voltage-current-resistance]

Приклад: резистор `10 Ω` пропускає `0.2 A`. За ідеалізованого сталого опору падіння напруги дорівнює `2 V`, а розсіювана потужність – `0.4 W` за формулами `V = I*R` і `P = I²*R`. Результат узгоджується з `P = V*I = 2 V*0.2 A = 0.4 W`. Вибираючи реальний резистор, враховують допустиму потужність і температурні умови; обчислене значення описує розсіювання, а не автоматично потрібний номінал компонента.[^aac-electric-power]

**Типова помилка:** використовувати `P = V²/R` або `P = I²*R`, підставляючи напругу чи струм не того самого елемента. Перевірте, що величини задані на резисторі, і що його опір можна вважати сталим у розглянутому режимі.[^aac-voltage-current-resistance]
