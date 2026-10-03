---
id: emb-elintro-0243
title: "Що таке R_DS(on) і чому він важливий?"
description: "Що таке R_DS(on) і чому він важливий?"
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

`R_DS(on)` – опір каналу між drain і source у відкритому MOSFET за заданих умов, зокрема `V_GS` і температури. Для сталого струму провідникові втрати приблизно `P = I²*R_DS(on)`, тож менший опір зменшує саме ці втрати; він не враховує перемикання, керування затвором та інші втрати.[^toshiba-mosfet-drive]

## Detailed explanation

`R_DS(on)` – це опір каналу MOSFET між drain і source, коли транзистор належно керується у відкритому стані. Це параметр провідності силового ключа, а не незмінний резистор, що діє за будь-якої напруги та температури.[^toshiba-mosfet-drive]

Виробник задає `R_DS(on)` за конкретних `V_GS` і температури переходу. Якщо драйвер подає лише напругу, близьку до `V_th`, MOSFET може почати проводити, але канал ще не матиме малого опору, вказаного в таблиці. Для вибору компонента звіряйте гарантоване значення за реально доступної напруги затвора; також враховуйте, що опір зазвичай зростає з нагріванням.[^toshiba-mosfet-drive]

Коли через канал тече струм, його опір спричиняє падіння напруги та нагрів. Для приблизно сталого струму використовують `P = I²*R_DS(on)`. Наприклад, при `I = 5 A` і `R_DS(on) = 25 mΩ` ідеалізоване наближення дає `P = 5²*0.025 = 0.625 W`; це розрахунок лише провідникової складової, за припущення сталих 25 mΩ.[^toshiba-mosfet-drive]

У реальній схемі опір залежить від нагрівання, розкиду параметрів і режиму керування. Перевірте тепловий опір корпусу й плати та робочу точку: мале значення `R_DS(on)` саме по собі не гарантує допустимої температури. За імпульсного перемикання додатково виникають switching loss і gate-drive loss, яких проста формула не описує.[^toshiba-mosfet-drive]

**Типова помилка:** брати найменше число `R_DS(on)` із заголовка datasheet без перевірки умов тесту. Переконайтеся, що таблиця гарантує це значення при вашому `V_GS`, а оцінку нагрівання робіть для струму й температури реального застосування.[^toshiba-mosfet-drive]

## Sources

<!-- generated from frontmatter -->
