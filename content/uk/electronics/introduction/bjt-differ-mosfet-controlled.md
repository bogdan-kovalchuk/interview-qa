---
id: emb-elintro-0008
title: Чим `BJT` відрізняється від `MOSFET` за принципом керування?
description: Чим `BJT` відрізняється від `MOSFET` за принципом керування?
track: electronics
section: introduction
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
anki:
  export: true
sources:
- source_id: udemy-electronics-course
  title: 'Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу'
  url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  accessed: 2026-09-27
  kind: community
  version: null
  applicability: 'Historical question provenance: lecture 3 of the Udemy course. Original flashcards remain in imports.
    Current answers and explanations were independently revised against cited technical sources on 2026-10-04; this
    source is not factual proof of the revised prose.'
- source_id: aac-direct-current
  title: 'All About Circuits textbook, Volume I: DC'
  url: https://www.allaboutcircuits.com/textbook/direct-current/
  accessed: 2026-09-27
  kind: book
  version: null
  applicability: 'Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання;
    конкретні номінали й схеми курсу можуть відрізнятися.'
- source_id: aac-semiconductors
  title: 'All About Circuits textbook, Volume III: Semiconductors'
  url: https://www.allaboutcircuits.com/textbook/semiconductors/
  accessed: 2026-09-27
  kind: book
  version: null
  applicability: 'Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела
    живлення; конкретні номінали й схеми курсу можуть відрізнятися.'
- source_id: ti-gate
  title: 'TI SLUA618A: Fundamentals of MOSFET and IGBT gate driver circuits'
  url: https://www.ti.com/lit/ug/slua618a/slua618a.pdf
  accessed: 2026-10-04
  kind: official
  version: SLUA618A
  applicability: Gate charge, driver current and power; section 2.7.
---

## Short answer

BJT зазвичай потребує base current для керування collector current; MOSFET керується gate-to-source voltage. Gate MOSFET споживає дуже малий steady-state current, але switching потребує заряджання й розряджання його capacitances. Менші сумарні power losses залежать від застосування й не гарантовані самим voltage control. [^ti-gate] [^aac-semiconductors]

## Detailed explanation

«Current controlled» – практичний вступний опис BJT drive: driver забезпечує base current. Це не повне рівняння transistor, і current gain не є сталою для всіх робочих точок, особливо saturation. Для MOSFET потрібна напруга gate відносно source, а не gate відносно довільного ground. [^aac-semiconductors]

Insulated gate потребує малого DC струму після встановлення напруги. Проте на кожному switching transition driver має перемістити gate charge. TI наводить середній gate-drive current приблизно `I = Q_G*f` та gate-drive power приблизно `P = V_drive*Q_G*f`. Gate charge залежить від указаних operating conditions. [^ti-gate]

Для ілюстративних припущень `Q_G = 20 nC`, `f = 100 kHz` та drive 10 V ці співвідношення дають середній струм живлення 2 mA і gate-drive power 20 mW. Peak transition current може бути значно більшим. Сумарна efficiency також залежить від conduction loss, transition duration, навантаження та driver design; порівнюйте повні operating conditions, а не лише назву способу керування.

## Sources

<!-- generated from frontmatter -->
