---
id: emb-elintro-0293
title: "Чому у схемі з батареєю 9 V, резистором 220 Ω і LED струм не дорівнює точно `9/220`?"
description: "Чому у схемі з батареєю 9 V, резистором 220 Ω і LED струм не дорівнює точно 9/220?"
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
    applicability: "Походження питання: лекція 26, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: ti-led-resistor
    title: "Texas Instruments: AN-1293 Driving RGB LED Using LP3936"
    url: https://www.ti.com/jp/lit/pdf/snva071
    accessed: 2026-10-04
    kind: official
    version: "SNVA071A, revised April 2013"
    applicability: "Формула обмежувального резистора та мінливість прямої напруги; приклади стосуються драйвера LP3936."
---
## Short answer

LED має пряме падіння напруги `V_f`, тому на резисторі залишається приблизно `9 V - V_f`, а струм дорівнює цьому падінню, поділеному на 220 Ω.[^ti-led-resistor] За `V_f = 2 V` оцінка становить близько 31.8 mA, а не `9/220`.

## Detailed explanation

У послідовному колі батарея, резистор і LED мають однаковий струм, але напруга батареї розподіляється між компонентами. Коли LED увімкнений у прямому напрямку, на ньому є пряме падіння `V_f`; на резисторі залишається різниця між напругою живлення й напругою LED. Тому оцінка струму: `I = (V_supply - V_f)/R`.[^ti-led-resistor]

Припустімо, що батарея дорівнює 9 V, резистор – рівно 220 Ω, а `V_f` у робочій точці становить 2 V. На резисторі буде 7 V, а струм – приблизно 31.8 mA. Це оцінка, не гарантовано точне значення: напруга батареї змінюється під навантаженням, допуск резистора ненульовий, а `V_f` залежить від типу LED, струму й температури.[^ti-led-resistor]

Вольт-амперна характеристика діода нелінійна. Не можна вважати LED резистором із фіксованим опором; при зміні струму змінюється його падіння напруги. Резистор встановлює робочу точку й обмежує струм, а точний проєкт враховує крайні значення живлення, `V_f`, допуск резистора та допустимий струм LED.[^ti-led-resistor]

**Типова помилка:** ділити всі 9 V на 220 Ω, ніби вся напруга припадає на резистор. Це ігнорує LED. Також не слід вважати 2 V універсальним значенням: виробник задає `V_f` для конкретних умов.

У наведеній оцінці резистор розсіює приблизно `P = 7 V * 31.8 mA ≈ 0.223 W`, тож резистор 0.25 W має малий запас. Реальний вибір потужності залежить від допусків і температурних умов.[^ti-led-resistor]

## Sources

<!-- generated from frontmatter -->
