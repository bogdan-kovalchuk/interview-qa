---
id: emb-elintro-0253
title: "Як працює N-channel MOSFET як low-side switch?"
description: "Як працює N-channel MOSFET як low-side switch?"
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
  - source_id: ti-mosfet-selection
    title: "Texas Instruments: Avoid Common Mistakes When Selecting and Designing with Power MOSFETs"
    url: https://www.ti.com/lit/an/slpa021/slpa021.pdf
    accessed: 2026-10-04
    kind: official
    version: "SLPA021, November 2024"
    applicability: "Пояснює, чому VGS(th) не гарантує малого RDS(on), і наводить параметри для добору MOSFET; параметри конкретного компонента треба звіряти з його datasheet."
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 23, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
---

## Short answer

Навантаження під’єднане між живленням і drain, а source – до спільного `GND`. Коли керування створює достатнє додатне `V_GS`, N-channel MOSFET проводить струм від навантаження до землі; `V_GS(th)` позначає лише початок провідності, а не гарантує малий `R_DS(on)`.[^ti-mosfet-selection]

## Detailed explanation

У схемі low-side switch N-channel MOSFET стоїть між навантаженням і землею: навантаження з’єднане з плюсом живлення, drain – з його нижнім виводом, а source – зі спільним `GND`. Керувальний сигнал задає напругу саме між gate і source. Коли `V_GS` достатньо додатне, канал утворює провідний шлях від drain до source, струм проходить через навантаження, а напруга на ньому приблизно дорівнює напрузі живлення за малих втрат ключа.[^ti-mosfet-selection]

Коли gate повертається до потенціалу source, канал вимикається й струм навантаження припиняється, окрім можливих шляхів через інші елементи схеми. Для індуктивного навантаження струм не може миттєво зникнути, тому потрібен належний шлях рециркуляції або обмеження напруги. Спільна земля між контролером і силовим колом потрібна для визначеного керувального `V_GS`; інакше напруга pin відносно землі може не бути напругою gate-source.[^ti-mosfet-selection]

Важлива межа – `V_GS(th)` не є рекомендованою напругою керування. Цей параметр задають за дуже малого струму, коли MOSFET лише починає проводити. Щоб ключ працював із низькими втратами, знайдіть у datasheet значення `R_DS(on)` при `V_GS`, яке реально може видати контролер. Наприклад, не можна автоматично вважати, що MOSFET з `V_GS(th) = 2 V` повністю відкритий від GPIO 3.3 V: потрібна специфікація опору за відповідної напруги gate.[^ti-mosfet-selection]

Практично перевіряють розсіювану потужність `P = I²*R_DS(on)`, нагрівання, допустимі `V_DS` та `V_GS`, а також перехідні процеси навантаження. Типова помилка – під’єднати MOSFET як ключ, але оцінити його лише за порогом `V_GS(th)` або за максимальним струмом із заголовка datasheet. Номінали треба оцінювати за умовами вимірювання, корпусом і реальним охолодженням.[^ti-mosfet-selection]

## Sources

<!-- generated from frontmatter -->
