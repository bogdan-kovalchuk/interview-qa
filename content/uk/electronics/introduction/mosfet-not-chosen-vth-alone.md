---
id: emb-elintro-0250
title: "Чому не можна вибирати MOSFET лише за `V_th`?"
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
  - source_id: onsemi-fds2582-datasheet
    title: "onsemi: FDS2582 N-Channel MOSFET datasheet"
    url: https://www.onsemi.com/download/data-sheet/pdf/fds2582-d.pdf
---

## Short answer

`V_th` задають за малим тестовим струмом, тому вона не гарантує низького `R_DS(on)`.[^onsemi-fds2582-datasheet] Для ключа перевіряйте `R_DS(on)` за потрібної `V_GS` у datasheet.[^onsemi-fds2582-datasheet]

## Detailed explanation

Порогова напруга gate-to-source `V_th` (у багатьох datasheet позначена `V_GS(th)`) задає умову, за якої канал щойно починає проводити визначений малий тестовий струм. Це не напруга повного відкриття й не обіцянка, що MOSFET пропустить номінальний струм із малими втратами. Точне визначення та тестовий струм зазначають у datasheet; значення залежить від екземпляра й температури.[^onsemi-fds2582-datasheet]

Для перемикального режиму важливий `R_DS(on)` за реально доступної `V_GS`. Провідникові втрати приблизно дорівнюють `P = I_D²*R_DS(on)`, коли MOSFET уже працює як низькоомний ключ; якщо gate отримує недостатню напругу, транзистор може лишатися в лінійній області, де одночасно значні струм і `V_DS`, а отже, нагрів. У таблицях ці дві характеристики часто виміряні за різних умов, тому не можна підставляти поріг замість напруги керування.[^onsemi-fds2582-datasheet]

Наприклад, у datasheet FDS2582 поріг вимірюють при `I_D = 250 µA`, тоді як `R_DS(on)` задають при `V_GS = 10 V` і амперах струму. Це конкретний приклад, а не універсальний тест для всіх транзисторів; він показує, чому однієї цифри `V_GS(th)` недостатньо для вибору. Якщо контролер дає лише 3.3 V, знайдіть гарантований рядок `R_DS(on)` при відповідній напрузі або оберіть іншу деталь.[^onsemi-fds2582-datasheet]

**Типова помилка:** бачити `V_th = 2 V` і вирішувати, що ключ гарантовано повністю ввімкнеться від 3.3 V. Перевіряйте межі `V_GS(th)`, тестові умови `R_DS(on)`, струм, температуру та тепловий опір корпусу перед оцінкою втрат.[^onsemi-fds2582-datasheet]

Приклад перевірки: якщо навантаження бере `2 A`, а таблиця гарантує `R_DS(on) = 0.1 Ω` саме при вашій напрузі керування, ідеальна оцінка втрат у каналі становить `P = 2²*0.1 = 0.4 W`. Якщо такого рядка для доступної напруги немає, datasheet не підтверджує розрахунок для цього керування.
