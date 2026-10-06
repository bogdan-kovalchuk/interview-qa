---
id: emb-elee-0137
title: "Чому дуже малий сигнал погано проходить через діодний міст?"
description: "Чому дуже малий сигнал погано проходить через діодний міст?"
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
    applicability: "Походження питання: лекція 57, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Конденсаторний фільтр і пульсації (розряд між піками, зростання пульсацій зі струмом навантаження, зарядні піки струму), мостовий випрямляч (у кожному півперіоді провідні два діоди, два падіння V_F), простий стабілітронний стабілізатор і втрата регуляції при надто великому струмі навантаження; книга не наводить формули ΔV = I/(f*C) і не задає V_F конкретного діода."
  - source_id: libretexts-fiore-diode-models
    title: "Fiore: Semiconductor Devices, 2.4 Diode Circuit Models (Engineering LibreTexts)"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.4:_Diode_Circuit_Models"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Моделі діода: «колінна» напруга 0,7 В для кремнію як поведінкове наближення, опір R_bulk, динамічний опір ≈ 26 мВ / I. Це спрощені моделі, а не точні значення для конкретного приладу."
---

## Short answer

У кожному півперіоді струм навантаження проходить через два діоди мосту послідовно, тож для його появи потрібна напруга приблизно `2*V_F`, для кремнію близько 1,4 В.[^fiore-rectification] Сигнал з амплітудою нижчою за цей поріг майже не проходить, а сигнал із трохи більшою амплітудою дає лише короткі низькі імпульси, зменшені на `2*V_F`.[^fiore-rectification]

## Detailed explanation

Міст пропускає струм у кожному півперіоді через два діоди, і навантаження бачить вхідну напругу мінус два прямі падіння.[^fiore-rectification] У простій моделі з «колінною» напругою кремнієвий діод починає помітно проводити приблизно від 0,6–0,7 В.[^fiore-rectification] Підручник застерігає, що це поведінкові моделі, а не літеральні джерела 0,7 В усередині діода.[^libretexts-fiore-diode-models] Для двох діодів послідовно поріг подвоюється: `2*V_F ≈ 1.4 V`. Тому «малим» для мосту є сигнал, амплітуда якого порівнянна з 1,4 В, а не з нулем.

Реальна характеристика діода плавна, тому нижче порогу струм не дорівнює точно нулю, а лише дуже малий. У підручнику динамічний опір переходу оцінено як `26 mV/I`.[^libretexts-fiore-diode-models] За цим наближенням при 10 мкА він становить близько `0.026/10^-5 = 2.6 kΩ`, а при 1 мА – близько `0.026/10^-3 = 26 Ω`. Отже, слабкий сигнал створює малий струм, діоди виглядають для нього як великий опір, і якщо він більший за опір навантаження, то більша частина напруги падає на діодах, а не на навантаженні.

**Приклад (модель з `V_F = 0.7 V`, синусоїда з амплітудою `A`).** Пік виходу `A - 1.4 V`, а діоди проводять тільки тоді, коли `|v_in| > 1.4 V`, тобто частку півперіоду `(180° - 2*asin(1.4/A))/180°`:

- `A = 1 V`: вихід нульовий, діоди не відкриваються;
- `A = 1.41 V` (це сигнал 1 В RMS): пік виходу `0.01 V`, практично нуль;
- `A = 2 V`: пік `0.6 V` (30 % від входу), провідність близько 91° із 180°, тобто ≈ 51 %;
- `A = 5 V`: пік `3.6 V` (72 %), провідність ≈ 82 %;
- `A = 20 V`: пік `18.6 V` (93 %), і поріг майже непомітний.

Звідси видно, що вплив падіння залежить від відношення амплітуди до `2*V_F`: за високих напруг це дрібна поправка, за низьких – головний ефект. Той самий розрахунок показує також спотворення форми: поки амплітуда лише трохи вища за поріг, вихід складається з вузьких імпульсів біля піків, а не з копії входу.

Тому діодний міст не годиться для випрямлення сигналів, амплітуда яких порівнянна з 1,4 В, наприклад слабких вимірювальних чи радіосигналів. Для них потрібні інші підходи, що компенсують падіння діода або використовують діоди з меншим `V_F`; ці схеми тут не розглядаються.

**Типові помилки:**

- Вважати, що діод пропускає будь-яку додатну напругу, і забувати про поріг близько 0,7 В на кожен діод.
- Брати для мосту одне падіння замість двох.
- Порівнювати поріг з діючим (RMS) значенням, а не з амплітудою: сигнал 1 В RMS має пік 1,41 В.

## Sources

<!-- generated from frontmatter -->
