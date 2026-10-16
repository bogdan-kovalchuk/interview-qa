---
id: emb-elee-0046
title: "Як обчислити частоту зрізу простих RC- і RL-фільтрів?"
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
  - source_id: filter-cutoff
    title: "Low-pass Filters | Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/low-pass-filters/
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
