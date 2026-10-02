---
id: emb-elintro-0081
title: "Що таке VCVS і яке його типове застосування?"
description: "Що таке VCVS і яке його типове застосування?"
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
    applicability: "Походження питання: лекція 9, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-dependent-sources
    title: "All About Circuits: Nodal Analysis and Dependent Sources"
    url: https://www.allaboutcircuits.com/technical-articles/nodal-analysis-and-dependent-sources/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Визначення VCVS як залежного джерела напруги та його коефіцієнт передачі; приклади аналізу схем."
---


## Short answer

VCVS (Voltage-Controlled Voltage Source) – ідеалізоване залежне джерело, у якому вихідна напруга пропорційна керувальній напрузі: `V_out = A_v*V_control`. Модель op-amp часто подають як VCVS із великим відкритим коефіцієнтом підсилення, але реальний op-amp – це складна схема, а не саме ідеальне джерело.[^aac-dependent-sources]

## Detailed explanation

VCVS належить до залежних джерел: на схемі його вихідна напруга не задається сталою батареєю, а визначається іншою напругою в колі. Для лінійної моделі співвідношення записують як `V_out = A_v*V_control`, де `A_v` – безрозмірний коефіцієнт передавання, а `V_control` вимірюють між визначеними контрольними вузлами. Полярність джерела та знак коефіцієнта визначають, чи вихід повторює контрольну напругу, чи інвертує її.[^aac-dependent-sources]

VCVS корисний у схемному аналізі, бо дає змогу описати підсилення без моделювання кожного транзистора. Наприклад, у SPICE ним можна наближено подати вихідний зв’язок op-amp: велике відкрите підсилення множить різницю напруг на входах. Це ідеалізація; джерело в простій моделі може не мати обмежень живлення, вихідного струму, смуги пропускання чи швидкості наростання, які є в реального компонента.[^aac-dependent-sources]

У зворотному зв’язку від’ємний сигнал із виходу повертається на вхід так, щоб зменшити різницю між контрольними входами. Резистори чи інші елементи задають частину вихідної напруги, яку повертають, а велике відкрите підсилення змушує замкнену схему підтримувати малу похибку, поки вона працює в лінійному режимі. Якщо вихід упирається в межу живлення або навантаження вимагає надмірного струму, ця умова перестає виконуватися й проста формула підсилення вже не описує результат.[^aac-dependent-sources]

Приклад: для `A_v = 10` і контрольної напруги `V_control = 0.2 V` ідеальна модель дає `V_out = 2 V`. Це не гарантує, що реальний op-amp здатен видати 2 V: перевіряють його живлення, допустимий діапазон входів і виходу та навантаження. Типова помилка – назвати будь-який op-amp VCVS; коректніше сказати, що VCVS є корисною моделлю його підсилювальної поведінки.[^aac-dependent-sources]

## Sources

<!-- generated from frontmatter -->
