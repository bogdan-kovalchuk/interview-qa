---
id: emb-elintro-0134
title: "Чому напруговий рейтинг конденсатора треба брати із запасом?"
description: "Чому напруговий рейтинг конденсатора треба брати із запасом?"
track: electronics
section: introduction
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
    applicability: "Походження питання: лекція 13, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: analog-devices-an140-capacitor-selection
    title: "Analog Devices, AN-140: Basic Concepts of Linear Regulator and Switching Mode Power Supplies"
    url: https://www.analog.com/en/resources/app-notes/an-140.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Розділ Input and Output Capacitor Selection вимагає враховувати voltage derating та RMS ripple current для buck-конвертера; джерело не встановлює універсального коефіцієнта запасу для всіх типів конденсаторів."
---

## Short answer

Робоча напруга конденсатора має залишатися в межах його datasheet з урахуванням піків і пульсацій; потрібний запас залежить від технології, температури та режиму. Універсального правила `1.5×–2×` для всіх конденсаторів немає – застосовують derating, заданий виробником і схемою.[^analog-devices-an140-capacitor-selection]

## Detailed explanation

Рейтинг напруги в datasheet визначає межу прикладеної напруги за визначених умов. У реальній схемі напруга може містити не лише сталу складову, а й ripple та короткі перехідні піки; усі ці складові треба враховувати, щоб напруга на компоненті не перевищувала допустиму межу.[^analog-devices-an140-capacitor-selection]

Запас потрібен, бо робоча точка змінюється через допуски джерела, навантаження, температуру та перехідні режими. Проте його розмір не є сталою часткою для кожного конденсатора. Для switching supply виробник схеми може вимагати достатній voltage derating, а виробник конденсатора задає конкретні обмеження для серії та умов експлуатації.[^analog-devices-an140-capacitor-selection]

Перевіряють найгіршу напругу на виводах: максимальну постійну напругу разом із ripple та transient, а для змінної складової – її амплітуду й форму. Окремо для MLCC перевіряють effective capacitance під DC bias: запас за номінальною напругою може зменшити втрату ємності, але це залежить від діелектрика, корпусу й конкретної деталі.[^analog-devices-an140-capacitor-selection]

Приклад: якщо шина має номінал `12 V`, але на конденсаторі можливі піки `15 V`, вибір роблять за реальною максимальною напругою та рекомендаціями datasheet, а не лише за числом `12 V` на схемі. Також перевіряють ripple current і температуру, оскільки електрична напруга – не єдиний чинник довговічності.[^analog-devices-an140-capacitor-selection]

**Типова помилка:** механічно множити робочу напругу на однаковий коефіцієнт для керамічного, електролітичного та плівкового конденсаторів. Спершу визнач максимальні напругу й температуру в схемі, потім звір конкретний компонент із таблицями, графіками та вимогами виробника.[^analog-devices-an140-capacitor-selection]

## Sources

<!-- generated from frontmatter -->
