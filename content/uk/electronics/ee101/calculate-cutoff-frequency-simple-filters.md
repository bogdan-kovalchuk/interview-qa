---
id: emb-elee-0046
title: "Як обчислити частоту зрізу простих RC- і RL-фільтрів?"
description: "Як обчислити частоту зрізу простих RC- і RL-фільтрів?"
track: electronics
section: ee101
level: junior
type: concept
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
  - source_id: filter-cutoff
    title: "Low-pass Filters | Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/low-pass-filters/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Частота зрізу RC-фільтра, рівень 70.7% та вплив опору навантаження."
---

## Short answer

Для простого RC-фільтра першого порядку `f_c = 1/(2*π*R*C)`, а для простого RL-фільтра `f_c = R/(2*π*L)`. Ці формули припускають зазначену базову топологію та відсутність навантаження, яке змінює частоту зрізу.[^filter-cutoff]

## Detailed explanation

Частота зрізу однополюсного фільтра – частота, де амплітуда падає до `1/√2`, або приблизно 70.7% від рівня в смузі пропускання. У простому RC-колі `τ = R*C`, звідки `f_c = 1/(2*π*τ)`. У простому RL-колі `τ = L/R`, тому `f_c = 1/(2*π*τ) = R/(2*π*L)`. Одиниця обох виразів для `f_c` – `1/s`, тобто герц.[^filter-cutoff]

Топологія має значення: для RC low-pass резистор стоїть послідовно, а конденсатор з’єднаний із вихідним вузлом; для RL low-pass послідовний індуктор працює з опором навантаження. Додавання вхідного чи вихідного опору змінює опір, який бачить реактивний елемент, отже проста формула з номіналом одного резистора може вже не описувати реальний полюс.[^filter-cutoff]

Приклад розрахунку для ненавантаженого RC low-pass:
```text
R = 1 kΩ, C = 100 nF
f_c = 1/(2*π*R*C)
f_c = 1/(2*π*1000*100e-9) ≈ 1592 Hz
```
Тобто оцінка становить `1.59 kHz`. Реальні компоненти також мають допуски й паразитні параметри, а котушка має опір обмотки. Для складнішої схеми потрібно побудувати передавальну функцію або перевірити частотний відгук симуляцією та вимірюванням.[^filter-cutoff]

**Типова помилка:** підставляти номінали, не уточнивши, де знімається вихід і чи під’єднано навантаження. Спершу зафіксуйте схему, потім перевірте розмірність та порівняйте розрахунок із частотним розгортанням.

## Sources

<!-- generated from frontmatter -->
