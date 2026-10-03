---
id: emb-elintro-0301
title: "Що перевірити перед першим підключенням батареї до саморобної плати?"
description: "Що перевірити перед першим підключенням батареї до саморобної плати?"
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
    applicability: "Походження питання: лекція 26, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: fluke-continuity-test
    title: "Fluke: A Guide to Continuity Testing with a Multimeter"
    url: https://www.fluke.com/en-us/learn/blog/digital-multimeters/how-to-test-for-continuity
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Підтримує перевірку знеструмленого кола на цілісність з’єднань; режим continuity не визначає сам по собі правильність усієї схеми."
---

## Short answer

Перевірте полярність роз’єму й LED, правильність номіналів та наявність послідовного резистора, а також огляньте пайку. На знеструмленій платі перевірте, що між `+9V` і `GND` немає короткого замикання, а потрібні доріжки мають continuity; показ continuity сам по собі не доводить правильність усієї схеми.[^fluke-continuity-test]

## Detailed explanation

Перед підключенням батареї перевірте плату без живлення, щоб помилка монтажу не перетворилася на надмірний струм або пошкодження компонента. Спочатку звірте полярність батарейного роз’єму з позначеннями `+9V` і `GND`, а полярні компоненти, зокрема LED, – зі схемою та посадковими позначеннями. Переконайтеся, що послідовно з LED стоїть резистор потрібного номіналу, а не перемичка чи резистор в іншій гілці.[^aac-semiconductors]

Огляньте обидва боки плати: шукайте містки припою між сусідніми площадками, кульки припою, перевернуті компоненти та ненадійні механічні з’єднання. Вимірювання continuity або опору між шинами живлення робіть лише на знеструмленій платі. Показ близько нуля може свідчити про коротке, але конденсатори під час заряджання від мультиметра, напівпровідникові переходи та паралельні гілки впливають на показ; звуковий сигнал не є універсальним доказом несправності або справності. За потреби ізолюйте гілку, яку перевіряєте.[^fluke-continuity-test]

При першому ввімкненні використайте джерело з обмеженням струму або послідовний захисний резистор, якщо це доступно, і перевірте напруги в ключових вузлах. Негайно вимкніть живлення, якщо струм значно перевищує очікуваний, компонент швидко нагрівається чи з’явився запах. Такий поетапний запуск допомагає відрізнити помилку полярності, коротке замикання й неправильний монтаж; простий тест мультиметром до подачі живлення не може перевірити роботу плати під навантаженням.

## Sources

<!-- generated from frontmatter -->
