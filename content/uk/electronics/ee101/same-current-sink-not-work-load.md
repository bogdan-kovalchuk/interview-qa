---
id: emb-elee-0225
title: "Чому той самий `current sink` 10 мА від 9 В не працює з навантаженням 1 кОм?"
description: "Чому той самий `current sink` 10 мА від 9 В не працює з навантаженням 1 кОм?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-14
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
    applicability: "Походження питання: лекція 74, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-14; курс не є доказом цих тверджень."
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
  - source_id: fiore-ohms-law
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 3.5 Ohm's Law"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/03:_Series_Resistive_Circuits/3.05:_Ohm's_Law"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Підручник, розділ 3.5: закон Ома V = I×R; з відомої напруги на резисторі знаходять струм. Загальна форма, не конкретні схеми."
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Підручник, розділ 4.6: I_C(sat) = V_CC/R_C як максимум колекторного струму в насиченні; V_CE(sat) «десята частка вольта або близько того» для малосигнальних приладів; приклад дає 0,15 В при I_C = 10 mA, I_B = 0,3 mA. Розрахунок не враховує падіння на емітері."
---

## Short answer

**Запасу напруги немає:** 10 мА на 1 кОм потребують `V = I*R = 10 V`, а все живлення лише 9 V.[^fiore-ohms-law] Коли заданий струм недосяжний, транзистор насичується, і `current sink` дає не більше 9 мА – максимум, який задає коло.[^fiore-bjt-dc-load-line]

## Detailed explanation

Якщо навантаження 1 кОм і `current sink` з’єднані послідовно між шиною 9 V і землею, сума падінь напруги на них не може перевищувати 9 V. Для 10 мА на 1 кОм потрібно `0.010 A * 1000 Ω = 10 V` лише на навантаженні. Це більше за все живлення, тож такий режим недосяжний за будь-якого транзистора й будь-якого резистора емітера. Обмеження випливає із закону Ома `V = I*R`, застосованого до резистора в колі.[^fiore-ohms-law]

Граничний струм задає коло: `V_CC/R = 9 V / 1 kΩ = 9 mA`. Коли заданий струм вищий, транзистор насичується і дає не більше 9 mA.[^fiore-bjt-dc-load-line] Навіть якщо знехтувати падінням на резисторі емітера й узяти `V_CE(sat)` близько 0,1 В, навантаження отримає не більше `(9 - 0.1)/1000 = 8.9 mA`. Ідеальна межа без жодних втрат – 9 mA, і вона вже менша за 10 mA.

`Current sink` тримає заданий струм лише за наявності запасу напруги. Тому мінімальне живлення для 10 mA на 1 kΩ становить 10 V плюс падіння на самому стоці. При 9 V навантаження має бути не більше 900 Ω (`9 V / 10 mA`), а з урахуванням падінь на стоці – менше.

**Типові помилки:**

- Вважати, що `current sink` видає задані 10 mA незалежно від навантаження: струм обмежує живлення.
- Перевіряти лише номінал резистора емітера, а не запас напруги на навантаженні.
- Не враховувати `V_CE(sat)` і падіння на резисторі емітера, коли шукають граничне навантаження.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
