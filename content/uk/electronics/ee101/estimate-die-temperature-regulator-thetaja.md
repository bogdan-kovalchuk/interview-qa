---
id: emb-elee-0159
title: "Як оцінити температуру кристала лінійного стабілізатора 12 В -> 5 В при 0,2 А, якщо `theta_JA` = 60 °C/Вт, `T_a` = 25 °C?"
description: "Як оцінити температуру кристала лінійного стабілізатора 12 В -> 5 В при 0,2 А, якщо `theta_JA` = 60 °C/Вт, `T_a` = 25 °C?"
track: electronics
section: ee101
level: junior
type: concept
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
    applicability: "Походження питання: лекція 61, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA079, October 1999"
    applicability: "Потужність розсіювання лінійного регулятора P_D = (V_i - V_o)*I_o, визначення quiescent current I_q = I_i - I_o, обмеження максимальною junction temperature і формула P_D(max) = (T_Jmax - T_A)/R_θJA. Записка про LDO; не стосується імпульсних перетворювачів і не задає θ_JA для конкретного корпусу."
  - source_id: ti-spra953d
    title: "Texas Instruments SPRA953D: Semiconductor and IC Package Thermal Metrics"
    url: https://www.ti.com/lit/an/spra953d/spra953d.pdf
    accessed: 2026-10-06
    kind: official
    version: "SPRA953D, March 2024"
    applicability: "Визначення R_θJA на стандартизованій тестовій платі, формула T_J = T_A + R_θJA*Power, застереження, що R_θJA залежить від плати й системи і пряме застосування до реальної плати може дати хибні значення, та поняття R_θJA(effective). Не задає значення θ_JA для конкретного корпусу чи плати."
---

## Short answer

Для лінійного стабілізатора втрати `P = (12 - 5)*0.2 = 1.4 W`, тож `T_j = T_a + P*theta_JA = 25 + 1.4*60 = 109 °C`.[^ti-slva079][^ti-spra953d] Результат порівнюють з максимальною junction temperature з datasheet із запасом.[^ti-slva079] `theta_JA` залежить від плати й умов охолодження, тому це лише оцінка, а не універсальна стала.[^ti-spra953d]

## Detailed explanation

Оцінка складається з двох кроків: електричної потужності в тепло і тепла в температуру. У лінійному стабілізаторі різниця `V_in - V_out` падає на pass element, тому розсіювана потужність `P_D = (V_i - V_o)*I_o`; для 12 В, 5 В і 0,2 А це `7*0.2 = 1.4 W`.[^ti-slva079] Точніше, до цього додається ще `V_i*I_q`, де `I_q = I_i - I_o` – quiescent current самого регулятора, але за 0,2 А цей доданок зазвичай малий порівняно з 1,4 Вт.[^ti-slva079] Формула `P = (V_in - V_out)*I_out` справедлива лише для лінійного регулятора: в імпульсному перетворювачі втрати мають інші механізми й не дорівнюють `(V_in - V_out)*I_out`.

Тепловий опір `theta_JA` показує, на скільки градусів кристал гарячіший за навколишнє повітря на кожен ват розсіюваної потужності: його вимірюють як підвищення температури, поділене на потужність, за стандартизованих умов.[^ti-spra953d] Звідси `T_j = T_a + P*theta_JA`, і для наших даних `1.4*60 = 84 °C` підвищення, тобто `T_j = 25 + 84 = 109 °C`.[^ti-spra953d] Це аналог закону Ома: потужність відіграє роль струму, тепловий опір – опору, різниця температур – напруги.

Головне обмеження – сама величина `theta_JA`. TI наголошує, що `R_θJA` вимірюють на стандартній тестовій платі, а в реальній системі вона залежить від конструкції плати, тож пряма підстановка в `T_J = T_A + R_θJA*Power` може дати суттєво хибні значення; у JEDEC-вимірюваннях у спокійному повітрі 70–95 % потужності відводиться через плату, а не через поверхню корпусу.[^ti-spra953d] Тому число 109 °C – оцінка першого наближення. Для точнішого результату використовують `R_θJA(effective)` для конкретної системи, отриману з моделювання чи вимірювань.[^ti-spra953d]

Результат потрібно порівняти з межею. Для LDO зазначають максимальну junction temperature, а допустима потужність `P_D(max) = (T_Jmax - T_A)/R_θJA`; фактична потужність не має її перевищувати.[^ti-slva079] **Приклад (ілюстративно, `T_Jmax = 125 °C`):** `P_D(max) = (125 - 25)/60 = 1.67 W`, отже 1,4 Вт допустимо, але запас за температурою лише `125 - 109 = 16 °C`. Якщо ж температура в корпусі пристрою `T_a = 50 °C`, то `T_j = 50 + 84 = 134 °C` – вище за 125 °C; максимальна `T_a` для цього режиму `125 - 84 = 41 °C`. Отже, результат, який проходить за 25 °C, може не пройти в теплому корпусі.

**Типові помилки:**

- Використовувати значення `theta_JA` з datasheet як точну константу для власної плати.
- Брати `T_a = 25 °C` замість найгіршої температури всередині корпусу пристрою.
- Застосовувати `P = (V_in - V_out)*I_out` до імпульсного перетворювача.
- Не залишати запас до максимальної `T_j` і не перераховувати за максимальної вхідної напруги й струму.

## Sources

<!-- generated from frontmatter -->
