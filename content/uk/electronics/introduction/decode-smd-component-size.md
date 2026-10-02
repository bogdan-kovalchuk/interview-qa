---
id: emb-elintro-0011
title: Як розшифрувати розмір `SMD`-компонента "0805"?
description: Як розшифрувати розмір `SMD`-компонента "0805"?
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
- source_id: vishay-sizes
  title: Vishay D/CRCW e3 standard thick film chip resistors
  url: https://www.vishay.com/docs/20035/dcrcwe3.pdf
  accessed: 2026-10-04
  kind: official
  version: null
  applicability: Imperial/metric package designations and nominal dimensions of 0402/0805.
---

## Short answer

Для поширених rectangular chip resistors imperial size code 0805 означає приблизно 0.08 на 0.05 inches; звичайні nominal dimensions – 2.0 на 1.25 mm, що відповідає metric 2012. Перевірте систему коду та actual package drawing, бо imperial і metric codes можна переплутати. [^vishay-sizes]

## Detailed explanation

Imperial code розділяють на length і width, кожну в hundredths of an inch. Точне перетворення 0.08 inch дає 2.032 mm, а 0.05 inch – 1.270 mm. Проте package naming номінальне: drawing Vishay для CRCW0805 задає nominal length 2.0 mm і width 1.25 mm з manufacturing tolerances. [^vishay-sizes]

Відповідний metric code 2012 позначає приблизний naming class 2.0 на 1.2 mm; він не вимагає width рівно 1.20 mm. Аналогічно imperial 0402 у цій resistor family зазвичай відповідає nominal 1.0 на 0.5 mm та metric 1005. [^vishay-sizes]

Body size сам по собі не є PCB land pattern. Pad dimensions, termination geometry, clearance та assembly recommendations беруть з відповідного drawing чи footprint specification. Розмір також не визначає однозначно resistance або power rating. При виборі компонента явно вказуйте unit system, щоб не сплутати imperial 0805 з metric designation.

## Sources

<!-- generated from frontmatter -->
