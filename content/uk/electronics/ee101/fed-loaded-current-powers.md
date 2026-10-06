---
id: emb-elee-0164
title: "7805 живиться від 9 В і навантажений резистором 100 Ом. Які струм і потужності?"
description: "7805 живиться від 9 В і навантажений резистором 100 Ом. Які струм і потужності?"
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
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA079, October 1999"
    applicability: "Розсіювана стабілізатором потужність P_D = (V_i - V_o)*I_o; quiescent (ground) current визначено як різницю вхідного й вихідного струмів I_q = I_i - I_o; ККД = I_o*V_o/((I_o + I_q)*V_i). Записка про LDO: її числа й приклади стосуються LDO, а не 7805."
  - source_id: ti-ua78
    title: "TI: uA7805, uA7808, uA7810, uA7812, uA7815, uA7824 positive-voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/ua78.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVS056P, January 2015"
    applicability: "Для uA7805 (25 °C): вихідна напруга 4,8–5,2 В (типово 5 В), bias current 4,2 мА (типово) і 8 мА (максимум), dropout 2 В (типово) за 1 А, рекомендована вхідна напруга 7–25 В, вихідний струм до 1,5 А. Значення стосуються родини uA78xx від TI, не 7805 інших виробників."
---

## Short answer

Вихід 7805 – 5 В, тому `I = 5/100 = 0.05 А`, тобто 50 мА, а резистор розсіює `P = V²/R = 25/100 = 0.25 Вт`; його беруть із запасом, наприклад 0,5 Вт. Стабілізатор розсіює `(9 - 5)*0.05 = 0.2 Вт`[^ti-slva079] плюс `V_in*I_q`: за datasheet uA7805 `I_q` – кілька мА, тож це ще десятки мВт.[^ti-ua78] При 50 Ом струм, потужність резистора й складова `(V_in - V_out)*I_out` подвояться (0,1 А; 0,5 Вт; 0,4 Вт), а частина `V_in*I_q` лишається тією самою.

## Detailed explanation

7805 тримає на виході 5 В, якщо вхід вищий за вихід щонайменше на dropout (2 В за струму 1 А, типово) і лежить у рекомендованому діапазоні 7–25 В для uA7805; 9 В цій умові відповідає.[^ti-ua78] Тому на резисторі 100 Ом падає 5 В, і `I = V/R = 5/100 = 50 мА`. Datasheet задає вихід 4,8–5,2 В за 25 °C,[^ti-ua78] тож реальний струм лежить у межах 48–52 мА, і ще додається допуск самого резистора.

Потужність на резисторі `P_R = V²/R = 5²/100 = 0.25 Вт`. Резистор із номіналом рівно 0,25 Вт працював би на межі, тому беруть запас; поширена практика – подвійний, тобто 0,5 Вт, але це не правило, а ступінь запасу залежить від умов охолодження. У стабілізаторі різниця напруг `9 - 5 = 4 В` падає на тому самому струмі 50 мА: `P_reg = (V_in - V_out)*I_out = 4*0.05 = 0.2 Вт`.[^ti-slva079] Це не повна картина: власний струм спокою стабілізатора, за datasheet uA7805, – 4,2 мА типово й до 8 мА,[^ti-ua78] він іде з входу, і додає `9*0.0042 ≈ 0.038 Вт` (до `9*0.008 = 0.072 Вт`). Тож типово стабілізатор розсіює близько 0,24 Вт.

Перевіримо баланс. Вхідний струм `I_in = 50 + 4.2 = 54.2 мА`, вхідна потужність `9*0.0542 = 0.488 Вт`, з них резистору дістається 0,25 Вт, стабілізатору – `0.488 - 0.25 ≈ 0.238 Вт`. ККД `0.25/0.488 ≈ 51 %`, що за формулою `I_o*V_o/((I_o + I_q)*V_i)` збігається з розрахунком[^ti-slva079] і не перевищує `V_out/V_in = 5/9 ≈ 56 %`.

При 50 Ом струм зростає вдвічі: `I = 5/50 = 100 мА`, потужність на резисторі `P_R = 25/50 = 0.5 Вт`, у стабілізаторі `(9 - 5)*0.1 = 0.4 Вт` (без урахування `I_q`). Тобто резистор 0,5 Вт тепер працює на самій межі, і потрібен резистор більшої потужності, наприклад 1 Вт.

**Типові помилки:**

- Рахувати потужність резистора від 9 В замість 5 В: на ньому падає лише вихідна напруга стабілізатора.
- Рахувати потужність стабілізатора як `5*0.05`, тобто потужність навантаження, замість `(V_in - V_out)*I_out`.
- Забувати про `I_q`, який додає десятки мВт і зменшує ККД.
- Брати резистор рівно на 0,25 Вт без запасу.

## Sources

<!-- generated from frontmatter -->
