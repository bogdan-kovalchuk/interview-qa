---
id: emb-elee-0227
title: "Як правильно вимірювати струм амперметром і чому небезпечне інше підключення?"
description: "Як правильно вимірювати струм амперметром і чому небезпечне інше підключення?"
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
  - source_id: kuphaldt-ammeter-usage
    title: "Workforce LibreTexts: Electric Circuits VI – Experiments (Kuphaldt), 2.4 How to Use an Ammeter to Measure Current"
    url: "https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_VI_-_Experiments_(Kuphaldt)/02%3A_Basic_Concepts_and_Test_Equipment/2.04%3A_How_to_Use_an_Ammeter_to_Measure_Current"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Підручник (Kuphaldt), розділ 2.4: амперметр вмикають послідовно й ідеально не створює падіння напруги; паралельно до значного джерела напруги він діє як коротке замикання, сплеск струму може пошкодити прилад і спрацювати його внутрішній запобіжник; для ручних приладів радять починати з найвищого діапазону. Конкретні моделі не розглядаються."
  - source_id: fiore-source-conversions
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 6.2 Source Conversions"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/06:_Analysis_Theorems_and_Techniques/6.2:_Source_Conversions"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Підручник, розділ 6.2: реальне джерело напруги має послідовний внутрішній опір; при короткому замиканні виходів максимальний струм дорівнює E/R. Про амперметри в цьому розділі не йдеться."
  - source_id: fiore-ohms-law
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 3.5 Ohm's Law"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/03:_Series_Resistive_Circuits/3.05:_Ohm's_Law"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Підручник, розділ 3.5: закон Ома V = I×R; з відомої напруги на резисторі знаходять струм. Загальна форма, не конкретні схеми."
---

## Short answer

Амперметр вмикають послідовно з елементом, струм якого вимірюють: він майже не має опору й майже не змінює струм.[^kuphaldt-ammeter-usage] Паралельне підключення до джерела напруги дає майже коротке замикання: струм обмежує лише опір цього короткозамкненого шляху, `E/R`, де `R` – внутрішній опір джерела плюс опір приладу; внутрішній запобіжник приладу перегорає.[^kuphaldt-ammeter-usage][^fiore-source-conversions] Струм можна також знайти за падінням напруги на відомому резисторі, `I = V/R`.[^fiore-ohms-law]

## Detailed explanation

Амперметр вимірює струм, пропускаючи його крізь себе, тому його включають у розрив провідника: послідовно з навантаженням або резистором, через який тече струм.[^kuphaldt-ammeter-usage] Ідеальний амперметр не створює падіння напруги, тож майже не змінює струм у колі. Вимірювання виконують, розірвавши ланцюг у потрібному місці й вставивши прилад у цей розрив.

Для ілюстрації нехай джерело 9 V ідеальне, тобто має нульовий внутрішній опір, навантаження 1 kΩ, а опір амперметра на діапазоні струму 0.1 Ω (умовне значення, не паспортне). У послідовному ланцюзі `I = 9/(1000 + 0.1) ≈ 9.0 mA`, тобто прилад майже не змінює струм. Якщо ж поставити амперметр паралельно джерелу, шлях із джерела йде лише через прилад, і `I = E/R = 9/0.1 = 90 A`, тобто приблизно в 10 000 разів більше. Тут струм задає опір приладу, бо внутрішній опір джерела дорівнює нулю; у загальному випадку струм обмежує лише опір короткозамкненого шляху.[^fiore-source-conversions]

Чому це небезпечно: 90 A значно перевищують струм, на який прилад розрахований для вимірювання, тож сплеск може його пошкодити. Внутрішній запобіжник перегорає, і прилад не вимірює струм, доки запобіжник не замінять.[^kuphaldt-ammeter-usage] Для ручних приладів радять починати з найвищого діапазону струму й переходити до нижчих, поки показник не стане найсильнішим без перевантаження.[^kuphaldt-ammeter-usage]

**Типові помилки:**

- Вмикати амперметр паралельно джерелу або елементу, як вольтметр.
- Торкатися провідників щупами, а не розривати ланцюг і не вставляти прилад у розрив.
- Вибирати надто малий діапазон струму замість того, щоб почати з найвищого.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
