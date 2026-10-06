---
id: emb-elee-0156
title: "Яку вхідну напругу стабілізатора порівнюють із dropout, якщо на вході є пульсації?"
description: "Яку вхідну напругу стабілізатора порівнюють із dropout, якщо на вході є пульсації?"
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
    applicability: "Визначення dropout (регулятор перестає стабілізувати за подальшого зменшення входу; у dropout PMOS pass element поводиться як резистор, V_dropout = I_o*R_on) і визначення PSRR як V_o,ripple/V_i,ripple. Записка про LDO; наведені в ній значення dropout – лише приклади конкретних мікросхем."
  - source_id: ti-tps752q1-datasheet
    title: "Texas Instruments TPS752-Q1 datasheet"
    url: https://www.ti.com/lit/ds/symlink/tps752-q1.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Datasheet конкретного LDO: dropout приблизно пропорційний струму навантаження, залежить від температури переходу (графік), а мінімальну вхідну напругу задає примітка V_I(min) = V_O(max) + V_DO(max load). Значення стосуються лише TPS752-Q1."
---

## Short answer

Порівнюють мінімальну миттєву вхідну напругу, тобто дно пульсацій, а не середнє значення: потрібно `V_in,min > V_out + V_dropout`. Dropout залежить від струму навантаження й температури, тож його беруть з datasheet для найгіршого режиму, зокрема для максимального струму. Коли дно опускається нижче, регулятор у ці моменти перестає стабілізувати, і провали входу проходять на вихід.[^ti-slva079][^ti-tps752q1-datasheet]

## Detailed explanation

Dropout – це різниця вхід–вихід, за якої регулятор перестає стабілізувати вихід під час подальшого зменшення вхідної напруги.[^ti-slva079] Умова `V_in - V_out >= V_dropout` має виконуватися в кожен момент часу, а не в середньому: pass element реагує на миттєве значення входу; за пульсацій 100–120 Гц вихідна ємність LDO зазвичай не здатна покрити провал, тож стабілізація порушується в ці моменти (дуже короткі провали вихідна ємність може згладити). Тому в розрахунку беруть `V_in,min` – найнижче значення вхідної напруги за період пульсацій. Для випрямляча з конденсатором це дно між зарядними імпульсами, а не середнє значення постійної складової.

Сама величина dropout не стала. У PMOS pass element вона дорівнює `V_dropout = I_o*R_on`, тож росте зі струмом навантаження.[^ti-slva079] У datasheet TPS752-Q1 сказано, що dropout приблизно пропорційний вихідному струму, а також наведено його залежність від температури переходу; мінімальну вхідну напругу там задано як `V_I(min) = V_O(max) + V_DO(max load)`.[^ti-tps752q1-datasheet] Тож перевіряти слід dropout для максимального струму й для температури з datasheet, за якої він найбільший, а не типове значення за малого навантаження. Нижню межу напруги джерела (допуск мережі, падіння на діодах випрямляча) також варто закласти в `V_in,min`.

Поки вхід вище порога, регулятор послаблює пульсації з коефіцієнтом PSRR, який визначають як `V_o,ripple/V_i,ripple`.[^ti-slva079] Нижче порога регулятор уже не стабілізує, тож цифри PSRR із datasheet там не діють: вихід починає слідувати за входом, і дно пульсацій з’являється на виході, наприклад з частотою 100 Гц для двопівперіодного випрямляча від мережі 50 Гц.

**Приклад (ілюстративні числа):** `V_out = 5 V`, dropout для максимального струму `0.5 V`, отже потрібно `V_in,min > 5.5 V`. Якщо середня напруга після випрямляча `6.5 V`, а розмах пульсацій `2 V` (від `5.5 V` до `7.5 V`), то перевірка за середнім дає «запас 1 V» (`6.5 - 5.5`), але за дном запас нульовий: `5.5 - 5.5 = 0 V`. Найменше просідання мережі чи зростання струму вже виводить регулятор зі стабілізації. Виправити це можна, лише підвищивши саме дно: зменшивши пульсації (більша ємність, менший струм) або піднявши середню напругу; після цього `V_in,min` слід перерахувати.

**Типові помилки:**

- Порівнювати dropout із середньою напругою на вході замість `V_in,min`.
- Брати типове значення dropout за малого струму замість значення для максимального струму й найгіршої температури.
- Не враховувати допуск і просідання мережі, падіння на діодах та перехідні режими під час визначення `V_in,min`.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
