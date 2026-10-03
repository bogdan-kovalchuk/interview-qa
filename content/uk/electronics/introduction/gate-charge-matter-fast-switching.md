---
id: emb-elintro-0258
title: "Що таке gate charge і чому він важливий у швидкому перемиканні?"
description: "Що таке gate charge і чому він важливий у швидкому перемиканні?"
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
  - source_id: infineon-gate-drive
    title: "Infineon: Gate drive for power MOSFETs in switching applications"
    url: https://www.infineon.com/assets/row/public/documents/24/42/infineon-gate-drive-for-power-mosfets-in-switchtin-applications-applicationnotes-en.pdf?fileId=8ac78c8c80027ecd0180467c871b3622
    accessed: 2026-10-04
    kind: official
    version: "V1.0, 2022-04-20"
    applicability: "Описує gate charge, Miller plateau і вплив gate current на час перемикання; числові параметри залежать від MOSFET та умов."
  - source_id: ti-mosfet-selection
    title: "Texas Instruments: MOSFET Selection Guide for BQ2575x Family"
    url: https://www.ti.com/lit/an/sluaax9/sluaax9.pdf
    accessed: 2026-10-04
    kind: official
    version: "SLUAAX9, June 2025"
    applicability: "Пояснює QG, QGD, втрати та теплові параметри у контексті BQ2575x; конкретні розрахунки залежать від схеми."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

`Q_g` – заряд, потрібний для зміни стану gate за заданих умов вимірювання; він впливає на струм драйвера та час перемикання, але сам по собі не визначає його.[^infineon-gate-drive] Для однакового драйвера більший заряд зазвичай потребує більшого часу, а switching losses залежать також від напруги, струму й частоти.[^ti-mosfet-selection]

## Detailed explanation

Gate charge `Q_g` – кількість заряду, яку драйвер має подати на gate під час перемикання MOSFET. Gate ізольований, але має ємності gate-source та gate-drain, тому для перемикання потрібні короткі імпульси струму на заряджання й розряджання. У datasheet `Q_g` наводять разом з умовами тесту, бо значення залежить від drain voltage, drain current і кінцевої напруги керування.[^infineon-gate-drive]

Поки gate заряджається, `V_GS` зростає, а після досягнення Miller plateau значна частина струму змінює drain voltage через ємність gate-drain. Цей проміжок впливає на швидкість фронту, електромагнітні завади та switching losses. Більше `Q_g` за того самого доступного gate current зазвичай означає довше перемикання; більша частота також збільшує середній струм драйвера. Груба оцінка споживання драйвера має вигляд `P_gate ≈ Q_g*V_drive*f_sw`, але це не дорівнює повним втратам MOSFET.[^infineon-gate-drive] [^ti-mosfet-selection]

При виборі не мінімізуйте `Q_g` ізольовано. MOSFET з меншим `R_DS(on)` може мати більшу площу кристала й більший gate charge, а кінцевий компроміс залежить від частоти, навантаження та того, чи домінують conduction чи switching losses. Важливий також `Q_GD`, оскільки він пов’язаний із проходженням Miller plateau, та здатність драйвера віддавати й поглинати струм. Порівнюйте кандидатів за однакових тестових умов, а не лише за одним числом із заголовка datasheet.[^ti-mosfet-selection]

**Типові помилки:**

- Називати `Q_g` сталою ємністю. Заряд залежить від траєкторії напруг та умов тесту.
- Вважати великий `Q_g` єдиною причиною повільного перемикання: обмеження драйвера і резистор gate теж важливі.
- Ототожнювати оцінку втрат драйвера з повними switching losses транзистора.

## Sources

<!-- generated from frontmatter -->
