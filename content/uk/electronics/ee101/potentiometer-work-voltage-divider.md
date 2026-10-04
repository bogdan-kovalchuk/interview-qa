---
id: emb-elee-0012
title: "Як потенціометр працює як дільник напруги?"
description: "Як потенціометр працює як дільник напруги?"
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
    applicability: "Походження питання: лекція 34, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: bourns-potentiometer
    title: "Bourns: 3386 Trimpot Trimming Potentiometer Datasheet"
    url: https://bourns.com/docs/Product-Datasheets/3386.pdf
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Підтверджує конфігурацію voltage divider; числові межі стосуються лише серії 3386."
---

## Short answer

Крайні виводи потенціометра підключають до `V_in` і GND, а вихід знімають із wiper. Для ненавантаженого ідеального дільника `V_out = V_in*R_2/(R_1+R_2)`, де `R_1+R_2 = R_total`; отже, вихід змінюється між напругами на крайніх виводах. Навантаження виходу змінює поділ напруги, тому формула без навантаження не завжди описує реальне коло.[^bourns-potentiometer]

## Detailed explanation

Потенціометр працює як voltage divider, коли напруга подана між його крайніми виводами, а вихід знімається з рухомого контакту. Wiper ділить резистивну доріжку на дві частини: `R_1` від верхнього кінця до контакту та `R_2` від контакту до землі. За відсутності навантаження через обидві частини проходить той самий струм, тому вихідна напруга визначається часткою опору нижньої секції від загального опору.[^bourns-potentiometer]

Якщо напруга на крайніх виводах дорівнює `V_in` і `0 V`, для ідеального потенціометра маємо `V_out = V_in*R_2/(R_1+R_2)`. При переміщенні wiper `R_1` зростає, а `R_2` зменшується або навпаки – залежно від того, який кінець обрано опорним. На крайніх положеннях вихід наближається до напруги відповідного кінцевого виводу, але контактний і залишковий опори можуть не дати точного нуля чи повного рівня.[^bourns-potentiometer]

Приклад розрахунку:

```text
V_in = 5 V
R_1 = 6 kΩ, R_2 = 4 kΩ
V_out = 5 V*4/(6+4) = 2 V
```

Цей розрахунок припускає, що вихід не навантажений. Якщо до wiper під’єднати вхід із кінцевим опором, цей опір стає паралельним `R_2`, зменшує ефективний нижній опір і зазвичай знижує `V_out`. Щоб вплив був малим, вхідний опір наступного каскаду має бути значно більшим за опір секції дільника; за потреби ставлять buffer.[^bourns-potentiometer]

**Типова помилка:** вважати потенціометр регулятором, який завжди видає задану частку `V_in`. Частка залежить від положення wiper, закону доріжки та навантаження; ще слід перевірити допустиму напругу, розсіювану потужність і струм контакту конкретної моделі.[^bourns-potentiometer]

## Sources

<!-- generated from frontmatter -->
