---
id: emb-elee-0101
title: "Чому −3 dB за напругою – це не половина амплітуди?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-decibels
    title: "All About Circuits: Decibels for Voltage and Power Ratios"
    url: https://www.allaboutcircuits.com/textbook/designing-analog-chips/analog-measurements/db-for-voltage-add-power-ratios/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

−3 dB відповідає відношенню амплітуд `10^(-3/20) ≈ 0.708`, тобто приблизно 70.8%, а не половині. Половина напруги становить близько −6.02 dB; половина потужності відповідає −3 dB за однакових опорів.[^aac-decibels]

## Detailed explanation

Значення в децибелах для відношення напруги обчислюють за формулою `G_dB = 20*log10(V_out/V_in)`. Тому −3 dB дають `V_out/V_in = 10^(-3/20) ≈ 0.708`: вихідна амплітуда становить близько 70.8% вхідної, а не 50%. Формула для напруги спирається на однакові опори; саме тоді відношення потужностей дорівнює квадрату відношення напруг.[^aac-decibels]

Число 3 dB походить від потужності: `10*log10(0.5) ≈ -3.01 dB`, тобто половина потужності. Коли опори однакові, потужність пропорційна квадрату напруги, отже половині потужності відповідає напруга `sqrt(0.5) ≈ 0.707` від початкової. Для половини напруги розрахунок інший: `20*log10(0.5) ≈ -6.02 dB`.[^aac-decibels]

Приклад для сигналу з початковою амплітудою 2 V: після ослаблення на 3 dB амплітуда буде приблизно `2*0.708 = 1.416 V`, а не 1 V. Якщо ж джерело й навантаження мають однаковий опір, потужність сигналу становитиме приблизно половину початкової.[^aac-decibels]

**Типова помилка:** сприйняти «половина потужності» як «половина напруги». Вона проявляється у вимірюванні −6 dB замість −3 dB для точки зрізу простого RC-фільтра. Щоб уникнути цього, спершу визначте, чи порівнюєте напругу, струм або потужність, а для відношення напруг перевірте, чи однакові опори на обох вимірюваннях.[^aac-decibels]
