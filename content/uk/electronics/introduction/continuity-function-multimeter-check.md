---
id: emb-elintro-0266
title: "Що перевіряє функція continuity на мультиметрі?"
description: "Що перевіряє функція continuity на мультиметрі?"
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
    applicability: "Походження питання: лекція 24, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
    applicability: "Принцип перевірки низького опору, звуковий індикатор і вимога знеструмити та за потреби ізолювати компонент; поріг звукового сигналу залежить від моделі мультиметра."
---

## Short answer

Вона подає малий тестовий струм, оцінює опір і за достатньо низького значення подає звуковий сигнал; поріг залежить від моделі мультиметра.[^fluke-continuity-test] Перевірку виконують на знеструмленому колі, а компонент іноді потрібно від’єднати від решти кола, щоб паралельні шляхи не спотворили результат.[^fluke-continuity-test]

## Detailed explanation

Функція continuity перевіряє, чи існує між щупами провідний шлях із опором нижче порога конкретного мультиметра. Прилад подає малий тестовий струм, вимірює відгук і часто вмикає звуковий індикатор, коли опір достатньо низький; звуковий сигнал не означає, що опір дорівнює нулю.[^fluke-continuity-test]

Так можна швидко перевірити запобіжник, замкнений вимикач, провід або доріжку на обрив. Відсутність сигналу означає, що виміряний шлях відкритий або його опір перевищує поріг сигналізації, а не обов’язково доводить, що компонент зіпсований: спершу треба перевірити контакт щупів і діапазон вимірювання.[^fluke-continuity-test]

Коло має бути знеструмлене, а конденсатори – розряджені до початку перевірки. Напруга ззовні може пошкодити прилад або зробити вимірювання недійсним. Якщо деталь лишається впаяною, паралельний шлях через інші компоненти може створити сигнал навіть за розімкненого компонента, тому для однозначного результату один його вивід від’єднують.[^fluke-continuity-test]

Приклад: щоб перевірити запобіжник, вимкніть живлення, торкніться щупами двох його контактів і порівняйте звуковий сигнал із показом опору. Сигнал разом із малим опором сумісний із цілим запобіжником; нескінченний опір або `OL` вказує на розрив. Не робіть висновок про точну величину опору лише за звуком – дивіться на дисплей мультиметра.

**Типові помилки:**

- Вважати, що кожен мультиметр пищить за одного універсального значення опору.
- Перевіряти коло під напругою або не враховувати заряд конденсаторів.
- Приписувати компоненту коротке замикання, не від’єднавши його від паралельних шляхів.

## Sources

<!-- generated from frontmatter -->
