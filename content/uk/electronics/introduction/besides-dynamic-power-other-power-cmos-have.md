---
id: emb-elintro-0100
title: "У CMOS окрім динамічної потужності є ще яка?"
description: "У CMOS окрім динамічної потужності є ще яка?"
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
    applicability: "Походження питання: лекція 10, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: ti-cmos-power
    title: "CMOS Power Consumption and CPD Calculation"
    url: https://www.ti.com/lit/an/scaa035b/scaa035b.pdf
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Для CMOS-логіки описує статичну потужність від leakage current, динамічну потужність, перехідні струми та навантажувальну ємність; деталі залежать від сімейства IC."
---

## Short answer

Окрім dynamic power під час перемикання, CMOS-логіка має static power, переважно через leakage current навіть за стабільних логічних рівнів. Під час переходу можливий короткий through current, коли обидва транзистори інвертора частково відкриті; ємність навантаження також додає динамічне споживання.[^ti-cmos-power]

## Detailed explanation

У CMOS-логіці, крім потужності перемикання, є статичне споживання. У простій CMOS-інверторній моделі за стабільного логічного рівня один транзистор увімкнений, а інший вимкнений, тому постійний шлях від живлення до землі майже відсутній. Реальний IC все одно має leakage current, а деякі внутрішні блоки можуть споживати струм спокою; добуток цього струму на напругу живлення дає внесок у static power.[^ti-cmos-power]

Під час зміни логічного стану вузли заряджаються й розряджаються. Частина енергії витрачається на внутрішні паразитні ємності транзисторів, а частина – на ємність вихідного навантаження, наприклад доріжки, входи інших мікросхем або кабелю. Вхід із повільним фронтом може довше тримати PMOS і NMOS частково відкритими одночасно, створюючи короткий струм напряму від живлення до землі. Цей through current теж належить до перехідного споживання під час перемикання, а не є тотожним статичному leakage.[^ti-cmos-power]

У першому наближенні динамічне споживання зростає зі switching frequency, напругою живлення в квадраті та сумарною перемикною ємністю. Отже, воно може домінувати в активному швидкому пристрої, тоді як у режимі очікування частіше помітним стає leakage або споживання аналогових та інших спеціалізованих блоків. Співвідношення залежить від технології, температури, частоти, навантаження й конкретного IC, тому «CMOS не споживає потужності у спокої» – лише спрощення.[^ti-cmos-power]

Приклад: якщо інвертор перемикає вихід, з’єднаний із великою ємністю, джерело мусить заряджати й розряджати її на кожному переході. Зменшення частоти переходів або ємності навантаження зменшує цей внесок; зупинка перемикань не усуває leakage та струм спокою інших блоків. Точну оцінку беруть із datasheet і методики виробника для потрібної напруги, температури та режиму.[^ti-cmos-power]

**Типова помилка:** звести всі втрати до dynamic power або, навпаки, вважати through current постійним струмом у сталому логічному стані. Розділяйте втрати спокою та втрати, що виникають під час фронтів і заряджання ємностей.

## Sources

<!-- generated from frontmatter -->
