---
id: emb-elee-0157
title: "З чого починати проєктування джерела живлення?"
description: "З чого починати проєктування джерела живлення?"
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
    applicability: "Ефективність і потужність розсіювання LDO, обмеження P_D(max) = (T_Jmax - T_A)/R_θJA через максимальну junction temperature, стабільний діапазон compensation series resistance вихідного конденсатора. Записка про LDO; імпульсних перетворювачів не стосується."
  - source_id: ti-tps752q1-datasheet
    title: "Texas Instruments TPS752-Q1 datasheet"
    url: https://www.ti.com/lit/ds/symlink/tps752-q1.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Datasheet конкретного LDO як приклад: recommended operating conditions (V_I 2.7–5.5 V, I_O до 2 A), примітка V_I(min) = V_O(max) + V_DO(max load), absolute maximum ratings і таблиця допустимої потужності, що різниться для різних плат і обдуву. Значення стосуються лише TPS752-Q1."
---

## Short answer

Починають із вимог: вихідна напруга, робочий і піковий струм, діапазон вхідної напруги, допустимі пульсації. З них оцінюють розсіювання `P = (V_in - V_out)*I_out` і вирішують, чи вистачить лінійного регулятора. Потім за datasheet обраної мікросхеми перевіряють recommended operating conditions, dropout, вимоги до вихідного конденсатора й тепловий режим.[^ti-slva079][^ti-tps752q1-datasheet]

## Detailed explanation

Проєктування джерела живлення починають із чисел, бо від них залежать усі наступні вибори. Потрібні вихідна напруга і допуск на неї, робочий та піковий струм навантаження, діапазон вхідної напруги з обома краями та допустимі пульсації. Мінімальна вхідна напруга разом із дном пульсацій визначає, чи виконується умова dropout (див. `qid:emb-elee-0156`), а максимальна – скільки тепла виділиться й чи не наближається вхід до граничних значень (див. `qid:emb-elee-0158`).

Другий крок – оцінити втрати. Для лінійного регулятора вони дорівнюють `P = (V_in - V_out)*I_out`, а ефективність обмежена відношенням `V_out/V_in`.[^ti-slva079] Рахувати слід за найгіршого поєднання: найбільша вхідна напруга й найбільший струм. Якщо тепла забагато, розглядають інший підхід, наприклад імпульсний перетворювач або попередній понижувальний каскад, і тільки після цього обирають конкретну мікросхему.

Третій крок – звірити вимоги з datasheet. Спершу recommended operating conditions: у TPS752-Q1, наприклад, `V_I` має лежати в межах 2.7–5.5 V, а струм – не перевищувати 2 A, тоді як absolute maximum для входу становить 6 V.[^ti-tps752q1-datasheet] Це різні таблиці з різним призначенням: розрахунок ведуть за рекомендованими умовами. Потім dropout для максимального струму: мінімальна вхідна напруга там задана як `V_I(min) = V_O(max) + V_DO(max load)`.[^ti-tps752q1-datasheet] Потім вихідний конденсатор: виробники LDO зазвичай наводять діапазон допустимого compensation series resistance, поза яким регулятор може бути нестабільним, тож тип конденсатора й його ESR підбирають за datasheet.[^ti-slva079] Розміщення конденсаторів і розведення плати теж виконують за рекомендаціями datasheet.

Останній крок – тепловий режим. Фактична потужність розсіювання має бути не більшою за `P_D(max) = (T_Jmax - T_A)/R_θJA`.[^ti-slva079] Допустима потужність залежить від плати й обдуву: datasheet TPS752-Q1 для корпусу PWP наводить різні значення для різних плат і за різного потоку повітря.[^ti-tps752q1-datasheet]

**Приклад (ілюстративний, за даними TPS752-Q1):** вимоги `V_in = 4.5–5.5 V`, `V_out = 3.3 V`, `I_out(max) = 1 A`. Найгірші втрати `(5.5 - 3.3)*1 = 2.2 W`. За datasheet для корпусу PWP на однощаровій платі 5 in x 5 in без обдуву допустима потужність `2.9 W` при `T_A <= 25 °C` і `1.9 W` при `T_A = 70 °C`.[^ti-tps752q1-datasheet] Отже, `2.2 W` проходить за 25 °C, але не проходить за 70 °C: у цьому випадку саме тепло, а не напруга чи струм, вирішує, чи потрібні радіатор, краща плата, обдув або інша топологія.

**Типові помилки:**

- Обирати мікросхему до того, як визначено діапазон входу, піковий струм і пульсації.
- Перевіряти лише середню чи типову вхідну напругу, не розглядаючи її мінімум і максимум.
- Орієнтуватися на absolute maximum ratings замість recommended operating conditions.
- Не рахувати розсіювання для найгіршого режиму й не перевіряти його за температурою навколишнього середовища.

## Sources

<!-- generated from frontmatter -->
