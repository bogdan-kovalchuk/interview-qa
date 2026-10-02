---
id: emb-elintro-0080
title: "Які номінальні напруга і частота низьковольтної мережі в Україні?"
description: "Які номінальні напруга і частота низьковольтної мережі в Україні?"
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
  - source_id: nerc-voltage-quality
    title: "НКРЕКП: Якість електричної енергії"
    url: https://www.nerc.gov.ua/sferi-diyalnosti/elektroenergiya/yakist-elektropostachannya/yakist-elektrichnoyi-energiyi
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Вказує номінальну напругу низьковольтних мереж України 230 В та частоту 50 Гц із допустимими відхиленнями; не є довідкою про кожну країну Європи."
  - source_id: aac-ac-magnitude
    title: "All About Circuits: Measurements of AC Magnitude"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-1/measurements-ac-magnitude
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює RMS і розрахунок пікових значень для синусоїди; коефіцієнти стосуються чистої синусоїди."
---

## Short answer

Номінальні параметри низьковольтної мережі України – 230 V `RMS` і 50 Hz; фактична напруга коливається в допустимих межах. Для синусоїди пік становив би близько `325 V`, але це розрахункова амплітуда, а не номінал мережі.[^nerc-voltage-quality] [^aac-ac-magnitude]

## Detailed explanation

Для низьковольтної мережі України номінальна напруга становить `230 V RMS`, а номінальна частота – `50 Hz`. Номінал не означає, що миттєва напруга весь час дорівнює 230 V: для синусоїди вона змінюється протягом кожного циклу, а діюче значення має нормативний допуск.[^nerc-voltage-quality]

НКРЕКП наводить `230 V` між фазним і нульовим проводом у трифазній чотирипровідній низьковольтній мережі та `50 Hz` як номінальну частоту. Для синхронно приєднаних до ОЕС України систем указано діапазони частотної якості: відхилення ±1% протягом 99.5% року, а також ширші межі для всього часу. Це критерії якості постачання, а не обіцянка абсолютно сталої частоти кожної миті.[^nerc-voltage-quality]

Те саме джерело вимагає, щоб 95% десятихвилинних середньоквадратичних значень напруги за тиждень були в межах ±10% від 230 V, тобто 207–253 V. Цей діапазон допомагає зрозуміти, чому виміряна напруга може відрізнятися від номіналу, не означаючи автоматично порушення критерію.[^nerc-voltage-quality]

Для ідеальної синусоїди `230 V RMS` відповідає піку `230*√2 ≈ 325 V` та peak-to-peak близько `650 V`. Це геометрія чистої синусоїди; реальна форма може бути спотворена, а результат вимірювання залежить від приладу. Частота `50 Hz` означає 50 повних циклів за секунду.[^aac-ac-magnitude] [^nerc-voltage-quality]

**Приклад:** для навантаження, розрахованого на стандартну мережу, орієнтуються на RMS-напругу й паспортний діапазон пристрою. Пікова напруга важлива для ізоляції та компонентів, але її не слід підміняти номінальним значенням мережі.[^nerc-voltage-quality] [^aac-ac-magnitude]

**Типова помилка:** подавати 325 V як «напругу розетки» або поширювати параметри України на всю Європу без перевірки національного стандарту. Розділяйте RMS-номінал, розрахунковий пік і допустимі відхилення; твердження тут стосується саме України.[^nerc-voltage-quality] [^aac-ac-magnitude]

## Sources

<!-- generated from frontmatter -->
