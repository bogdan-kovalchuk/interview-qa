---
id: emb-elintro-0175
title: "Який розділ даташиту ніколи не можна перевищувати?"
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
  - source_id: ti-tps752q1-datasheet
    title: "Texas Instruments TPS752-Q1 datasheet"
    url: https://www.ti.com/lit/ds/symlink/tps752-q1.pdf
---

## Short answer

<span class="warn">Absolute Maximum Ratings</span> задає межі стресу, які не слід перевищувати: перевищення може пошкодити компонент, але навіть робота всередині цих меж не гарантує нормальної функціональності. Для штатної роботи дотримуйтеся `Recommended Operating Conditions` і враховуйте derating та теплові умови.[^ti-tps752q1-datasheet]

## Detailed explanation

`Absolute Maximum Ratings` – таблиця граничних електричних і теплових навантажень, які компонент може витримати без негайного руйнування за зазначених умов. Вона не визначає режим, у якому виробник гарантує нормальну роботу: для цього призначений розділ `Recommended Operating Conditions` або його аналог. Datasheet TI прямо застерігає, що вихід за абсолютні межі може спричинити постійне пошкодження, а функціонування поза рекомендованими умовами не гарантується.[^ti-tps752q1-datasheet]

Тому є дві перевірки. Спершу переконайтеся, що жоден перехідний процес не перетинає абсолютну межу – наприклад, напруга на вході не перевищує максимум і температура переходу не виходить за межу. Потім переконайтеся, що звичайний режим лежить у рекомендованому діапазоні. Робота нижче абсолютного максимуму, але поза рекомендованою областю може не пошкодити деталь одразу, проте її характеристики та надійність там не обіцяні.[^ti-tps752q1-datasheet]

Граничне значення не можна читати без приміток. Допустима потужність часто залежить від температури середовища, корпусу, потоку повітря й площі міді на платі; тривале перебування біля межі також може скоротити надійність. Практичний розрахунок має врахувати worst-case напругу, струм, імпульси та нагрівання, після чого потрібен запас, або derating, відповідно до вимог виробу й системи.[^ti-tps752q1-datasheet]

Приклад: якщо datasheet задає абсолютний максимум живлення `5.5 V`, це не означає, що `5.5 V` є рекомендованою напругою для тривалої роботи. Робочий інтервал шукають окремо в рекомендованих умовах і з урахуванням допуску джерела та перехідних процесів.[^ti-tps752q1-datasheet]

**Типова помилка:** трактувати абсолютний максимум як штатний setpoint або як межу, яку безпечно регулярно торкатися. Проєктуйте за рекомендованими умовами й не допускайте навіть коротких виходів за абсолютну межу.
