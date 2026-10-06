---
id: emb-elee-0143
title: "Чому той самий стабілізатор (9 В, 5,1 В, 390 Ом) не дає 5,1 В на навантаженні 100 Ом?"
description: "Чому той самий стабілізатор (9 В, 5,1 В, 390 Ом) не дає 5,1 В на навантаженні 100 Ом?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Походження питання: лекція 58, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: nexperia-an90031
    title: "Nexperia AN90031: Zener diodes – physical basics, parameters and application examples"
    url: https://assets.nexperia.com/documents/application-note/AN90031.pdf
    accessed: 2026-10-06
    kind: official
    version: "Rev. 3.0, 7 June 2023"
    applicability: "Вибір R1 = (V_IN - V_Z)/(I_Z(min) + I_LOAD(max)), мінімальний струм стабілітрона приблизно 5 мА для діодів до 17 В, максимальне розсіювання стабілітрона без навантаження P = V_Z*I_Z, те, що базова схема призначена для малих потужностей, а для більших навантажень наведено варіант із біполярним транзистором (V_OUT = V_Z - V_BE); дані наведено для серій Nexperia, інші виробники можуть мати інші числа."
  - source_id: nexperia-bzx84
    title: "Nexperia BZX84 series: voltage regulator diodes (datasheet)"
    url: https://assets.nexperia.com/documents/data-sheet/BZX84_SER.pdf
    accessed: 2026-10-06
    kind: official
    version: "Rev. 7, 1 January 2023"
    applicability: "Параметри BZX84-C5V1: зворотний струм не більший за 2 мкА при V_R = 2 В, P_tot ≤ 250 мВт при T_amb ≤ 25 °C; значення для цієї серії, а не для всіх стабілітронів на 5,1 В."
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Простий стабілітронний стабілізатор: максимальний струм навантаження дорівнює струму послідовного резистора (V_cap - V_Z)/R_limit; при надто великому навантаженні стабілітрон перестає проводити, регуляція зникає, а резистор і навантаження утворюють дільник напруги."
---

## Short answer

Для 5,1 В на 100 Ом потрібно `5.1/100 = 51 mA`, а резистор 390 Ом при `V_out = 5.1 V` пропускає лише `(9 - 5.1)/390 = 10 mA`. Тому припущення `V_out ≈ V_Z` хибне: розрахунок дав би від’ємний `I_Z`, а стабілітрон не може віддавати струм у коло. Стабілітрон не проводить, і вихід задає дільник: `9*100/(390 + 100) ≈ 1.84 V`.[^fiore-rectification]

## Detailed explanation

**Що потрібно й що можливо.** Щоб отримати `5.1 V` на `100 Ом`, навантаженню треба `5.1/100 = 51 mA`. Максимум, який може віддати резистор, коли вихід на рівні `V_Z`, – `I_R = (9 - 5.1)/390 = 10 mA`; це ж і максимальний струм навантаження в такій схемі, коли через стабілітрон нічого не тече.[^fiore-rectification] Різниця велика: 51 мА проти 10 мА. Якщо все ж підставити в баланс струмів, вийде `I_Z = I_R - I_load = 10 - 51 = -41 mA`. Стабілітрон же проводить у пробої лише в один бік, тому від’ємний результат – не фізичний струм, а сигнал, що початкове припущення («вихід тримається на `V_Z`») не виконується.

**Що відбувається насправді.** Навантаження стягує вихід нижче `V_Z`, і стабілітрон виходить із пробою. Нижче напруги пробою він – звичайний діод у зворотному напрямку з малим струмом витоку: для BZX84-C5V1 не більше 2 мкА при `V_R = 2 V`.[^nexperia-bzx84] Порівняно зі струмом у десятки міліампер це можна не враховувати, тож залишаються резистор 390 Ом і навантаження 100 Ом. Вихід задає дільник напруги: `V_out = 9*100/(390 + 100) = 900/490 ≈ 1.84 V`, а струм `9/490 ≈ 18.4 mA`. Перевірка узгодженості: `1.84 V < 5.1 V`, тож стабілітрон і справді не в пробої, і припущення «він не проводить» виконується.[^fiore-rectification]

**Потужності.** На резисторі падає `9 - 1.84 = 7.16 V`, тож `P_R = 7.16²/390 ≈ 132 mW`, а на навантаженні `1.84²/100 ≈ 34 mW`; разом `≈ 165 mW`, що збігається з `9*18.4 mA`. Резистор у типовому корпусі на 1/8 Вт (125 мВт) уже перевантажений, тож «непрацюючий» стабілізатор ще й може перегрітися.

**Як виправити.** Спокуса – зменшити R. За формулою Nexperia `R1 = (V_IN - V_Z)/(I_Z(min) + I_LOAD(max))`, для мінімуму 5 мА й навантаження 51 мА вийде `3.9/(0.005 + 0.051) ≈ 69.6 Ом`, тобто 68 Ом.[^nexperia-an90031] Але без навантаження через стабілітрон піде `3.9/68 ≈ 57 mA`, а `P_Z = 5.1*0.057 ≈ 293 mW` – більше за допустимі 250 мВт для BZX84.[^nexperia-bzx84] Сама Nexperia зазначає, що базова схема призначена для малих потужностей, а для більших навантажень пропонує додати біполярний транзистор.[^nexperia-an90031] Інший шлях – стабілізатор без шунтування струму через стабілітрон.

**Типові помилки:**

- Вважати, що `V_out = V_Z` завжди, і не перевіряти, чи вистачає струму резистора.
- Прийняти від’ємний `I_Z` за результат, а не за ознаку хибного припущення.
- Рахувати дільник без перевірки, що `V_out < V_Z`.
- «Лікувати» проблему зменшенням R без перевірки потужності стабілітрона.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
