---
id: emb-elintro-0201
title: "Які три режими роботи має `BJT`?"
description: "Які три режими роботи має `BJT`?"
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
    applicability: "Походження питання: лекція 19, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-bjt-active-mode
    title: "Active-mode Operation (BJT), All About Circuits"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/active-mode-operation-bjt/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Визначення режимів cutoff, active та saturation і межа між керуванням струмом та обмеженням навантаженням."
---

## Short answer

Основні режими: cutoff (відсічка), active (активний) і saturation (насичення). У cutoff струм колектора практично відсутній, в active базовий струм керує струмом колектора, а в saturation його вже обмежує зовнішнє коло навантаження.[^aac-bjt-active-mode]

## Detailed explanation

Режими `BJT` розрізняють за станом переходів і тим, що обмежує струм колектора. У cutoff транзистор майже закритий: перехід база–емітер не має достатнього прямого зміщення, тому струми колектора й бази малі, хоча реальний компонент має витік. Це наближення відповідає розімкненому ключу, а не абсолютному нулю струму.[^aac-bjt-active-mode]

В active перехід база–емітер прямо зміщений, а база–колектор зазвичай зворотно зміщений. У межах робочих умов зміна базового струму керує струмом колектора; співвідношення `I_C ≈ β*I_B` є наближеною моделлю, а β залежить від компонента та режиму. Саме цю область використовують для підсилення, коли робоча точка не доходить до cutoff чи saturation.[^aac-bjt-active-mode]

У saturation обидва переходи прямо зміщені, і навантаження разом із живленням визначає доступний струм. Додатковий базовий струм вже не дає пропорційного збільшення `I_C`, тому формула активного режиму непридатна. `V_CE(sat)` не є універсально фіксованими 0.1 V: значення залежить від транзистора й струмів, а паспорт задає його за конкретних умов.[^aac-bjt-active-mode]

**Приклад перемикання:** коли `BJT` керує навантаженням, у вимкненому стані його наближено вважають cutoff, а у ввімкненому – saturation. Для лінійного підсилювача ж прагнуть залишити сигнал у active, щоб вихід не обрізався обома межами.[^aac-bjt-active-mode]

**Типова помилка:** називати active просто «частково відкритим ключем». Це приховує його призначення як режиму керованого підсилення та плутає з ключовим застосуванням; перевіряйте, чи струм обмежений керуванням базою, чи вже навантаженням.

## Sources

<!-- generated from frontmatter -->
