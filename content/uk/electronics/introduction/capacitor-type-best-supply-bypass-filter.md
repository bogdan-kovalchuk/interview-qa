---
id: emb-elintro-0132
title: "Який тип конденсатора найкраще підходить для bypass-фільтру на живленні?"
description: "Який тип конденсатора найкраще підходить для bypass-фільтру на живленні?"
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
    applicability: "Розділ Input and Output Capacitor Selection наводить приклад buck-конвертера з керамічними та електролітичними вхідними конденсаторами паралельно й пояснює роль ESR, ємності та ripple current; це не універсальна схема для кожного джерела."
---

## Short answer

Для локального високочастотного bypass зазвичай обирають MLCC через малі ESR та ESL. Для bulk-фільтрації чи значного ripple current можуть додати електролітичний конденсатор; тип і номінал залежать від вимог схеми, робочої частоти та datasheet мікросхеми.[^analog-devices-an140-capacitor-selection] У керамічного конденсатора перевіряють ефективну ємність за робочої напруги.[^analog-devices-an140-capacitor-selection]

## Detailed explanation

Для високочастотного bypass біля мікросхеми зазвичай обирають MLCC (multilayer ceramic capacitor): він компактний і має низькі ESR та ESL, що допомагає подавати короткі імпульси струму й зменшувати високочастотний імпеданс живлення.[^analog-devices-an140-capacitor-selection]

Однак «найкращий тип» залежить від функції конденсатора. У buck-конвертері керамічний конденсатор може працювати паралельно з алюмінієвим електролітичним: вибір враховує RMS ripple current, потрібну ємність, навантаження та робочі частоти. Для кожної конкретної мікросхеми також перевіряють рекомендовані номінали й вимоги до стабільності.[^analog-devices-an140-capacitor-selection]

Номінал на корпусі керамічного конденсатора не завжди дорівнює його ефективній ємності під напругою. Діелектрики на кшталт X5R або X7R можуть втрачати частину ємності через DC bias і температуру, тому треба перевірити графік конкретного компонента в діапазоні робочих напруг.[^analog-devices-an140-capacitor-selection]

**Типова помилка:** поставити один і той самий конденсатор далеко від навантаження й очікувати, що він прибере всі пульсації. Для локального bypass важливе коротке з’єднання між виводом живлення та ground; довгі доріжки додають паразитну індуктивність. Приклад конкретного рішення для buck-живлення – паралельні MLCC та електролітичний конденсатор на вході, якщо цього вимагають струм пульсацій і схема.[^analog-devices-an140-capacitor-selection]

## Sources

<!-- generated from frontmatter -->
