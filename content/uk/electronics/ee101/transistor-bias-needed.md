---
id: emb-elee-0198
title: "Що таке зміщення (bias) транзистора і навіщо воно потрібне?"
description: "Що таке зміщення (bias) транзистора і навіщо воно потрібне?"
track: electronics
section: ee101
level: junior
type: concept
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Походження питання: лекція 69, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; курс не є доказом цих тверджень."
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
  - source_id: fiore-bias-need
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.2 The Need For Biasing"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.2:_The_Need_For_Biasing"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 5.2: навіщо потрібне зміщення (V_BE близько 0,7 В; без постійного зміщення від’ємна півхвиля сигналу ігнорується, сигнали в кілька сотень мілівольт); нестабільна Q-точка погіршує підсилення, спотворення й вихідну потужність. Загальна картина."
  - source_id: fiore-bjt-ebers-moll
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.5 Ebers-Moll Model"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.5:_Ebers-Moll_Model"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 4.5: для NPN потрібно V_C > V_B > V_E; β змінюється між екземплярами, зі струмом і температурою. Загальна картина; числа прикладів стосуються лише їхніх кіл."
  - source_id: fiore-bjt-collector-curves
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.3 BJT Collector Curves"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.3:_BJT_Collector_Curves"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 4.3: три зони колекторних характеристик – насичення ліворуч, майже постійний струм посередині для лінійних підсилювачів і пробій праворуч. Загальна картина, не для конкретного транзистора."
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 4.6: навантажувальна пряма, Q-точка (I_CQ, V_CEQ) лежить на ній; кінці прямої – I_C(sat) і V_CE(cutoff); типове V_CE(sat) близько десятої вольта, у прикладі 0,15 В при I_C = 10 мА і I_B = 0,3 мА. Точні значення беруть із графіків транзистора."
---

## Short answer

Зміщення (bias) – це постійні напруги й струми, які задають робочу точку транзистора. Завдяки ним малий змінний сигнал коливається навколо цієї точки і не вимикає транзистор у кожному півперіоді, бо база–емітер відкривається лише при напрузі близько 0,7 В.[^fiore-bias-need]

## Detailed explanation

Робоча точка, або Q-точка, – це постійні струм і напруга транзистора без сигналу: `I_CQ` і `V_CEQ`. Усі можливі Q-точки лежать на навантажувальній прямій.[^fiore-bjt-dc-load-line] Для NPN зміщення має забезпечити прямо зміщене база–емітерне з’єднання і зворотно зміщений колекторно-базовий перехід, тобто `V_C` > `V_B` > `V_E`.[^fiore-bjt-ebers-moll] Саме ці постійні напруги й струми і є зміщенням.

Навіщо це потрібно. Транзистор практично не проводить, поки `V_BE` не досягне близько 0,7 В.[^fiore-bias-need] Приклад: синусоїда з амплітудою 0,2 В, подана на базу без зміщення, дає `V_BE` не більше 0,2 В, тобто менше за 0,7 В. Транзистор не відкривається в жодній півхвилі, тож підсилення немає. Підручник пише, що сигнали мікрофонів і датчиків часто мають кілька сотень мілівольт, і без постійного зміщення такий сигнал може бути повністю проігнорований.[^fiore-bias-need] Постійне зміщення вирішує це: змінний сигнал накладається на велику постійну напругу, і навіть його негативний пік лишається додатною напругою на базі.[^fiore-bias-need]

Q-точка має бути стабільною, бо `I_C` і `V_CE` залежать від β, а β змінюється з температурою, струмом і напругою `V_CE`.[^fiore-bjt-ebers-moll] Підручник пояснює, що нестабільна Q-точка робить підсилення нестабільним, підвищує спотворення й зменшує вихідну потужність.[^fiore-bias-need] Тому робочу точку вибирають у зоні постійного струму, де `I_C` майже не залежить від `V_CE` і де працюють лінійні підсилювачі.[^fiore-bjt-collector-curves] Її кінці – це `I_C(sat)` і `V_CE(cutoff)`; Q-точка лежить між ними, а не на одному з кінців, тож сигнал має запас в обидва боки.[^fiore-bjt-dc-load-line]

**Типові помилки:**

- Вважати, що Q-точка стабільна сама собою: β змінюється від екземпляра до екземпляра і з температурою.[^fiore-bjt-ebers-moll]
- Ставити робочу точку в зону насичення або пробою замість зони постійного струму, де працюють лінійні підсилювачі.[^fiore-bjt-collector-curves]
- Розраховувати зміщення за одним значенням β з каталогу без перевірки запасу сигналу.

## Sources

<!-- generated from frontmatter -->
