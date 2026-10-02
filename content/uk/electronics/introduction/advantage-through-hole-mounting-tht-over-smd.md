---
id: emb-elintro-0013
title: Яка перевага вивідного монтажу (`THT`) над `SMD`?
description: Яка перевага вивідного монтажу (`THT`) над `SMD`?
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
- source_id: ti-hc00
  title: TI SN74HC00 quadruple NAND gates datasheet
  url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
  accessed: 2026-10-04
  kind: official
  version: SCLS181H
  applicability: Section 6.3 input thresholds; switching characteristics and PDIP/SOIC package drawings.
- source_id: vishay-sizes
  title: Vishay D/CRCW e3 standard thick film chip resistors
  url: https://www.vishay.com/docs/20035/dcrcwe3.pdf
  accessed: 2026-10-04
  kind: official
  version: null
  applicability: Imperial/metric package designations and nominal dimensions of 0402/0805.
---

## Short answer

Through-hole mounting використовує виводи, вставлені в отвори PCB, і може бути зручним для hand assembly, prototyping та деяких механічно навантажених з’єднань. Переваги залежать від компонента й конструкції; він не універсально міцніший за будь-яке SMD рішення. Більший lead pitch може полегшувати ручну роботу. [^ti-hc00]

## Detailed explanation

THT leads проходять через отвори; surface-mount terminations кріпляться до pads на поверхні плати. Практична перевага багатьох through-hole parts – фізичний доступ: виводи можна окремо тримати, згинати й паяти. Це залежна від конструкції причина вибору компонента, а не доказ універсальної mechanical superiority.

Для конкретного порівняння geometry datasheet TI SN74HC00 має PDIP package з lead pitch 2.54 mm та SOIC package з pitch 1.27 mm. Більший pitch може полегшити hand wiring. Невеликі SMD chip resistors ще компактніші: imperial 0402 Vishay має nominal body 1.0 на 0.5 mm. Це конкретні приклади, а не розміри всіх THT чи всіх SMD components. [^ti-hc00] [^vishay-sizes]

Для connector, який часто підключатимуть, оцінюйте весь load path: body support, mounting hardware, solder joints і конструкцію PCB. Through-hole lead може допомагати утримувати конкретний part, а належно підтриманий SMD connector теж може бути міцним. SMD корисний, коли важливі board area й automated assembly; вибір визначають фактичні design requirements.

## Sources

<!-- generated from frontmatter -->
