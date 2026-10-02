---
id: emb-elintro-0072
title: "Чому паралельно можна з'єднувати лише батареї з близькою напругою?"
description: "Чому паралельно можна з'єднувати лише батареї з близькою напругою?"
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
  - source_id: discover-helios-parallel
    title: "Discover Battery Helios Installation and Operation Manual"
    url: https://assets.discoverbattery.com/documents/helios/opm-helios-manual.pdf
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Вимагає для батарей Helios однакової моделі та різниці напруг не більш як 50 mV за рівня заряду від 95%; це конкретна вимога цієї лінійки, не універсальний поріг для всіх батарей."
---

## Short answer

Якщо напруги різні, між батареями потече вирівнювальний струм, обмежений переважно їхнім внутрішнім опором. Навіть невелика різниця може спричинити великий струм, а допустиме значення залежить від конкретної батареї та вказівок виробника.[^discover-helios-parallel]

## Detailed explanation

Паралельне з’єднання примусово задає однакову клемну напругу на всіх батареях. Якщо їхні напруги холостого ходу різняться, батарея з вищою напругою віддає струм у батарею з нижчою, доки різниця не зменшиться. У простій моделі з послідовним внутрішнім опором струм приблизно дорівнює різниці напруг, поділеній на суму внутрішніх опорів батарей та опору з’єднань.[^aac-direct-current]

Тому вимога «близькі напруги» є запобіжним правилом, а не універсальним числовим порогом. Допустима різниця залежить від хімії, конструкції, стану заряду, захисту та інструкцій виробника. Для літієвих батарей із BMS також треба враховувати, чи виробник дозволяє паралельну роботу саме цих моделей; не можна виводити сумісність лише з однакової номінальної напруги.[^aac-direct-current]

Приклад: батареї з різницею потенціалів `0.5 V` і сумарним еквівалентним опором `0.1 Ω` дали б початкову оцінку `5 A` за законом Ома. Це лише лінійна оцінка для заданої моделі: фактичний опір залежить від температури, заряду, хімічної поляризації та проводки, а струм може бути небезпечно великим.

**Типова помилка:** вважати, що однаковий напис «12 V» означає однакову фактичну напругу або автоматично дозволяє з’єднання. Перевіряють реальні напруги та документацію виробника, а батареї різних хімій чи конструкцій без прямого дозволу виробника не паралелять.[^aac-direct-current]

## Sources

<!-- generated from frontmatter -->
