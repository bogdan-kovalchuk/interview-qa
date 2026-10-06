---
id: emb-elee-0160
title: "Як обчислити тепловий опір стабілізатора з радіатором?"
description: "Як обчислити тепловий опір стабілізатора з радіатором?"
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
  - source_id: ti-sboa020
    title: "Texas Instruments (Burr-Brown) SBOA020 / AB-037: Mounting Considerations for TO-3 Packages"
    url: https://www.ti.com/lit/an/sboa020/sboa020.pdf
    accessed: 2026-10-06
    kind: official
    version: "SBOA020 (AB-037), March 1992"
    applicability: "Модель T_J = T_A + P_D*θ_JA, θ_JA = θ_JC + θ_CH + θ_HA (θ_CH – опір контакту корпус–радіатор); таблиця II: орієнтовні θ_CH для корпусу TO-3 (голий контакт 0,5–1,0, паста 0,1–0,2, Kapton із пастою 0,3–0,5, слюда без пасти 1,0–1,5 °C/Вт); електроізоляційні прокладки через діелектричний шар зазвичай мають гірший θ_CH, ніж паста. Числа стосуються TO-3; для TO-220 вони інші."
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
    accessed: 2026-10-06
    kind: official
    version: "SNOSBT0L, September 2016"
    applicability: "Примітка до Absolute Maximum Ratings: P_DMAX = (T_JMAX - T_A)/θ_JA з T_JMAX 125 або 150 °C, thermal shutdown понад 150 °C; з радіатором θ_JA є сумою θ_JC корпусу (4 °C/Вт для TO-3 і TO-220) та опору «корпус–довкілля» радіатора; для TO-220 примітка дає θ_JA 54 °C/Вт, а таблиця Thermal Information – 23,9 °C/Вт (значення не збігаються); на першій сторінці: «Tab/Case is Ground or Output»; quiescent current до 6 мА (LM340A, 25 °C). Значення стосуються родини LM340/LM7805, не всіх стабілізаторів."
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA079, October 1999"
    applicability: "Розсіювана стабілізатором потужність P_D = (V_i - V_o)*I_o; quiescent (ground) current визначено як різницю вхідного й вихідного струмів I_q = I_i - I_o; вираз для ККД; формула P_D(max) = (T_Jmax - T_A)/R_θJA. Записка про LDO: її числа й приклади стосуються LDO, а не 7805."
  - source_id: ti-spra953
    title: "Texas Instruments SPRA953: Semiconductor and IC Package Thermal Metrics"
    url: https://www.ti.com/lit/pdf/spra953
    accessed: 2026-10-06
    kind: official
    version: "SPRA953D, March 2024"
    applicability: "R_θJA залежить не лише від корпусу, а й від плати та умов вимірювання (плата діє як радіатор; у JEDEC-вимірюваннях у спокійному повітрі 70–95 % потужності відводить плата, а не корпус); дизайн плати має «сильний» вплив на R_θJA (таблиця 1-1). Загальна записка: не дає значень для конкретних плат чи адаптерів."
---

## Short answer

Тепловий опір від кристала до повітря – сума послідовних ділянок: `θ_JA = θ_JC + θ_CS + θ_SA` (°C/Вт), тобто кристал–корпус, корпус–радіатор (контакт із термоінтерфейсом) і радіатор–повітря.[^ti-sboa020] Паста зменшує `θ_CS` порівняно з голим контактом, а електроізоляційна прокладка зазвичай дає більший `θ_CS`, ніж паста.[^ti-sboa020] Ізоляція буває потрібна, бо tab або корпус стабілізатора з’єднаний із землею чи з виходом.[^ti-lm340]

## Detailed explanation

Тепло, яке розсіює стабілізатор, іде від кристала до повітря послідовним ланцюгом, і тепловий опір ділянок додається так само, як опір резисторів. Для лінійного стабілізатора потужність дорівнює `P = (V_in - V_out)*I_out` (плюс невелика частка `V_in*I_q`),[^ti-slva079] а температура кристала – `T_J = T_A + P*θ_JA`, де `θ_JA = θ_JC + θ_CS + θ_SA`. TI записує ту саму модель як `θ_JC + θ_CH + θ_HA`, де `θ_CH` – контакт «корпус–радіатор».[^ti-sboa020] Datasheet LM340 каже те саме: з радіатором `θ_JA` складається з `θ_JC` корпусу та опору «корпус–довкілля» радіатора.[^ti-lm340]

Кожну ланку беруть з іншого місця. `θ_JC` дає datasheet корпусу, `θ_SA` – каталог радіатора, а `θ_CS` залежить від монтажу: між корпусом і радіатором лишаються повітряні зазори, тож їх заповнюють пастою або прокладкою. Для корпусу TO-3 TI наводить такі діапазони: голий контакт 0,5–1,0 °C/Вт, паста 0,1–0,2, Kapton із пастою 0,3–0,5, слюда без пасти 1,0–1,5 °C/Вт.[^ti-sboa020] Для TO-220 числа інші, але порядок ланок той самий.

Електрична ізоляція – окрема причина прокладки. Tab або корпус стабілізатора з’єднаний із землею чи з виходом залежно від виконання,[^ti-lm340] тому спільний радіатор може замкнути ці вузли, і між корпусом та радіатором ставлять ізоляційну прокладку. Через діелектричний шар така прокладка, за TI, зазвичай гірша за пасту за `θ_CS`.[^ti-sboa020] Не варто й підставляти `θ_JA` корпусу без радіатора: цей параметр залежить від плати та умов вимірювання,[^ti-spra953] а в datasheet LM340 для TO-220 наведено навіть різні значення (54 °C/Вт у примітці й 23,9 °C/Вт у таблиці).[^ti-lm340]

**Приклад.** 7805 у TO-220, `V_in = 12 В`, `I_out = 0.5 А`, `T_A = 40 °C`, бажана межа `T_J = 125 °C` (datasheet припускає `T_JMAX` 125 або 150 °C, а понад 150 °C вмикається thermal shutdown).[^ti-lm340] Потужність `P = (12 - 5)*0.5 = 3.5 Вт`; спокійний струм (до 6 мА за datasheet LM340A) додає менш ніж 0,1 Вт. Допустимий `θ_JA = (125 - 40)/3.5 ≈ 24.3 °C/Вт`. Беремо `θ_JC = 4 °C/Вт` (примітка datasheet для TO-220) і `θ_CS = 1 °C/Вт` (ілюстративне припущення для ізоляційної прокладки), тоді `θ_SA ≤ 24.3 - 4 - 1 ≈ 19 °C/Вт`. Перевірка: `T_J = 40 + 3.5*(4 + 1 + 19) = 124 °C`.

**Типові помилки:**

- Додавати `θ_SA` до `θ_JA` корпусу з datasheet: `θ_JA` уже містить шлях до повітря, а з радіатором потрібен `θ_JC`.[^ti-lm340]
- Вважати `θ_CS` нульовим або забувати, що ізоляційна прокладка гірша за пасту.[^ti-sboa020]
- Переносити `θ_JA` з datasheet на власну плату, не перевіривши умов вимірювання.[^ti-spra953]

## Sources

<!-- generated from frontmatter -->
