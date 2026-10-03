---
id: emb-elintro-0277
title: "Що означає правило `AWG`: більший номер – тонший дріт?"
description: "Що означає правило `AWG`: більший номер – тонший дріт?"
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
    applicability: "Походження питання: лекція 25, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: nist-awg-wire-diameter
    title: "NIST: Evaluation of Wire Detection in X-Ray Images"
    url: https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=919567
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Наводить конкретні діаметри AWG 20, 24 і 30; підтримує порівняння номеру й діаметра, але не визначає допустимий струм проводу."
---

## Short answer

В American Wire Gauge більший номер означає менший діаметр і, за однакового металу та довжини, більший опір проводу. Наприклад, 30 AWG значно тонший за 22 AWG; допустимий струм не визначається лише номером AWG.[^nist-awg-wire-diameter]

## Detailed explanation

American Wire Gauge (AWG) – це система позначення діаметра дроту, в якій числовий номер поводиться неінтуїтивно: що він більший, то тонша жила. Наприклад, у таблиці NIST діаметр проводу 24 AWG наведений як `0.511 mm`, а 30 AWG – як `0.255 mm`; отже, провід 30 AWG має приблизно вдвічі менший діаметр.[^nist-awg-wire-diameter]

Менший діаметр означає меншу площу поперечного перерізу. За однакового матеріалу й довжини опір такого проводу більший, бо струм проходить крізь меншу площу провідника. Це одна з причин, чому тонший дріт зазвичай сильніше нагрівається за того самого струму. Але не слід виводити конкретний допустимий струм лише з AWG: він залежить також від матеріалу жили, ізоляції, температурного класу, довжини, прокладання, охолодження та вимог застосовного стандарту.[^nist-awg-wire-diameter]

Практичне порівняння: для коротких мідних проводів однакової конструкції 22 AWG товщий за 24 AWG, а 24 AWG – товщий за 30 AWG. Для багатожильного проводу важливо з’ясувати, чи вказаний AWG стосується кожної жили чи всього кабелю; зовнішній діаметр ізоляції не є діаметром міді. Так само не можна підміняти AWG іншою системою калібрів, де напрямок нумерації може відрізнятися.[^nist-awg-wire-diameter]

**Типова помилка:** вважати, що «більший номер» означає «більший провід» або що з номера можна одразу визначити безпечний струм. Для вибору перерізу спершу встановіть матеріал і тип проводу, умови монтажу й струм навантаження, а тоді перевірте таблицю допустимого струму для цих умов. AWG допомагає ідентифікувати геометричний розмір, але сам собою не задає універсального рейтингу струму.[^nist-awg-wire-diameter]

## Sources

<!-- generated from frontmatter -->
