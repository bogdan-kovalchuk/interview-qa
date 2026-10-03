---
id: emb-elintro-0202
title: "Умова активного режиму для `NPN`-транзистора?"
description: "Умова активного режиму для `NPN`-транзистора?"
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
    applicability: "Походження питання: лекція 19, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-bjt-junctions
    title: "Bipolar Junction Transistors, All About Circuits"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/bipolar-junction-transistors/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює зміщення переходів NPN та інжекцію носіїв у прямому активному режимі; приблизна напруга переходу залежить від компонента й струму."
---

## Short answer

Для NPN у прямому активному режимі перехід база–емітер прямо зміщений, а база–колектор – зворотно; за звичайної схеми це відповідає `V_C > V_B > V_E`. Для кремнієвого транзистора `V_BE` часто близько 0.6–0.7 V, але це не стала універсальна напруга.[^aac-bjt-junctions]

## Detailed explanation

Прямий активний режим NPN означає, що перехід база–емітер прямо зміщений, а перехід база–колектор зворотно зміщений. Якщо позначити напруги вузлів відносно спільної точки, типовий порядок буде `V_C > V_B > V_E`; важливо саме зміщення кожного переходу, а не абсолютна напруга відносно землі.[^aac-bjt-junctions]

Пряме зміщення емітерного переходу вводить електрони з N-емітера в тонку P-базу. Невелика частина носіїв рекомбінує в базі, формуючи базовий струм; більшість доходить до збідненої області колекторного переходу й електричним полем переноситься до колектора. Тому малий базовий сигнал може керувати значно більшим струмом колектора. У спрощеній схемній моделі пишуть `I_C ≈ β*I_B`, але β не є точною сталою й змінюється залежно від екземпляра та умов роботи.[^aac-bjt-junctions]

Для кремнієвого транзистора `V_BE` часто має значення порядку 0.6–0.7 V у типових режимах, але його фактичне значення залежить від струму, температури й конкретної моделі. Тому активний режим не визначають перевіркою «рівно 0.7 V»: слід також переконатися, що колекторний перехід не перейшов у пряме зміщення. Якщо він прямо зміщений, транзистор наближається до saturation, і лінійна модель підсилення перестає описувати струм.[^aac-bjt-junctions]

**Приклад перевірки:** якщо емітер під’єднаний до 0 V, база приблизно до 0.65 V, а колектор утримується на 3 V, обидві нерівності виконуються і полярності відповідають прямому активному режиму. Це лише перевірка узгодженості; реальні напруги залежать від кола зміщення та навантаження.[^aac-bjt-junctions]

**Типова помилка:** вважати 0.7 V достатньою умовою незалежно від колектора. Перевіряйте обидва переходи відносно їхніх виводів і враховуйте, що граничний режим залежить від схеми та характеристик транзистора.

## Sources

<!-- generated from frontmatter -->
