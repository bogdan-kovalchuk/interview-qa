---
id: emb-elintro-0027
title: "Як орієнтувати `DIP`-мікросхему й знайти pin 1?"
description: "Як орієнтувати `DIP`-мікросхему й знайти pin 1?"
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
    applicability: "Походження питання: лекція 4, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: ti-sn74hc04-pinout
    title: "Texas Instruments: SNx4HC04 Hex Inverters datasheet, Rev. H"
    url: https://www.ti.com/lit/ds/symlink/sn74hc04.pdf
    accessed: 2026-10-04
    kind: official
    version: "Rev. H, April 2021"
    applicability: "Ілюструє індекс pin 1 у конкретному корпусі TI CDIP; позначки й виводи інших мікросхем треба звіряти з їхніми datasheet."
---

## Short answer

Виріз або крапка часто позначає бік pin 1, але точну орієнтацію перевіряйте за datasheet конкретної мікросхеми. Для корпусу TI CDIP у прикладі виробника позначений pin 1; не вважайте положення вирізу універсальним правилом.[^ti-sn74hc04-pinout]

## Detailed explanation

Pin 1 – це початок нумерації виводів, а його положення визначає виробник для конкретного корпусу та компонента. На корпусі його часто позначають крапкою, виїмкою або іншим індексом, однак вигляд і розміщення позначки можуть різнитися; спершу знайдіть відповідний package drawing або pin configuration у datasheet саме цієї мікросхеми.[^ti-sn74hc04-pinout]

Для звичного дворядного `DIP` із виїмкою зверху типовий вигляд зверху показує pin 1 у верхньому лівому куті, а послідовність номерів обходить корпус проти годинникової стрілки. Це корисна підказка, а не заміна документації: деякі корпуси мають крапку замість виїмки, а спеціальні виконання чи інші типи корпусу можуть інакше позначати індекс.[^ti-sn74hc04-pinout]

Перед установленням сумістіть позначку pin 1 на платі з кресленням корпусу в документації; не орієнтуйте компонент лише за напрямком тексту на кришці. У даташиті TI для SNx4HC04 окремо показано положення pin 1 для CDIP, що демонструє, чому перевірка конкретного package drawing надійніша за загальне правило.[^ti-sn74hc04-pinout]

**Типова помилка:** переплутати верх корпусу з боком pin 1. Якщо маркування нечітке або відсутнє, зупиніться й знайдіть part number та його pinout у документації до монтажу.

## Sources

<!-- generated from frontmatter -->
