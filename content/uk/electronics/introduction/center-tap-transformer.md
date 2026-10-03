---
id: emb-elintro-0160
title: "Що таке center tap у трансформаторі?"
description: "Що таке center tap у трансформаторі?"
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
    applicability: "Походження питання: лекція 15, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: electronics-tutorials-multiple-windings
    title: "Electronics Tutorials: Multiple Winding Transformers with Multiple Coils"
    url: https://www.electronics-tutorials.ws/transformer/multiple-winding-transformers.html
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Вивід від середини вторинної обмотки, напруги двох половин і протифазність відносно center tap; рівність напруг передбачає симетричну обмотку."
---

## Short answer

`Center tap` – вивід із середини вторинної обмотки; для симетричної обмотки він дає дві рівні за модулем AC-напруги у протифазі відносно цієї точки.[^electronics-tutorials-multiple-windings] Наприклад, позначення `12-0-12 V` означає `12 V` RMS від кожного кінця до відводу та `24 V` між кінцями; це не готові DC-шини `+12 V` і `−12 V`.[^electronics-tutorials-multiple-windings]

## Detailed explanation

`Center tap` – це вивід, приєднаний до середини вторинної обмотки трансформатора. Він ділить обмотку на дві секції; якщо вони мають однакову кількість витків, напруга кожної секції відносно відводу має однаковий модуль.[^electronics-tutorials-multiple-windings]

Коли через обмотку проходить змінний магнітний потік, напруги на двох половинах мають протилежну миттєву полярність відносно center tap. Якщо середню точку зробити спільним проводом кола, кінці вторинної обмотки утворюють два AC-виходи, зсунуті за фазою на 180 градусів. Напруга між крайніми кінцями дорівнює сумі модулів напруг половин у кожний момент, а не напрузі однієї половини.[^electronics-tutorials-multiple-windings]

Наприклад, для симетричної обмотки з позначенням `12-0-12 V` кожна половина має номінально `12 V` RMS відносно відводу, а між крайніми виводами буде `24 V` RMS. Напис `12-0-12 V` описує AC-обмотку; щоб отримати стабільні DC-шини, потрібні випрямлячі та, за потреби, фільтрація і регулювання.[^electronics-tutorials-multiple-windings]

Відвід не обов’язково розташований точно посередині. Якщо число витків або навантаження половин різниться, напруги будуть несиметричними; навіть за симетричної обмотки нерівні навантаження можуть змістити потенціал середньої точки в реальній схемі.[^electronics-tutorials-multiple-windings]

**Типова помилка:** називати два кінці вторинної обмотки `+12 V` і `−12 V` без уточнення точки відліку та випрямлення. Це протифазні AC-напруги відносно center tap; полярність DC-виходів визначається вже схемою випрямлення.[^electronics-tutorials-multiple-windings]

## Sources

<!-- generated from frontmatter -->
