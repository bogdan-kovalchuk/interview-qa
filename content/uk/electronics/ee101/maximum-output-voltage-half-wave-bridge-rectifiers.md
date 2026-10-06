---
id: emb-elee-0136
title: "Який максимум вихідної напруги дадуть однопівперіодний і мостовий випрямлячі від синуса 5 В peak?"
description: "Який максимум вихідної напруги дадуть однопівперіодний і мостовий випрямлячі від синуса 5 В peak?"
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
  - source_id: vishay-1n4001
    title: "Vishay: 1N4001 to 1N4007 general purpose plastic rectifier datasheet"
    url: https://www.vishay.com/docs/88503/1n4001.pdf
    accessed: 2026-10-06
    kind: official
    version: "Revision 29-Apr-2020"
    applicability: "Максимальне V_F 1,1 В за 1 А (25 °C); I_R до 5 мкА за 25 °C і до 50 мкА за 125 °C за номінальної зворотної напруги; V_RRM від 50 до 1000 В залежно від типу. Стосується цієї серії випрямних діодів."
---

## Short answer

Для кремнієвих діодів з `V_F ≈ 0.7 V`: однопівперіодний випрямляч дає пік `5 - 0.7 = 4.3 V`, бо в колі один діод.[^fiore-rectification] Міст дає `5 - 2*0.7 = 3.6 V`: у кожному півперіоді струм іде через два діоди послідовно.[^fiore-rectification] Поки вхідна напруга нижча за падіння на діодах, вони майже не проводять, тому біля нуля синусоїди вихід близький до нуля.[^fiore-rectification]

## Detailed explanation

Максимум вихідної напруги (пік) – це пік входу мінус падіння на діодах у колі струму. В однопівперіодній схемі діод стоїть послідовно з навантаженням: у додатний півперіод він відкритий і вихід дорівнює вхідній напрузі мінус `V_F`, у від’ємний – закритий, і вихід нульовий.[^fiore-rectification] Для синуса з піком 5 В і `V_F = 0.7 V` маємо `5 - 0.7 = 4.3 V`. Підручник наголошує, що при малій амплітуді (3–4 В) падіння 0,7 В – помітна частка входу й ним не можна нехтувати.[^fiore-rectification]

У мостовому випрямлячі використовуються обидва півперіоди, але струм навантаження проходить послідовно через два діоди відкритої діагональної пари, і навантаження бачить усю напругу вхідного джерела мінус два прямі падіння.[^fiore-rectification] Тому пік дорівнює `5 - 2*0.7 = 3.6 V`. Міст виграє у ефективності (використовується весь сигнал), але програє в піку вихідної напруги.

**Чому біля нуля вихід малий.** Модель діода з «колінною» напругою 0,7 В – це поведінкове наближення, а не буквальне джерело 0,7 В.[^libretexts-fiore-diode-models] Діод проводить помітний струм лише тоді, коли вхідна напруга сягає приблизно 0,6–0,7 В.[^fiore-rectification] За цією моделлю в однопівперіодній схемі вихід нульовий, доки `v_in < 0.7 V`, тобто на ділянці `asin(0.7/5) ≈ 8°` біля кожного нуля. У мосту поріг удвічі вищий: `v_in < 1.4 V`, `asin(1.4/5) ≈ 16°` з кожного боку нуля, і разом близько 32° із кожних 180° півперіоду, тобто біля 18 %.

**Межі.** Це розрахунок для моделі зі сталим `V_F`. Реальне `V_F` залежить від струму: для діодів серії 1N4001 максимум становить 1,1 В за 1 А.[^vishay-1n4001] Якби обидва діоди мосту мали по 1,1 В, пік за 5 В був би лише `5 - 2.2 = 2.8 V`, а в однопівперіодній схемі `5 - 1.1 = 3.9 V`. Окрім цього, 5 В peak – це не 5 В RMS: діюче значення синуса з піком 5 В дорівнює `5/sqrt(2) ≈ 3.54 V`, і падіння віднімають саме від піка. Фільтрувального конденсатора в цьому розрахунку немає: з ним форма вихідної напруги інша.

**Типові помилки:**

- Відняти лише одне падіння для мосту або два для однопівперіодної схеми.
- Віднімати падіння від діючого (RMS) значення замість піка.
- Вважати 0,7 В точним значенням для будь-якого діода й струму.

## Sources

<!-- generated from frontmatter -->
