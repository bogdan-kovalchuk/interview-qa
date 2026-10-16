---
id: emb-elee-0016
title: "Чому навантаження змінює вихідну напругу потенціометра-дільника і яке практичне правило?"
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
  - source_id: aac-voltage-divider-loading
    title: "All About Circuits: Voltmeter Impact on Measured Circuit"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-8/voltmeter-impact-measured-circuit/
---

## Short answer

Навантаження паралельне нижній частині дільника, тому зменшує її еквівалентний опір і зазвичай знижує `V_out`. Практичне правило – брати `R_load` принаймні у 10 разів більшим за повний опір потенціометра, але це лише наближення: похибка залежить від положення wiper і вимог до точності.[^aac-voltage-divider-loading]

## Detailed explanation

Потенціометр як дільник можна подати двома послідовними опорами: верхньою частиною доріжки та нижньою частиною між wiper і опорним вузлом. Коли до виходу під’єднують навантаження, воно стає паралельним нижній частині доріжки. Паралельне з’єднання має менший опір, ніж кожна з гілок окремо, тому частка напруги, що припадає на нижню гілку, змінюється. Це і є loading; попереднє рівняння дільника без навантаження вже не описує вихід.[^aac-voltage-divider-loading]

Для конкретного положення wiper позначимо верхню частину `R_1`, а нижню `R_2`. Тоді `R_2_eff = R_2 || R_load`, а напругу можна знайти як `V_out = V_in*R_2_eff/(R_1 + R_2_eff)`. Оскільки `R_2_eff < R_2`, вихідна напруга нижча за значення без навантаження. В еквіваленті Тевенена вихідний опір дільника дорівнює `R_1 || R_2`; саме його співвідношення з `R_load` допомагає оцінити похибку для обраного положення.[^aac-voltage-divider-loading]

Приклад розрахунку: потенціометр 10 kΩ стоїть посередині, отже `R_1 = R_2 = 5 kΩ`. Без навантаження вихід становить половину `V_in`. Якщо `R_load = 100 kΩ`, тоді `R_2_eff ≈ 4.76 kΩ`, а частка виходу буде близько 0.488 від `V_in` замість 0.500. Правило 10:1 тут дає невелику похибку, але інше положення wiper, допуск деталей або суворіша вимога можуть змінити прийнятний номінал; розраховуйте найгіршу точку або моделюйте повний діапазон.[^aac-voltage-divider-loading]

**Типові помилки:** вважати, що сам факт підключення входу не змінює схему, або застосовувати 10:1 як універсальну межу похибки. Високоомний вхід буфера чи підсилювача може зменшити loading, а для точного аналогового сигналу слід перевірити вхідний опір, допустиму похибку й вихідний опір дільника. Опір вольтметра також є навантаженням і може впливати на вимірювання, якщо він не набагато більший за опір вузла.[^aac-voltage-divider-loading]
