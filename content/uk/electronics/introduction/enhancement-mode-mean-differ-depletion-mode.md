---
id: emb-elintro-0247
title: "Що означає `enhancement mode` і чим він відрізняється від `depletion mode`?"
description: "Що означає `enhancement mode` і чим він відрізняється від `depletion mode`?"
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
    applicability: "Походження питання: лекція 22, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: ti-mosfet-modes-an558
    title: "Texas Instruments: AN-558 Introduction to Power MOSFETs and Their Applications"
    url: https://www.ti.com/lit/an/snva008/snva008.pdf
    accessed: 2026-10-04
    kind: official
    version: "AN-558"
    applicability: "Визначає enhancement MOSFET як normally off, а depletion MOSFET як normally on; наведений опис стосується основного принципу роботи, а не всіх особливостей конкретних типів."
---

## Short answer

Enhancement-mode MOSFET за `V_GS = 0` зазвичай вимкнений, а depletion-mode – увімкнений.[^ti-mosfet-modes-an558] Знак керувальної `V_GS`, потрібний для зміни стану, залежить від каналу й компонента.[^ti-mosfet-modes-an558]

## Detailed explanation

Назва описує стан каналу за відсутності керувальної напруги gate-to-source. В enhancement-mode MOSFET канал не є достатньо провідним при нульовій `V_GS`, тому для його утворення потрібне поле від gate. У типовому N-channel пристрої позитивна `V_GS` створює канал; у P-channel пристрої полярність керування протилежна. Величину напруги не можна виводити лише зі слова enhancement: її визначають за datasheet.[^ti-mosfet-modes-an558]

У depletion mode провідний канал існує вже без сигналу на gate. Керувальна напруга змінює кількість носіїв у каналі й може збіднити його настільки, що струм припиниться. Для класичного N-channel depletion MOSFET вимикання потребує від’ємної `V_GS`; у P-channel знаки протилежні. Отже, «нормально увімкнений» означає стан за визначеної напруги між gate і source, а не довільний стан за плаваючого gate.[^ti-mosfet-modes-an558]

Ця різниця впливає на поведінку схеми під час запуску та обриву керування. Normally-off ключ часто зручний для навантаження, яке має залишатися вимкненим до команди. Normally-on пристрій може бути корисним там, де потрібна провідність без живлення керування, але такий стан потребує відповідного захисту й схеми вимкнення. Не плутайте режим каналу з логічним рівнем: `logic-level` стосується придатності керувальної напруги для повного потрібного режиму, а не того, чи є транзистор enhancement чи depletion.[^ti-mosfet-modes-an558]

**Типова помилка:** називати будь-який MOSFET «нормально вимкненим» без уточнення режиму. Перевірте таблицю характеристик та схему конкретного компонента, особливо якщо стан після reset або втрати живлення має бути безпечним.

Приклад: enhancement N-channel MOSFET із source на спільному нулі за `V_GS = 0` має бути вимкненим у межах паспортного витоку; для ввімкнення gate підіймають відносно source. Такий приклад не переноситься без зміни полярності на P-channel чи depletion-пристрій.[^ti-mosfet-modes-an558]

## Sources

<!-- generated from frontmatter -->
