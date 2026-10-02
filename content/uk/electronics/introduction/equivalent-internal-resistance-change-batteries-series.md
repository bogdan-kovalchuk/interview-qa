---
id: emb-elintro-0070
title: "Як змінюється еквівалентний внутрішній опір батарей при послідовному з'єднанні?"
description: "Як змінюється еквівалентний внутрішній опір батарей при послідовному з'єднанні?"
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
    applicability: "Походження питання: лекція 8, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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

За послідовного з’єднання еквівалентний внутрішній опір дорівнює сумі опорів окремих батарей, якщо їх моделювати як ідеальні джерела ЕРС із послідовним опором.[^aac-direct-current] Сумарна ЕРС також додається для батарей, з’єднаних в одному напрямку.[^aac-direct-current]

## Detailed explanation

У простій моделі кожну батарею подають як ідеальне джерело електрорушійної сили послідовно з внутрішнім опором. При послідовному з’єднанні один і той самий струм проходить через кожне джерело та його опір, тому опори додаються так само, як звичайні резистори в одному послідовному колі: `R_int,total = R_int1 + R_int2 + ...`.[^aac-direct-current]

Якщо з’єднати дві однакові батареї з ЕРС `1.5 V` і внутрішнім опором `0.2 Ω` кожна, сумарна ЕРС становитиме `3.0 V`, а сумарний внутрішній опір – `0.4 Ω`. Для навантаження `10 Ω` ідеалізований струм дорівнює `3.0 V/(10 Ω + 0.4 Ω) ≈ 0.288 A`. Частина напруги втрачається всередині джерел, тому клемна напруга під навантаженням менша за сумарну ЕРС.[^aac-direct-current]

Цей результат стосується послідовного з’єднання без паралельних шляхів і моделі з постійними параметрами. Реальний внутрішній опір залежить від хімії, температури, стану заряду та режиму вимірювання; батареї, з’єднані послідовно, не стають автоматично однаковими. Для різних елементів треба скласти їхні фактичні ефективні опори, а не множити один номінал на кількість.[^aac-direct-current]

**Типова помилка:** додавати лише напруги й забувати про сумарний опір, а тоді завищувати очікуваний струм. У моделі джерела напруга на навантаженні визначається разом із падінням на внутрішньому опорі.[^aac-direct-current]

## Sources

<!-- generated from frontmatter -->
