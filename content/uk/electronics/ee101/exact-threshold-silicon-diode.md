---
id: emb-elee-0127
title: "Чи є 0,7 В точним порогом кремнієвого діода?"
description: "Чи є 0,7 В точним порогом кремнієвого діода?"
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
    applicability: "Походження питання: лекція 55, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: vishay-1n4148
    title: "Vishay: 1N4148 small signal fast switching diode datasheet"
    url: https://www.vishay.com/docs/81857/1n4148.pdf
    accessed: 2026-10-06
    kind: official
    version: "Rev. 1.6, 07-Nov-2024"
    applicability: "V_F не більше 1 В за I_F = 10 мА (25 °C); графіки V_F від струму (Fig. 2) і температури переходу (Fig. 1); струм витоку I_R до 25 нА за V_R = 20 В (25 °C) і до 50 мкА за 150 °C; V(BR) не менше 100 В. Значення стосуються цього малосигнального діода, а не всіх кремнієвих діодів; числа з графіків орієнтовні."
  - source_id: vishay-1n4001
    title: "Vishay: 1N4001 to 1N4007 general purpose plastic rectifier datasheet"
    url: https://www.vishay.com/docs/88503/1n4001.pdf
    accessed: 2026-10-06
    kind: official
    version: "Revision 29-Apr-2020"
    applicability: "Максимальне V_F 1,1 В за 1 А (25 °C); I_R до 5 мкА за 25 °C і до 50 мкА за 125 °C за номінальної зворотної напруги; V_RRM від 50 до 1000 В залежно від типу. Стосується цієї серії випрямних діодів."
  - source_id: libretexts-fiore-diode-models
    title: "Fiore: Semiconductor Devices, 2.4 Diode Circuit Models (Engineering LibreTexts)"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.4:_Diode_Circuit_Models"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Моделі діода: «колінна» напруга 0,7 В для кремнію як поведінкове наближення, опір R_bulk, динамічний опір ≈ 26 мВ / I. Це спрощені моделі, а не точні значення для конкретного приладу."
---

## Short answer

Ні. Пряме падіння `V_F` залежить від струму, температури і типу приладу; 0,7 В – зручне наближення.[^libretexts-fiore-diode-models] Наприклад, за datasheet 1N4148 `V_F` сягає 1 В за 10 мА, а випрямного 1N4001 – 1,1 В за 1 А.[^vishay-1n4148][^vishay-1n4001] У зворотному напрямку залишаються струм витоку й обмеження за допустимою напругою.

## Detailed explanation

Значення 0,7 В належить не діоду, а моделі. У «другому наближенні» діод – це перемикач із «колінною» напругою `V_knee`, яка для кремнію приймається рівною 0,7 В; підручник прямо наголошує, що це поведінкові моделі, а не буквальні джерела 0,7 В усередині діода.[^libretexts-fiore-diode-models] Реальна ж вольт-амперна характеристика описується експоненційним рівнянням Шоклі, тому `V_F` закономірно, хоч і порівняно повільно, зростає зі струмом і ніяк не є сталою.[^libretexts-fiore-diode-models]

**Залежність від струму.** Datasheet 1N4148 гарантує лише верхню межу: `V_F ≤ 1 В` за `I_F = 10 мА` при 25 °C.[^vishay-1n4148] На графіку Fig. 1 того ж документа за 25 °C напруга `V_F` – приблизно від 0,5 В за 0,1 мА до 0,85 В за 100 мА (числа зчитано з графіка, тож вони орієнтовні). Випрямний діод 1N4001 за 1 А може мати до 1,1 В.[^vishay-1n4001] Навіть проста модель із опором `R_bulk` дає напругу, що росте зі струмом: у прикладі підручника з `R_bulk = 10 Ω` за ≈ 5,6 мА діод має ≈ 0,756 В, а не 0,7 В.[^libretexts-fiore-diode-models]

**Залежність від температури.** За тим самим Fig. 1 при фіксованому струмі `V_F` знижується зі зростанням температури переходу: для `I_F = 10 мА` приблизно від 0,83 В при -40 °C до 0,54 В при 150 °C, тобто близько -1,5 мВ/°C (орієнтовно, за графіком).[^vishay-1n4148] Тому діод у гарячому корпусі має інше падіння, ніж на столі за кімнатної температури.

**Зворотний напрямок.** Модель «розімкнений перемикач» теж наближена. У 1N4148 струм витоку не більше 25 нА за `V_R = 20 В` при 25 °C, але до 50 мкА за тієї ж напруги при 150 °C – у 2000 разів більше; 1N4001 має до 5 мкА за 25 °C і до 50 мкА за 125 °C при номінальній зворотній напрузі.[^vishay-1n4148][^vishay-1n4001] А допустима зворотна напруга залежить від типу: `V_RRM` у серії 1N4001–1N4007 – від 50 до 1000 В, а `V(BR)` 1N4148 – не менше 100 В.

**Приклад впливу.** Для джерела 3,3 В і резистора 1 кОм `I = (3.3 - 0.7)/1000 = 2.6 мА`. Якщо реальне `V_F = 0.55 В`, то `I = 2.75 мА`; якщо `0.85 В`, то `I = 2.45 мА`. Розкид приблизно ±6 % від самого лише `V_F`, і чим нижча напруга джерела, тим помітніший вплив.

**Типові помилки:**

- Вважати 0,7 В гарантованою властивістю кремнієвого діода й закладати її в розрахунок без запасу.
- Не враховувати, що `V_F` залежить від струму й температури, особливо в низьковольтних колах і силових випрямлячах.
- Ігнорувати зворотний струм витоку й `V_RRM` / `V(BR)`, особливо при високій температурі.

## Sources

<!-- generated from frontmatter -->
