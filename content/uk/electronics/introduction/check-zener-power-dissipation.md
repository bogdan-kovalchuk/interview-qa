---
id: emb-elintro-0194
title: "Як перевірити потужність Зенера?"
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
  - source_id: aac-zener-regulator
    title: "All About Circuits: What Are Zener Diodes?"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/zener-diodes/
---

## Short answer

У найгіршому випадку без навантаження майже весь струм через `R_s` іде через Зенер. Обчислити `P_Z = V_Z*I_Z` і порівняти з допустимою потужністю з урахуванням температури та монтажу.[^aac-zener-regulator]

## Detailed explanation

Щоб перевірити потужність стабілітрона, визначають напругу на ньому та найбільший струм, який може пройти через нього в передбачених режимах. У простому шунтовому стабілізаторі струм через `R_s` ділиться між навантаженням і Зенером. За відсутності навантаження майже весь цей струм іде в стабілітрон, тому холостий хід часто є найгіршим режимом для його нагрівання.[^aac-zener-regulator]

Потужність у першому наближенні дорівнює `P_Z = V_Z*I_Z`. Для пошуку максимуму слід підставити максимальну напругу джерела, найменший струм навантаження та реальну напругу стабілізації за відповідного струму. Одночасно перевіряють резистор: зростання вхідної напруги збільшує і його розсіювання. Розраховану потужність порівнюють з умовами datasheet – допустимий номінал може знижуватися зі зростанням температури, а плата й корпус впливають на відведення тепла.[^aac-zener-regulator]

Приклад: для умовного стабілітрона `5.1 V`, через який тече `20 mA`, маємо `P_Z = 5.1 V*0.020 A = 0.102 W`. Це лише оцінка електричної потужності; вона не доводить, що будь-який стабілітрон із написом `0.5 W` безпечно працюватиме за цих умов. Треба звірити теплове derating, температуру довкілля і монтаж конкретного корпусу.[^aac-zener-regulator]

**Типова помилка:** перевірити лише максимальне навантаження. Воно зазвичай відбирає частину струму від Зенера й зменшує його розсіювання; для максимуму потужності аналізують також мінімальне навантаження або його відсутність.[^aac-zener-regulator]
