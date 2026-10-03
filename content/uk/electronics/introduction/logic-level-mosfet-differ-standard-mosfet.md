---
id: emb-elintro-0249
title: "Чим `logic-level MOSFET` відрізняється від стандартного MOSFET?"
description: "Чим `logic-level MOSFET` відрізняється від стандартного MOSFET?"
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
  - source_id: infineon-logic-level-mosfet
    title: "Infineon: OptiMOS logic level MOSFETs"
    url: https://www.infineon.com/products/power/mosfet/n-channel/optimos-strongirfet/optimos-ir-mosfet-logic-level?page=2
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Описує logic-level MOSFET як придатні для нижчих рівнів gate drive, зокрема 5 V; фактичне значення R_DS(on) слід перевіряти в datasheet конкретної деталі."
---

## Short answer

Logic-level MOSFET спроєктований так, щоб забезпечувати потрібний `R_DS(on)` за нижчої `V_GS`.[^infineon-logic-level-mosfet] Допустиму напругу керування й опір перевіряють за умовами datasheet, а не за назвою класу.[^infineon-logic-level-mosfet]

## Detailed explanation

Термін `logic-level` описує пристрій, чиї характеристики узгоджені з нижчими рівнями керування, поширеними в цифрових схемах і мікроконтролерах. На відміну від MOSFET, для якого низький `R_DS(on)` гарантований лише за вищої напруги gate, відповідна logic-level деталь може мати специфікований `R_DS(on)` уже при меншій `V_GS`. Це не означає, що будь-який такий транзистор повністю відкриється від будь-якого GPIO: перевірте конкретний тестовий рівень у таблиці параметрів.[^infineon-logic-level-mosfet]

У datasheet `R_DS(on)` наводять разом з умовами вимірювання, зокрема `V_GS`, струмом drain і часто температурою. Саме ця величина дає змогу оцінити провідникові втрати, наприклад `P = I_D²*R_DS(on)`, тоді як назва `logic-level` сама по собі не задає ні точного опору, ні максимального струму. Також звіряйте абсолютний максимум напруги gate, щоб не пошкодити оксид.[^infineon-logic-level-mosfet]

Позначення `standard` не є достатньою специфікацією і не встановлює універсальний рівень `10 V`. Це поширена умова тестування багатьох силових MOSFET, але інші деталі можуть мати таблицю для 4.5 V, 2.5 V або іншої напруги. Порівнюючи кандидати, використовуйте той `R_DS(on)`, який гарантовано за вашої фактичної напруги між gate і source, включно з падінням на драйвері та варіаціями живлення.[^infineon-logic-level-mosfet]

**Типова помилка:** ототожнювати низьку `V_GS(th)` із logic-level придатністю. Threshold означає лише початок провідності за малого тестового струму; потрібний опір у робочій точці – інша характеристика.

Приклад: для GPIO з рівнем `3.3 V` шукайте в datasheet гарантоване значення `R_DS(on)` при `V_GS` не більшій за доступну напругу з урахуванням запасу. Якщо таблиця гарантує опір тільки при `10 V`, така деталь не підтверджує належну роботу від 3.3 V без окремої схеми драйвера.[^infineon-logic-level-mosfet]

## Sources

<!-- generated from frontmatter -->
