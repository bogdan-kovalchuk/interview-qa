---
id: emb-elintro-0244
title: "Чому MOSFET ефективний для великих струмів?"
description: "Чому MOSFET ефективний для великих струмів?"
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
  - source_id: toshiba-mosfet-drive
    title: "Toshiba: MOSFET Gate Drive Circuit, Application Note"
    url: https://toshiba.semicon-storage.com/info/TPH4R50ANH1_application_note_en_20180726_AKX00068.pdf?did=59460&prodName=TPH4R50ANH1
    accessed: 2026-10-04
    kind: official
    version: "AKX00068-1, 2018-07-26"
    applicability: "Режими роботи MOSFET, умови відкривання, залежність R_DS(on) від V_GS і температури та втрати перемикання."
---

## Short answer

За достатньої напруги затвора силовий MOSFET може мати малий `R_DS(on)`, що дає невеликі провідникові втрати навіть за значного струму. Наприклад, ідеалізовані 5 A через 25 mΩ дають `P = I²*R = 0.625 W`; це не включає switching loss, втрати драйвера чи нагрівання, яке змінює опір.[^toshiba-mosfet-drive]

## Detailed explanation

MOSFET може бути ефективним силовим ключем за великих струмів, коли він повністю керується і має малий `R_DS(on)`. У відкритому стані канал створює падіння напруги, тож провідникова потужність приблизно дорівнює `I²*R_DS(on)`. Залежність квадратична: подвоєння струму за того самого опору збільшує ці втрати вчетверо.[^toshiba-mosfet-drive]

Наприклад, за умов сталого `R_DS(on) = 25 mΩ` і струму `5 A` наближена втрата становить `0.625 W`. Це лише приклад обчислення, а не універсальна характеристика MOSFET: реальний `R_DS(on)` залежить від напруги затвора й температури, тому потрібне значення треба брати з datasheet для відповідних умов. Якщо затвор керується недостатньо, канал може мати більший опір і сильно нагріватися.[^toshiba-mosfet-drive]

Малий опір каналу допомагає зменшити втрати провідності, але сам по собі не визначає загальну ефективність. У кожному циклі перемикання напруга й струм певний час перекриваються; додатково драйвер витрачає енергію на заряд і розряд затвора. За високої частоти ці складові можуть бути суттєвими, тому треба оцінювати весь режим, а не лише максимальний струм із таблиці.[^toshiba-mosfet-drive]

Також перевіряють тепловідведення, допустиму температуру переходу, корпус, мідь плати та межі safe operating area. Високий струм безперервно проходить через конкретну конструкцію плати, і допустимий струм із datasheet часто передбачає задану температуру корпусу або ідеальне охолодження; це не обіцянка, що будь-яка плата витримає такий струм.[^toshiba-mosfet-drive]

**Типова помилка:** називати MOSFET ефективним лише тому, що його можна відкрити логічним сигналом або тому, що в таблиці є великий `I_D`. Перевірте гарантований `R_DS(on)` при наявному `V_GS`, втрати перемикання та теплові умови саме вашої схеми.[^toshiba-mosfet-drive]

## Sources

<!-- generated from frontmatter -->
