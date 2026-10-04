---
id: emb-elee-0102
title: "Що децибели не показують про підсилювач і які позначення потребують обережності?"
description: "Що децибели не показують про підсилювач і які позначення потребують обережності?"
track: electronics
section: ee101
level: junior
type: pitfall
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
    applicability: "Походження питання: лекція 49, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-decibels
    title: "All About Circuits: Decibels for Voltage and Power Ratios"
    url: https://www.allaboutcircuits.com/textbook/designing-analog-chips/analog-measurements/db-for-voltage-add-power-ratios/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтримує відношення амплітуд і знакове підсумовування gain; dB задають модуль, не фазу."
  - source_id: keysight-db-reference
    title: "Keysight U1271A/U1272A Handheld Digital Multimeter User's Guide"
    url: https://www.keysight.com/am/en/assets/9018-03364/user-manuals/9018-03364.pdf
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Розрізняє dBV відносно 1 V та dBm відносно 1 mW із заданим опорним опором; стосується описаних режимів вимірювання мультиметра."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

dB описують модуль передавання, а не фазу: коефіцієнт напруги −10 має модуль 10, тобто 20 dB, і водночас означає інверсію фази. Позначення dBV задає рівень напруги відносно 1 V. Позначення dBm задає рівень потужності відносно 1 mW, а для перерахунку виміряної напруги потрібен опорний опір.[^aac-decibels] [^keysight-db-reference]

## Detailed explanation

Децибели описують логарифмічне відношення рівнів, але знак такого відношення не кодує фазу. Для коефіцієнта напруги використовують `G_dB = 20*log10(|V_out/V_in|)`. Якщо каскад має коефіцієнт `-10`, його модуль дорівнює 10, отже gain за амплітудою становить `20 dB`; знак мінус показує, що сигнал інвертовано на 180° для синусоїди, а не що gain у dB від’ємний.[^aac-decibels]

Це важливо при каскадуванні: значення в dB дозволяють скласти модулі коефіцієнтів, але для відновлення форми сигналу й знака потрібно знати фазу або полярність. Від’ємні dB означають ослаблення амплітуди відносно опорного рівня, тоді як інверсія – окрема фазова властивість. Наприклад, інвертувальний каскад із коефіцієнтом `-10` дає `20 dB` за модулем, хоча вихід синусоїди протилежний за фазою.[^aac-decibels]

Абсолютні рівні теж мають різні позначення. `dBV` – рівень напруги відносно 1 V RMS. `dBm` – рівень потужності відносно 1 mW; при перетворенні виміряної напруги у dBm прилад мусить використовувати заданий опорний опір. Отже, одне число в dBm не визначає напругу без цього опору. Позначення на кшталт `dBv` варто звіряти з документацією конкретного приладу або джерела, а не трактувати як універсальний стандартний запис.[^keysight-db-reference]

**Типова помилка:** прочитати `-10` як від’ємний gain у dB або зробити висновок про фазу з одного лише значення dB. Це призводить до хибного прогнозу рівня чи форми вихідного сигналу. Записуйте окремо модуль gain у dB та фазу/інверсію; для абсолютних одиниць фіксуйте опорний рівень і, для dBm, опір, який застосовано при вимірюванні.[^aac-decibels] [^keysight-db-reference]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
