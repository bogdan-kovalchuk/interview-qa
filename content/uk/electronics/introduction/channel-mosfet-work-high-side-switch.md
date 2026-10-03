---
id: emb-elintro-0254
title: "Як працює P-channel MOSFET як high-side switch?"
description: "Як працює P-channel MOSFET як high-side switch?"
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
  - source_id: ti-pmos-high-side
    title: "Texas Instruments: P-channel controllers simplify high-side gate drive"
    url: https://www.ti.com/document-viewer/lit/html/SSZT975/GUID-2E43C966-E5BD-4918-9B79-18A6DD85D045
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює керування P-channel high-side MOSFET відносно VIN; не визначає межі конкретного транзистора."
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

Source P-channel MOSFET під’єднаний до `+V`, а drain – до навантаження. Для ввімкнення gate опускають нижче source, створюючи від’ємне `V_GS`; для вимкнення gate підтягують до source, щоб `V_GS` стало близьким до нуля. Максимальну напругу `V_GS` не можна перевищувати.[^ti-pmos-high-side]

## Detailed explanation

P-channel MOSFET як high-side switch розміщують між плюсовим живленням і навантаженням: source під’єднаний до `+V`, drain – до навантаження. Стан ключа визначає різниця потенціалів між gate і source. Якщо gate майже на рівні source, `V_GS ≈ 0` і транзистор вимкнений; якщо gate стає нижчим за source, від’ємний `V_GS` відкриває канал.[^ti-pmos-high-side]

Для простої схеми це зручно: резистор може підтягувати gate до source, утримуючи ключ вимкненим, а малий транзистор або контролерний драйвер стягує gate до нижчої напруги для ввімкнення. Оскільки source перебуває біля плюса живлення, рівень gate треба оцінювати відносно нього. Якщо керувальна схема працює від нижчої логічної напруги, пряме з’єднання GPIO може не забезпечити потрібний режим і навіть порушити межу `V_GS`; потрібен відповідний транзисторний інтерфейс або driver.[^ti-pmos-high-side]

Перевірте абсолютний максимум `V_GS` у datasheet. За великої напруги живлення повне стягування gate до землі може перевищити допустиму напругу gate-source, тому застосовують обмеження, наприклад відповідний стабілітрон та резистор у керуванні. Також перевіряють `R_DS(on)` за фактичного від’ємного `V_GS`, струм і розсіювану потужність.[^ti-pmos-high-side]

Типова помилка – вважати, що «gate низький» завжди означає «MOSFET увімкнений». Важливий не абсолютний рівень відносно землі, а gate-source різниця. Після вимкнення gate має повернутися до потенціалу source, а схема керування мусить обмежувати напругу між цими виводами за всіх режимів живлення.[^ti-pmos-high-side]

## Sources

<!-- generated from frontmatter -->
