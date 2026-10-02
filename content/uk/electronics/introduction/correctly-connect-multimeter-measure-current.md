---
id: emb-elintro-0014
title: Як правильно підключити мультиметр для вимірювання струму?
description: Як правильно підключити мультиметр для вимірювання струму?
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
- source_id: fluke-meter
  title: Fluke 3000 FC Users Manual
  url: https://media.fluke.com/437e18a0-de4d-4090-ab8a-b0df016de4fd_original%20file.pdf
  accessed: 2026-10-04
  kind: official
  version: null
  applicability: Functions, terminals and power-off/series/current-measurement procedure, printed page 17.
---

## Short answer

Вимкніть живлення кола, виберіть правильні current function, rated input jack і range, потім розімкніть гілку та ввімкніть meter послідовно. Відновлюйте живлення лише після підключення; перед від’єднанням знову його вимкніть. Ніколи не підключайте meter у current mode безпосередньо паралельно voltage source. [^fluke-meter]

## Detailed explanation

Current measurement пропускає струм гілки через внутрішній current-measurement path мультиметра. Тому meter потрібно ввімкнути послідовно саме в гілку, яку вимірюють. Натомість voltage measurement підключає high-impedance input між двома вузлами. Плутанина цих підключень може замкнути source через current input. [^fluke-meter]

Процедура Fluke явно вимагає вимкнути живлення, розімкнути коло, підключити послідовно й потім відновити живлення. Оберіть AC чи DC за потребою та function, terminal і range з rating для очікуваного струму. Не припускайте, що кожен meter має input 10 A: згаданий 3000 FC має specified mA measurement ranges. Межі визначає manual фактичного meter. [^fluke-meter]

Вставлений meter може змінити коло через burden voltage; виміряний струм не обов’язково точно дорівнює початковому струму без приладу. Після вимірювання вимкніть живлення перед відновленням кола та поверніть lead у voltage/resistance jack для цих функцій. Перед наступним вимірюванням перевірте wiring та input rating.

## Sources

<!-- generated from frontmatter -->
