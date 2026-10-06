---
id: emb-elee-0165
title: "Чому 7805 не дає 5 В при вхідній напрузі рівно 5 В?"
description: "Чому 7805 не дає 5 В при вхідній напрузі рівно 5 В?"
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
    applicability: "Походження питання: лекція 62, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
    accessed: 2026-10-06
    kind: official
    version: "SNOSBT0L, September 2016"
    applicability: "Таблиця LM340/LM7805 (V_O = 5 В, V_I = 10 В): dropout 2 В (типово) за I_O = 1 А і T_J = 25 °C; вхідна напруга, потрібна для збереження line regulation, – 7,5 В (T_J = 25 °C, I_O ≤ 1 А). У datasheet є й графіки Dropout Characteristics і Dropout Voltage, яких тут не переказано. Значення стосуються родини LM340/LM7805, не інших стабілізаторів (зокрема LDO)."
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA079, October 1999"
    applicability: "Визначення dropout: різниця вхід–вихід, за якої схема перестає стабілізувати за подальшого зменшення входу; потужність, що розсіюється стабілізатором, P_D = (V_i - V_o)*I_o. Записка про LDO: її приклади (PMOS pass element, TPS767xx) стосуються LDO, а не 7805."
---

## Short answer

7805 – не LDO: його dropout типово 2 В за струму 1 А і `T_J = 25 °C`, а datasheet вимагає вхід від 7,5 В, щоб зберегти line regulation.[^ti-lm340] Вхід 5 В не дає жодного запасу над виходом 5 В, тож стабілізатор поза режимом стабілізації, і вихід нижчий за 5 В.[^ti-slva079]

## Detailed explanation

Лінійний стабілізатор вмикає між входом і виходом регулювальний елемент, і той лишається працездатним, лише поки на ньому є достатня напруга. Різницю вхід–вихід, за якої схема перестає стабілізувати під час подальшого зменшення входу, називають dropout.[^ti-slva079] Тому для 5 В на виході вхід має перевищувати 5 В щонайменше на dropout: за входу 5 В різниця дорівнює 0 В і менша за будь-який dropout.

7805 не належить до LDO. У datasheet TI для родини LM340/LM7805 dropout становить типово 2 В за `I_O = 1 А` і `T_J = 25 °C`, а вхідна напруга, потрібна для збереження line regulation, – 7,5 В (за `T_J = 25 °C` і `I_O ≤ 1 А`).[^ti-lm340] Отже, за 1 А мінімум становить орієнтовно `5 + 2 = 7 В` типово, а гарантований datasheet поріг – 7,5 В. Dropout залежить від струму й температури, тож для інших умов дивляться відповідні графіки datasheet, а не це одне число.

**Приклад.** Вхід 5 В, навантаження 1 А. У режимі dropout різниця вхід–вихід дорівнює dropout, тому вихід приблизно `V_in - V_dropout ≈ 5 - 2 = 3 В` (типово) і не стабілізований: його положення задає вхід, а не опорна напруга. За меншого струму dropout інший, але 5 В на виході однаково недосяжні, бо запас нульовий. Підвищення входу до 9 В дає запас `9 - 5 = 4 В`, проте потужність `P_D = (V_in - V_out)*I_out`[^ti-slva079] за 1 А зростає до 4 Вт, а за 7,5 В – лише 2,5 Вт. Тож вхід беруть із запасом над мінімумом, але не з надлишком, який перетворюється на тепло.

Якщо вхід реально близький до 5 В (наприклад, шина 5,5 В), 7805 не підходить, і потрібен стабілізатор із малим dropout; про порівняння дна пульсацій із dropout див. `qid:emb-elee-0156`.

**Типові помилки:**

- Вважати, що стабілізатор 5 В працює від 5 В на вході: для 7805 потрібен запас щонайменше кілька вольтів.
- Брати 2 В як сталий dropout: datasheet наводить його для 1 А й 25 °C.
- Порівнювати поріг із середнім входом, а не з найнижчою миттєвою напругою на вході.
- Піднімати вхід «про запас»: зайва напруга стає теплом у стабілізаторі.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
