---
id: emb-elintro-0048
title: "Як розрахувати резистор для `LED`, якщо `V_supply = 5 V`, `V_f = 2 V`, `I = 20 mA`?"
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
  - source_id: aac-led-resistor
    title: "All About Circuits: Series LED Resistor Calculator"
    url: https://www.allaboutcircuits.com/tools/led-resistor-calculator
---

## Short answer

Для одного `LED` послідовний резистор у цьому номінальному прикладі дорівнює `R = (V_supply - V_f)/I = (5 V - 2 V)/0.020 A = 150 Ω`. На ньому розсіюється `P = I²*R = 0.060 W`; фактичні `V_f` і допустимий струм слід перевірити за datasheet LED.[^aac-led-resistor]

## Detailed explanation

Послідовний резистор обмежує струм через `LED`: решта напруги джерела падає на резистор. Для заданої робочої точки застосовують закон Ома до цієї частини кола. Формула передбачає один LED, джерело постійної напруги й приблизно сталу пряму напругу діода; сам `LED` не є лінійним резистором і без обмеження струму його робоча точка не визначається лише номіналом живлення.[^aac-led-resistor]

**Приклад розрахунку:**

```text
V_R = 5 V - 2 V = 3 V
R = V_R / I = 3 V / 0.020 A = 150 Ω
P_R = V_R * I = 3 V * 0.020 A = 0.060 W
```

Отже, `150 Ω` дає розрахункові `20 mA` за припущених `5 V` живлення та `2 V` прямої напруги. Резистор `180 Ω` зменшить номінальний струм приблизно до `16.7 mA`, що може бути доречним для меншої яскравості чи запасу; перевіряють також допуск джерела, розкид `V_f` та граничний струм конкретного LED за його datasheet.[^aac-led-resistor]

Потужність у резисторі становить `60 mW` у цих ідеалізованих умовах. Номінал потужності компонента має перевищувати розсіювану потужність з урахуванням температури, охолодження й рекомендацій виробника; отже `1/4 W` тут має запас, але це не універсальна вимога до всіх таких кіл.[^aac-led-resistor]

Важливо не змішувати одиниці: `20 mA = 0.020 A`. Підставляння числа 20 замість `0.020 A` занижує розрахований опір у тисячу разів. Для кількох послідовних LED у формулі віднімають суму їхніх прямих напруг; для потужного LED простий резистор може бути непридатним, і потрібен стабілізатор струму.[^aac-led-resistor]
