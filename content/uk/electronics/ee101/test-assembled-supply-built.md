---
id: emb-elee-0167
title: "Як перевіряти зібране джерело 5 В на 7805?"
description: "Як перевіряти зібране джерело 5 В на 7805?"
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
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
    accessed: 2026-10-06
    kind: official
    version: "SNOSBT0L, September 2016"
    applicability: "Таблиця LM340/LM7805 (V_O = 5 В, V_I = 10 В, T_J = 25 °C): вихідна напруга 4,8–5,2 В за 5 мА ≤ I_O ≤ 1 А; load regulation за 5 мА ≤ I_O ≤ 1,5 А типово 10 мВ, максимум 50 мВ; line regulation за 7,5 В ≤ V_IN ≤ 20 В і I_O ≤ 1 А максимум 50 мВ; вхід від 7,5 В для збереження line regulation; струм спокою до 8 мА; характеристики виміряно імпульсною технікою (t_w ≤ 10 мс, скважність ≤ 5 %), зміну виходу через нагрів слід враховувати окремо. Значення стосуються родини LM340/LM7805, не інших стабілізаторів."
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA079, October 1999"
    applicability: "Потужність, що розсіюється стабілізатором, P_D = (V_i - V_o)*I_o. Записка про LDO; її числа й приклади не стосуються 7805."
---

## Short answer

Спочатку вимірюють вихід без навантаження, потім із розрахованим резистором, що дає потрібний струм. `V_in` вимірюють безпосередньо між виводами INPUT і GND мікросхеми, щоб бачити реальний запас над dropout. Порівнюють зміну виходу при зміні навантаження і при помірній зміні входу в межах, для яких datasheet задає line і load regulation.[^ti-lm340] Індикаторному LED потрібен власний резистор, і його струм теж входить у навантаження.

## Detailed explanation

Перевірку роблять поетапно, щоб кожен крок відділяв одну причину несправності. Без навантаження вихід показує лише, що стабілізатор живий і підключений правильно. Datasheet LM340/LM7805 задає вихідну напругу 4,8–5,2 В за струму від 5 мА до 1 А (`T_J = 25 °C`),[^ti-lm340] тому показання без навантаження – орієнтир, а не перевірка точності. Далі підключають резистор, що дає потрібний струм: для 100 мА це `R = 5 В / 0,1 А = 50 Ом` з потужністю `5*0,1 = 0,5 Вт`, тож беруть резистор із запасом, скажімо на 1 Вт.

`V_in` міряють на виводах мікросхеми, а не на вторинній обмотці чи конденсаторі: падіння на дротах, роз’ємах і діодах може зменшити реальний вхід. Це важливо, бо datasheet вимагає вхід від 7,5 В, щоб зберегти line regulation (див. `qid:emb-elee-0165`).[^ti-lm340] Тоді ж оцінюють нагрів: стабілізатор розсіює `P_D = (V_in - V_out)*I_out`,[^ti-slva079] наприклад за входу 9 В і 100 мА це `(9 - 5)*0,1 = 0,4 Вт`, а струм спокою (до 8 мА за `T_J = 25 °C`)[^ti-lm340] додає ще до `9*0,008 = 0,072 Вт`.

Зміну виходу порівнюють із datasheet. Load regulation за зміни струму від 5 мА до 1,5 А типово 10 мВ, максимум 50 мВ; line regulation за входу 7,5–20 В і струму до 1 А – максимум 50 мВ.[^ti-lm340] Наприклад, якщо вихід змінився з 5,03 до 5,01 В (20 мВ) при переході від 5 мА до 100 мА, це в межах норми. Сотні мілівольт означають інше: вхід нижчий за 7,5 В, поганий контакт чи великий опір проводів. Datasheet вимірює імпульсами (`t_w ≤ 10 мс`), тому за тривалого струму додається дрейф від нагріву.[^ti-lm340]

LED на 5 В без резистора не вмикають: струм задає резистор `R = (5 - V_F)/I`. Для ілюстрації `V_F = 2 В` і 10 мА дають 300 Ом; із 330 Ом струм становить `3 В / 330 Ом ≈ 9,1 мА`, і ці мА входять у навантаження. Нарешті форму виходу під навантаженням дивляться осцилографом, а не лише мультиметром (див. `qid:emb-elee-0166`).

**Типові помилки:**

- Міряти `V_in` на джерелі, а не на мікросхемі, і не бачити просідання.
- Підключати LED без власного резистора або не враховувати його струм у навантаженні.
- Брати резистор навантаження на потужність, що дорівнює розрахованій: `0,5 Вт` на резисторі 0,5 Вт нагріється до межі.
- Порівнювати показання без навантаження з допуском datasheet: той задано для струмів від 5 мА.

## Sources

<!-- generated from frontmatter -->
