---
id: emb-elintro-0006
title: Яка функція діода?
description: Яка функція діода?
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
- source_id: vishay-diode
  title: Vishay 1N4001-1N4007 rectifier datasheet
  url: https://www.vishay.com/docs/88503/1n4001.pdf
  accessed: 2026-10-04
  kind: official
  version: null
  applicability: Cathode band, reverse-voltage ratings and temperature-dependent reverse leakage.
---

## Short answer

Rectifier diode проводить переважно від anode до cathode за forward bias та блокує більшість струму за reverse bias в межах своїх ratings. Реальні діоди мають forward voltage та reverse leakage; `V_RRM` – максимальна повторювана пікова зворотна напруга, а не поріг нульового струму. [^vishay-diode]

## Detailed explanation

Forward bias означає, що anode достатньо позитивний відносно cathode для потрібного струму. Forward current сильно нелінійно залежить від напруги; діод не є сталим резистором чи ідеальним switch. Його forward drop залежить від струму, температури й технології компонента.

Reverse bias значно зменшує провідність звичайного rectifier, але не усуває її. Datasheet Vishay 1N4001-1N4007 задає максимальний reverse leakage за rated blocking voltage: 5 µA при 25 °C та 50 µA при 125 °C. Ці rating і температура стосуються саме цієї сім’ї, а не всіх діодів. [^vishay-diode]

В ideal-diode задачі можна наближено вважати forward conduction коротким замиканням, а reverse conduction – розривом. Це наближення потрібно назвати явно. Для hardware обирайте forward-current, reverse-voltage і thermal ratings та враховуйте transient/recovery behavior. Breakdown не слід вважати штатним режимом rectifier лише тому, що деякі інші типи діодів навмисно працюють у ньому.

## Sources

<!-- generated from frontmatter -->
