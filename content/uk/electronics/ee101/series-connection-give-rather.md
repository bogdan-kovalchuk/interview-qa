---
id: emb-elee-0026
title: "Чому послідовне з’єднання 10 мкФ і 1 мкФ дає приблизно 0,91 мкФ, а не близько 11 мкФ?"
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

У послідовному колі додаються обернені ємності, тому для 10 мкФ і 1 мкФ `C_total = 10*1/(10+1) ≈ 0.91 мкФ`, а не 11 мкФ. Ємності додаються при паралельному з’єднанні; серійний еквівалент завжди менший за найменшу ємність.[^aac-capacitors-series-parallel]

## Detailed explanation

Послідовне з’єднання 10 мкФ і 1 мкФ має еквівалентну ємність приблизно 0.91 мкФ, а не 11 мкФ.[^aac-capacitors-series-parallel]

Помилка зазвичай виникає через перенесення правила для паралельних конденсаторів на послідовний ланцюжок. Для паралельної конфігурації обидва елементи мають ту саму напругу, а їхні заряди додаються, тож додаються ємності. У послідовній конфігурації однаковий заряд проходить через кожний елемент, а загальна напруга дорівнює сумі падінь напруги. Оскільки `V = Q/C`, менший конденсатор створює більшу частину напруги, тому весь ланцюжок має меншу ємність, ніж будь-який його окремий конденсатор.[^aac-capacitors-series-parallel]

Для двох конденсаторів добуток їхніх ємностей ділять на суму. Підстановка дає `10*1/(10+1) = 10/11`, тобто близько 0.91 мкФ. Результат менший за 1 мкФ – найменшу ємність у парі, що є корисною перевіркою. Округлення до двох значущих цифр достатнє для цього прикладу; реальний номінал і виміряне значення також залежать від допуску компонентів.[^aac-capacitors-series-parallel]

**Типова помилка:** побачити два значення й одразу скласти їх. Спершу визначте топологію: спільні два вузли означають паралельне з’єднання, один спільний проміжний вузол у ланцюжку означає послідовне. Потім перевірте межу: серійний результат не може перевищити найменший конденсатор.[^aac-capacitors-series-parallel] Плутанина часто проявляється як неправдоподібні 11 мкФ у задачі з послідовним ланцюжком; уникнути її допомагає коротка перевірка межі перед тим, як записати відповідь.
