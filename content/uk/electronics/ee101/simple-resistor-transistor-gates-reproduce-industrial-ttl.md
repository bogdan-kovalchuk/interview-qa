---
id: emb-elee-0238
title: "Чи відтворюють прості резисторно-транзисторні вентилі промислову TTL?"
description: "Чи відтворюють прості резисторно-транзисторні вентилі промислову TTL?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-14
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
    applicability: "Походження питання: лекція 76, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-14; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: ti-sn74ls00
    title: "TI SDLS025D: SNx400, SNx4LS00, SNx4S00 quadruple 2-input NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74ls00.pdf
    accessed: 2026-10-14
    kind: official
    version: "SDLS025D"
    applicability: "Розділ 6.5 (SNx400, TTL): VOH (min) 2,4 В при IOH -0,4 мА і VOL (max) 0,4 В при IOL 16 мА. Розділ 11: багатоемітерні входи серій SN74 і SN74S. Вхідні рівні TTL: VIH 2 В, VIL 0,8 В. RTL не описує."
  - source_id: adi-ttl-lab
    title: "Analog Devices Wiki: TTL inverter and NAND gate activity for ADALM2000"
    url: https://wiki.analog.com/university/courses/electronics/electronics-lab-27
    accessed: 2026-10-14
    kind: official
    version: null
    applicability: "Вендорна лабораторна робота ADALM2000: TTL-інвертор із вхідним каскадом, фазорозщеплювачем і вихідною парою totem-pole, яка може і джерелити, і стікати струм. Це не datasheet, гарантованих рівнів немає."
  - source_id: utah-cs6710-diode-logic
    title: "Logic Gates from Resistors, Diodes, and Transistors (B.2), handout CS 6710, University of Utah"
    url: https://my.eng.utah.edu/~cs6710/handouts/AppendixB/appendixB.doc2.html
    accessed: 2026-10-14
    kind: book
    version: "last updated 1996-07-16"
    applicability: "Лекційний матеріал 1996 року (розділ B.2): резистор навантаження (pull-up) і транзистор замість нижнього резистора дають інвертор; падіння на діоді близько 0,7 В. Не містить параметрів конкретних приладів."
---

## Short answer

Ні. Логічна функція та сама. Серії SN74 мають багатоемітерні входи[^ti-sn74ls00], а TTL – вихід totem-pole[^adi-ttl-lab], тоді як RTL-вентиль має резистор pull-up.[^utah-cs6710-diode-logic] Тому гарантовані рівні й навантаження не збігаються, і сумісність перевіряють за datasheet.

## Detailed explanation

Пастка в тому, що логічна таблиця однакова, а електрика ні. RTL-вентиль має резистор від виходу до плюса і транзистори, що тягнуть вихід до землі. Високий рівень задає лише резистор, тому вихід слабо тягне вгору. TTL має вихід totem-pole: верхній транзистор активно тягне вихід до високого рівня, а нижній – до низького. Тому TTL-вихід здатен і джерелити, і стікати струм.[^adi-ttl-lab]

Гарантії TTL задано цифрами в datasheet: `VIH,min = 2 V`, `VIL,max = 0.8 V`, `VOH,min = 2.4 V` при струмі 0,4 мА і `VOL,max = 0.4 V` при 16 мА.[^ti-sn74ls00] Це зобов’язання виробника для конкретних умов. RTL-вентиль з довільними резисторами таких гарантій сам по собі не має: його `VOL` залежить від насичення транзистора, а `VOH` від падіння на резисторі, тож рівні треба рахувати для кожного навантаження.

Входи серій SN74 і SN74S – багатоемітерні транзистори, і datasheet окремо застерігає: напруга понад 5,5 В на таких входах пробиває перехід база–емітер.[^ti-sn74ls00] Тому однакова таблиця істинності не означає сумісності: вхідний струм, допустима напруга входу та вихідні рівні в цих схемах різні.

**Типові помилки:**

- Вважати, що однакова таблиця істинності означає сумісність: логічна функція не гарантує рівнів, навантаження чи швидкості.
- Подавати напругу понад 5,5 В на входи серій SN74 і SN74S, що пробиває їхній багатоемітерний вхід.[^ti-sn74ls00]
- Вважати RTL-вихід придатним замість TTL-виходу без розрахунку: TTL-вихід гарантує `VOL ≤ 0.4 V` при `IOL` до 16 мА, а RTL такої гарантії не має.[^ti-sn74ls00]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
