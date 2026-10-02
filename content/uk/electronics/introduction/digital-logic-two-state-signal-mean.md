---
id: emb-elintro-0016
title: Що означає "цифрова логіка – це двостановий сигнал"?
description: Що означає "цифрова логіка – це двостановий сигнал"?
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
  applicability: 'Historical question provenance: lecture 4 of the Udemy course. Original flashcards remain in imports.
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
---

## Short answer

Two-state digital logic інтерпретує сигнал як LOW або HIGH, які в positive logic зазвичай подають 0 чи 1. Ці стани – діапазони напруг, визначені input thresholds, а не обов’язково точні 0 V та supply voltage. Проміжні напруги можуть не мати гарантованої logical interpretation. [^ti-hc00]

## Detailed explanation

Binary state – інтерпретація input voltage приймачем. Реальний output для LOW може бути вище ground, а для HIGH – нижче supply, особливо під навантаженням. Важливо, щоб output levels задовольняли specified input limits приймача. Різні logic families можуть мати різні limits. [^ti-hc00]

Для TI SN74HC00 при `V_CC = 4.5 V` section 6.3 задає `V_IL(max) = 1.35 V` та `V_IH(min) = 3.15 V`. У specified input-voltage range рівень не вище 1.35 V приймається як LOW, а не нижче 3.15 V – як HIGH. Проміжок між ними не гарантований як жоден із цих станів. Числа стосуються цього device та supply condition. [^ti-hc00]

Отже, у цьому прикладі 1 V і 4 V можуть кодувати два стани, не будучи ідеальними rail voltages. Logic-level compatibility потребує порівняння transmitter output specifications із receiver input thresholds. Самої позначки живлення на кшталт 3.3 V недостатньо.

## Sources

<!-- generated from frontmatter -->
