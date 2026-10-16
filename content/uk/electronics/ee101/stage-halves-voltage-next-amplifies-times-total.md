---
id: emb-elee-0100
title: "Каскад послаблює напругу вдвічі, наступний підсилює в 10 разів. Яке загальне підсилення в dB?"
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
  - source_id: aac-decibels
    title: "All About Circuits: Decibels for Voltage and Power Ratios"
    url: https://www.allaboutcircuits.com/textbook/designing-analog-chips/analog-measurements/db-for-voltage-add-power-ratios/
---

## Short answer

Перший каскад має коефіцієнт напруги 0.5 (−6.02 dB), другий – 10 (+20 dB), тому разом це 5 або +13.98 dB. У каскаді коефіцієнти напруги множаться, а відповідні рівні в дБ додаються.[^aac-decibels]

## Detailed explanation

Децибел – логарифмічний спосіб подати відношення двох рівнів потужності; для коефіцієнта напруги за однакового вхідного й вихідного опору використовують `G_dB = 20*log10(V_out/V_in)`. Зворотне перетворення дає `V_out/V_in = 10^(G_dB/20)`. Через логарифм множення коефіцієнтів послідовних каскадів перетворюється на додавання їхніх значень у дБ.[^aac-decibels]

У першому каскаді відношення вихідної напруги до вхідної дорівнює `0.5`, тому `20*log10(0.5) ≈ -6.02 dB`. Для другого каскаду відношення дорівнює `10`, тобто `20*log10(10) = 20 dB`. Це коефіцієнти напруги; назва «підсилює» другого каскаду не скасовує ослаблення першого – обидва множники потрібно врахувати.[^aac-decibels]

Приклад розрахунку:

```text
V_total/V_in = 0.5*10 = 5
G_total = 20*log10(5) ≈ 13.98 dB
G_total = -6.02 dB + 20 dB = 13.98 dB
```

Отже, каскад загалом дає п’ятикратне підвищення напруги, або приблизно `13.98 dB`. Результат в дБ обчислено як для відношення напруги за однакових опорів; якщо опори різні, це саме по собі не визначає коефіцієнт потужності. Типова помилка – додати 0.5 до 10 або додати модулі обох змін у дБ. Треба перемножити лінійні коефіцієнти або додати знакові значення в дБ.[^aac-decibels]

Заокруглення до сотих достатнє для заданих цілих коефіцієнтів; виміряні каскади можуть відхилятися від них через навантаження та допуски компонентів.
