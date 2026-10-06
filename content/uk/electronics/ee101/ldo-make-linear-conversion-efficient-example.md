---
id: emb-elee-0155
title: "Чи робить LDO лінійне перетворення ефективним, наприклад 12 В -> 3,3 В?"
description: "Чи робить LDO лінійне перетворення ефективним, наприклад 12 В -> 3,3 В?"
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
    applicability: "Походження питання: лекція 60, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
    applicability: "Визначення dropout (у dropout PMOS pass element поводиться як резистор, V_dropout = I_o*R_on), формула ефективності LDO з урахуванням quiescent current, потужність розсіювання (V_i - V_o)*I_o і обмеження через максимальну junction temperature. Записка про LDO; не задає тепловий опір конкретної плати чи корпусу."
---

## Short answer

Ні. Низький dropout лише дозволяє регулятору працювати з малою різницею вхід–вихід, а не робить перетворення ефективним. Увесь струм навантаження проходить через регулятор, і на ньому розсіюється приблизно `P = (V_in - V_out)*I_out`, а ефективність обмежена відношенням `V_out/V_in`. Для 12 В до 3,3 В це близько 27,5 %, решта стає теплом.[^ti-slva079]

## Detailed explanation

LDO – це лінійний регулятор: його pass element працює як керований опір, увімкнений послідовно з навантаженням. Весь струм навантаження `I_out` проходить через цей елемент, тому різниця `V_in - V_out` падає саме на ньому, і розсіюється потужність `P = (V_in - V_out)*I_out`.[^ti-slva079] Слово «low» у назві стосується мінімальної різниці напруг, за якої регулятор ще стабілізує вихід: у dropout PMOS pass element поводиться як резистор, і `V_dropout = I_o*R_on`.[^ti-slva079] Це нижня межа робочої області, а не оцінка втрат за реальної різниці, яка може бути набагато більшою.

Ефективність LDO визначають як `η = I_o*V_o/((I_o + I_q)*V_i)`, де `I_q = I_i - I_o` – quiescent current, тобто струм, що не доходить до навантаження.[^ti-slva079] Навіть коли `I_q` дуже малий, ефективність не перевищує `V_o/V_i`: різниця вхід–вихід, за словами TI, є внутрішнім чинником ефективності незалежно від навантаження.[^ti-slva079] Тому низький dropout корисний переважно тоді, коли вхід лише трохи вищий за вихід, наприклад під час живлення 3,3 В від акумулятора, що розряджається, – там малі й втрати.

**Приклад:** `V_in = 12 V`, `V_out = 3.3 V`, `I_out = 0.1 A`. Споживана потужність `12*0.1 = 1.2 W`, корисна `3.3*0.1 = 0.33 W`, тепло `1.2 - 0.33 = 0.87 W`; ефективність `3.3/12 = 27.5%` (без `I_q`). За `I_out = 0.3 A` тепло дорівнює `(12 - 3.3)*0.3 = 2.61 W`; для ілюстративного `θ_JA = 60 °C/W` це підвищення температури кристала приблизно на `2.61*60 = 156.6 °C` над навколишньою, тобто такий режим без радіатора неприйнятний (див. також `qid:emb-elee-0159`). Для порівняння, з входом 5 В за тих самих 0,1 А втрати становлять `(5 - 3.3)*0.1 = 0.17 W`, а ефективність `3.3/5 = 66%`. Datasheet задає максимальну junction temperature, і фактична потужність має бути не більшою за `P_D(max) = (T_Jmax - T_A)/R_θJA`.[^ti-slva079]

Якщо різниця напруг велика, а струм помітний, ефективнішим рішенням зазвичай буде імпульсний перетворювач або попередній понижувальний каскад перед LDO; LDO лишають там, де важливі простота й низький шум, а тепло прийнятне. Розрахунок потрібно робити для найгіршого випадку: розсіювання максимальне за найвищої вхідної напруги й найбільшого струму.

**Типові помилки:**

- Вважати, що «low dropout» означає малі втрати: dropout – лише нижня межа різниці напруг.
- Оцінювати ефективність лише за `I_q` і не враховувати відношення `V_out/V_in`.
- Рахувати нагрів за номінальною вхідною напругою, а не за максимальною, і за середнім, а не за піковим струмом.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
