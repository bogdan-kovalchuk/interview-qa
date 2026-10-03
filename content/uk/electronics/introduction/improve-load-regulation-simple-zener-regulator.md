---
id: emb-elintro-0191
title: "Як покращити load regulation простого Зенер-стабілізатора?"
description: "Як покращити load regulation простого Зенер-стабілізатора?"
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
    applicability: "Походження питання: лекція 18, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-common-collector
    title: "All About Circuits: The Common-collector Amplifier"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/common-collector-amplifier/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює emitter follower, струмове підсилення та обмеження режимом транзистора; β залежить від транзистора й робочої точки."
---

## Short answer

Додати `NPN`-транзистор як emitter follower: базу під’єднати до вузла Зенера, колектор – до `V_in`, емітер – до навантаження. Зенер тоді задає напругу бази, а навантаження отримує більший струм від колектора; струм бази приблизно дорівнює струму навантаження, поділеному на β + 1. Це зменшує вплив зміни навантаження на струм Зенера, але результат обмежений β, запасом напруги та потужністю транзистора.[^aac-common-collector]

## Detailed explanation

Emitter follower на `NPN`-транзисторі може покращити load regulation простого стабілізатора Зенера, бо відокремлює навантаження від вузла, який формує опорну напругу. У базовій схемі струм через послідовний резистор ділиться між Зенером і навантаженням. Коли навантаження змінюється, його струм безпосередньо змінює доступний струм Зенера, а отже й стабільність напруги.[^aac-semiconductors]

У follower база під’єднана до стабілізованого вузла, колектор – до джерела живлення, а навантаження – до емітера. Емітерна напруга слідує за базовою з різницею приблизно `V_BE`; струм навантаження забезпечує транзистор, тоді як Зенер має віддавати переважно струм бази. У спрощеній моделі `I_E ≈ (β + 1)*I_B`, тому вимоги до струму Зенера можуть суттєво зменшитися. Реальний β змінюється між екземплярами й залежить від струму та температури, тож у розрахунку треба брати гарантоване мінімальне значення з datasheet, а не очікуване типове.[^aac-common-collector]

Цей каскад не є ідеальним стабілізатором: він не підвищує напругу, а емітер не може досягти напруги колектора без потрібного запасу для транзистора. Треба перевірити мінімальну вхідну напругу, максимальний струм і розсіювану потужність транзистора, а також залишковий струм Зенера за найгіршого навантаження. Якщо джерело просідає або транзистор входить у насичення, вихідна напруга перестає слідувати заданій.[^aac-common-collector] [^aac-semiconductors]

Приклад: якщо навантаженню потрібно `100 mA`, а для оцінки взяти β = 100, струм бази становитиме приблизно `100 mA/101 ≈ 0.99 mA`. Це приблизна оцінка для робочої точки, а не універсальна гарантія: при меншому β базовий струм і навантаження на Зенер зростуть.

**Типова помилка:** вважати, що транзистор сам підвищує напругу або що коефіцієнт β завжди дорівнює 200. Він дає струмове підсилення лише в допустимій області роботи, а для перевірки потрібні параметри конкретного транзистора та теплові умови.[^aac-common-collector]

## Sources

<!-- generated from frontmatter -->
