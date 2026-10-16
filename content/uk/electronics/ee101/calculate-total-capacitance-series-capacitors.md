---
id: emb-elee-0025
title: "Як обчислити загальну ємність послідовних конденсаторів?"
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
  - source_id: aac-capacitors-series-parallel
    title: "All About Circuits textbook: Series and Parallel Capacitors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/series-and-parallel-capacitors/
---

## Short answer

Для послідовного з’єднання додають обернені ємності: `1/C_total = 1/C_1 + 1/C_2 + ...`; для двох це `C_total = C_1*C_2/(C_1+C_2)`. Наприклад, 10 мкФ і 22 мкФ дають `220/32 = 6.875 мкФ`, тобто приблизно 6.88 мкФ. Для `n` однакових конденсаторів результат дорівнює ємності одного, поділеній на `n`.[^aac-capacitors-series-parallel]

## Detailed explanation

Еквівалентна ємність послідовного ланцюжка визначається сумою обернених ємностей його конденсаторів.[^aac-capacitors-series-parallel]

У послідовному колі через усі елементи проходить однаковий заряд за модулем. Для кожного конденсатора виконується співвідношення `Q = C*V`, тому за однакового заряду менша ємність потребує більшої напруги. Якщо замінити весь ланцюжок одним елементом, той самий заряд має створювати ту саму загальну напругу; звідси й правило додавання обернених ємностей. Воно не означає, що напруги на окремих реальних конденсаторах завжди стабільно діляться лише за їхніми номіналами: у тривалому режимі впливають допуск, витік та зовнішнє балансування.[^aac-capacitors-series-parallel]

Для двох елементів формулу можна перетворити на добуток, поділений на суму. Це зручно для ручного розрахунку, але одиниці треба узгодити: якщо обидва значення задані в мкФ, результат також буде в мкФ. Серійний еквівалент завжди менший за найменшу окрему ємність; у паралельному з’єднанні, навпаки, ємності додаються.[^aac-capacitors-series-parallel]

Приклад розрахунку:

```text
C_total = 1 / (1/10 + 1/22) мкФ
C_total = (10*22)/(10+22) мкФ
C_total = 220/32 мкФ = 6.875 мкФ ≈ 6.88 мкФ
```

**Типова помилка:** механічно додати значення, як для паралельного з’єднання. Перевірка результату проста: відповідь має бути меншою за 10 мкФ, інакше переплутано конфігурацію або формулу.
