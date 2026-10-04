---
id: emb-elee-0045
title: "Як правильно записати показник експоненти і постійну часу RL-кола?"
description: "Як правильно записати показник експоненти і постійну часу RL-кола?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 39, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: rl-time-constant
    title: "Why L/R and not LR? | RC and L/R Time Constants"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-16/why-l-r-and-not-lr/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтверджує τ = L/R та фізичний зміст сталої часу базового RL-кола."
  - source_id: rl-transient
    title: "Voltage and Current Calculations | RC and L/R Time Constants"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-16/voltage-current-calculations/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Експоненційний перехідний процес і розрахунок струму RL-кола."
---

## Short answer

Для природного спаду струму в RL-колі показник експоненти дорівнює `-t*R/L`, а стала часу `τ = L/R` вимірюється в секундах. Запис `e^(-t*L/R)` і твердження `τ = R/L` переставляють відношення: `R/L` має одиниці `1/s` і є оберненою сталою часу.[^rl-time-constant]

## Detailed explanation

У послідовному RL-колі після від’єднання джерела закон Кірхгофа дає `L*di/dt + R*i = 0`. Розв’язок цього рівняння – `i(t) = I0*e^(-t*R/L)`, де `I0` є струмом на початку спаду. Його також записують як `i(t) = I0*e^(-t/τ)`, якщо `τ = L/R`; обидва записи тотожні, оскільки `1/τ = R/L`.[^rl-transient]

Перевірка розмірностей швидко ловить помилку: генрі дорівнює `Ω*s`, тож `L/R` має одиницю секунди, потрібну часовій сталі. `R/L` натомість має одиницю `1/s`; воно може множити час у показнику експоненти, але не є часом. Мінус означає спад. Для наростання від нуля до усталеного струму з’являється множник `1 - e^(-t/τ)`.[^rl-transient]

Після однієї сталої часу струм спаду становить приблизно 36.8% від початкового, бо `e^-1 ≈ 0.368`. Це модель ідеального індуктора та сталого послідовного опору. Для складнішої лінійної схеми спершу знаходять еквівалентний опір Тевенена, видимий з виводів індуктора; не слід автоматично брати опір лише одного резистора.[^rl-transient]

Приклад розрахунку:
```text
L = 20 mH, R = 10 Ω
τ = L/R = 0.020/10 = 0.002 s = 2 ms
i(2 ms)/I0 = e^-1 ≈ 0.368
```
Отже, за `2 ms` залишається близько 36.8% початкового струму. Типова помилка – перенести `RC`-формулу на індуктор; підстановка одиниць або одного значення `τ` показує, що правильна стала часу є `L/R`.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
