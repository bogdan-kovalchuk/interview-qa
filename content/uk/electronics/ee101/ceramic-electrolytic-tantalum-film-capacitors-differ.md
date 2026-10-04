---
id: emb-elee-0023
title: "Чим відрізняються керамічні, електролітичні, танталові та плівкові конденсатори?"
description: "Чим відрізняються керамічні, електролітичні, танталові та плівкові конденсатори?"
track: electronics
section: ee101
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Походження питання: лекція 35, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-practical-capacitors
    title: "All About Circuits: Practical Considerations - Capacitors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/practical-considerations-capacitors/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Полярність, робоча напруга, витік та практичні відмінності поширених конструкцій; окремі характеристики залежать від серії компонента."
  - source_id: adi-capacitor-selection
    title: "Analog Devices: Capacitor Selection Guidelines for Analog Devices, Inc., LDOs"
    url: https://www.analog.com/en/resources/app-notes/an-1099.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "MLCC: розмір, ESR/ESL та залежність ємності від діелектрика, температури й DC bias; tantalum/aluminum properties discussed for LDO selection, not universal rankings."
---

## Short answer

Керамічні MLCC зазвичай компактні й мають низькі ESR/ESL, але ємність деяких dielectric класів помітно залежить від температури та DC bias. Алюмінієві electrolytic і більшість solid tantalum є полярними; tantalum часто дає високу ємність на об’єм, а film capacitors – неполярні. Вибір залежить від конкретного dielectric, серії, напруги, ESR, стабільності та режиму кола.[^aac-practical-capacitors] [^adi-capacitor-selection]

## Detailed explanation

Тип конденсатора визначають за dielectric та конструкцією електродів, і це впливає на полярність, доступну ємність, розмір, ESR, витік і зміну параметрів з умовами роботи. Жоден клас не є найкращим для всіх застосувань: порівнювати потрібно конкретні серії та їхні datasheet, а не лише назви технологій.[^aac-practical-capacitors] [^adi-capacitor-selection]

MLCC часто обирають для локального bypass, бо вони компактні й можуть мати низькі ESR та ESL. Однак dielectric клас має значення: Analog Devices застерігає, що ємність керамічних компонентів може змінюватися з температурою та DC bias. Тому номінал, надрукований на корпусі, не завжди дорівнює ефективній ємності в робочому колі. Для сигналових трактів також може бути важливий механічно зумовлений шум у деяких ceramic dielectric.[^adi-capacitor-selection]

Алюмінієві electrolytic capacitor дають велику ємність у відносно компактному корпусі, що зручно для згладжування та накопичення енергії. Вони зазвичай полярні, мають обмеження робочої напруги, витік і неідеальні паразитні параметри; переполюсування може пошкодити тонкий оксидний dielectric. Solid tantalum також зазвичай полярний і має високу ємність на об’єм, але потрібні належна полярність, запас за напругою та перевірка обмежень surge current конкретного компонента. Не можна робити висновок, що будь-який electrolytic має однаковий ESR: технологія та серія суттєво різняться.[^aac-practical-capacitors] [^adi-capacitor-selection]

Film capacitor зазвичай неполярний. Під час вибору перевіряють робочу напругу, температурний діапазон, допуск, допустимий ripple current і частотні параметри конкретної серії. Позначка «для аудіо» чи «для таймерів» сама по собі не замінює цих критеріїв.[^aac-practical-capacitors]

**Типова помилка:** вважати всі MLCC однаково стабільними або всі електролітичні однаково «поганими» на високих частотах. Поведінку визначають dielectric, конструкція, розмір корпусу й умови навантаження; треба дивитися характеристики конкретної серії та ефективне значення ємності в схемі.[^adi-capacitor-selection]

## Sources

<!-- generated from frontmatter -->
