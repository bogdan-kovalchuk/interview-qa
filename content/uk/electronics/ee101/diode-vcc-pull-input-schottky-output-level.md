---
id: emb-elee-0148
title: "Діодний AND: `V_CC` = 5 В, підтягування 10 кОм, вхід 0 В, `V_F` ≈ 0,3 В (Шотткі). Які рівень виходу і струм?"
description: "Діодний AND: V_CC = 5 В, підтягування 10 кОм, вхід 0 В, V_F ≈ 0,3 В (Шотткі). Які рівень виходу і струм?"
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
    applicability: "Походження питання: лекція 59, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: utah-cs6710-diode-logic
    title: "Logic Gates from Resistors, Diodes, and Transistors (B.2), handout CS 6710, University of Utah"
    url: https://my.eng.utah.edu/~cs6710/handouts/AppendixB/appendixB.doc2.html
    accessed: 2026-10-06
    kind: book
    version: "last updated 1996-07-16"
    applicability: "Лекційний матеріал курсу 1996 року зі спрощеною моделлю діода; додаткове джерело: діодні AND і OR з резистором, падіння на діоді «приблизно 0,7 В», накопичення падінь при каскадуванні (п’ять AND по 0,7 В дають 3,5 В), неможливість інвертора лише з діодів і резисторів. Не містить параметрів конкретних приладів."
  - source_id: nexperia-diode-handbook
    title: "Nexperia: Diode Application Handbook (Design Engineer’s Guide), 2022"
    url: https://assets.nexperia.com/documents/brochure/Nexperia_document_book_DiodeApplicationHandbook_2022.pdf
    accessed: 2026-10-06
    kind: official
    version: "2022"
    applicability: "Розділ 7.4 (Switching diode): прості повільні діодні функції OR і AND з резистором (рис. 114–117): діоди розв’язують входи, за низького входу на резисторі лежить V_F, за всіх високих входів вихід високий; розділ 2: діод Шотткі має низьке пряме падіння, але є компроміс між V_F, струмом витоку й зворотною напругою. Загальні відомості, а не параметри конкретного діода."
  - source_id: libretexts-fiore-diode-models
    title: "Fiore: Semiconductor Devices, 2.4 Diode Circuit Models (Engineering LibreTexts)"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.4:_Diode_Circuit_Models"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Моделі діода: «колінна» напруга 0,7 В для кремнію як поведінкове наближення, опір R_bulk, динамічний опір ≈ 26 мВ / I. Це спрощені моделі, а не точні значення для конкретного приладу."
  - source_id: vishay-bat54
    title: "Vishay: BAT54, BAT54A, BAT54C, BAT54S small signal Schottky diodes (datasheet)"
    url: https://www.vishay.com/docs/86410/bat54_bat54a_bat54c_bat54s.pdf
    accessed: 2026-10-06
    kind: official
    version: "Rev. 1.1, 21-Feb-2024"
    applicability: "Максимальне V_F за 25 °C: 240 мВ за 0,1 мА, 320 мВ за 1 мА, 400 мВ за 10 мА, 800 мВ за 100 мА; струм витоку до 2 мкА за V_R = 25 В; V_BR не менше 30 В. Значення стосуються цієї серії малосигнальних діодів Шотткі, а не всіх діодів Шотткі."
  - source_id: ti-hc00
    title: "TI: SN74HC00, SN54HC00 quadruple 2-input NAND gates (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
    accessed: 2026-10-06
    kind: official
    version: "SCLS181H"
    applicability: "Розділ 6.3 Recommended Operating Conditions: V_IL(max) = 1,35 В і V_IH(min) = 3,15 В за V_CC = 4,5 В; рядка для V_CC = 5 В у таблиці немає. Значення стосуються цієї родини HC, інші родини логіки мають інші пороги."
---

## Short answer

Вихід ≈ `V_in + V_F = 0 + 0.3 = 0.3 V`, а струм `I = (5 - 0.3)/10000 ≈ 0.47 mA` (без навантаження на виході). Цей струм тече від живлення через резистор і діод у вхід, тому його має поглинути драйвер входу, що утримує логічний нуль.[^nexperia-diode-handbook][^utah-cs6710-diode-logic]

## Detailed explanation

Коли вхід діодного AND заземлено, діод між виходом і входом відкривається, і вихідний вузол сідає на рівень входу плюс пряме падіння діода: `V_out = V_in + V_F`.[^nexperia-diode-handbook][^utah-cs6710-diode-logic] Для `V_in = 0 V` і `V_F ≈ 0.3 V` це дає `0.3 V`. Усю решту напруги живлення бере на себе підтягувальний резистор, тож струм визначає закон Ома: `I = (V_CC - V_out)/R = (5 - 0.3)/10000 = 0.47 mA`. На резисторі при цьому розсіюється `P = 0.47 mA * 4.7 V ≈ 2.2 mW`.

Значення `V_F ≈ 0.3 V` для діода Шотткі правдоподібне, але воно залежить від струму й типу діода. Наприклад, для BAT54 максимальне `V_F` – 0,24 В за 0,1 мА і 0,32 В за 1 мА, тож за 0,47 мА воно не перевищує 0,32 В.[^vishay-bat54] Для кремнієвого діода в простій моделі падіння 0,7 В:[^libretexts-fiore-diode-models] тоді вихід був би `0.7 V`, а струм `(5 - 0.7)/10000 = 0.43 mA`. Різниця в струмі невелика, а рівень виходу відрізняється більш ніж удвічі, і саме це виграє Шотткі.

Є ще три застереження. По-перше, `0 V` на вході – ідеалізація: якщо драйвер входу утримує нуль із власним `V_OL`, то вихід дорівнює `V_OL + V_F`, а не просто `V_F`. По-друге, струм `0.47 mA` тече в драйвер входу, і той має його поглинути. По-третє, важливо, чи є отриманий рівень коректним логічним нулем для наступного каскаду. Для SN74HC00 за `V_CC = 4.5 V` вхідний низький рівень не вище `1.35 V`, тому `0.3 V` і навіть `0.7 V` проходять, але таблиця не охоплює 5 В і не застосовується до інших родин.[^ti-hc00]

**Типові помилки:**

- Вважати вихід нулем: він вищий за низький вхід на `V_F`.
- Забути, що струм підтягування тече у вхід, а не «в нікуди».
- Підставити для діода Шотткі 0,7 В, а для кремнієвого – 0,3 В.
- Не врахувати навантаження на виході: воно змінює струм і рівень.

## Sources

<!-- generated from frontmatter -->
