---
id: emb-elintro-0055
title: "Що таке мА·год і що вона означає?"
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
  - source_id: analog-ampere-hour
    title: "Analog Devices: Ampere-hour"
    url: https://www.analog.com/en/resources/glossary/amp-hour-ampere-ah-mah.html
  - source_id: doe-battery-capacity-rate
    title: "U.S. Department of Energy: Primer on Lead-Acid Storage Batteries"
    url: https://www.energy.gov/documents/doe-hdbk-1084-95
---

## Short answer

мА·год (mAh) – одиниця електричного заряду, яку використовують для позначення ємності батареї: `Q = I*t`.[^analog-ampere-hour] Теоретично 2400 мА·год відповідають 240 мА протягом 10 годин, але фактичний час залежить від струму розряду та умов роботи батареї.[^doe-battery-capacity-rate]

## Detailed explanation

мА·год означає міліампер-годину: добуток струму в міліамперах на час у годинах. Це одиниця кількості електричного заряду, а не напруги й не енергії. Один ампер-година дорівнює 1000 мА·год; у SI один ампер-година відповідає 3600 кулонам заряду.[^analog-ampere-hour]

Якщо батарея віддає сталий струм, просте наближення для заряду має вигляд `Q = I*t`. Наприклад, для номіналу 2400 мА·год і струму 240 мА ідеальний розрахунок дає `t = Q/I = 2400 mAh/240 mA = 10 h`. Це оцінка за припущення сталого струму й доступності всієї номінальної ємності, а не гарантія часу до вимкнення пристрою.[^analog-ampere-hour]

Реальна ємність залежить від хімії батареї, температури, струму розряду, кінцевої напруги та інших умов. Для деяких батарей більший струм означає меншу доступну ємність, а номінальне значення в документації вказують разом із тестовими умовами. Крім того, мА·год не дозволяють порівнювати запас енергії батарей із різною напругою без урахування напруги: енергія приблизно пов’язана з добутком заряду на напругу.[^doe-battery-capacity-rate]

Приклад: ідеальні 2400 мА·год можна поділити на 120 мА й отримати 20 годин, або на 480 мА й отримати 5 годин. У реальному виробі ці результати можуть відрізнятися, бо струм може змінюватися, а доступна ємність залежить від швидкості розряду та порогу вимкнення. Типова помилка – вважати mAh безпосередньою мірою енергії або обіцяним часом роботи.[^analog-ampere-hour][^doe-battery-capacity-rate]
