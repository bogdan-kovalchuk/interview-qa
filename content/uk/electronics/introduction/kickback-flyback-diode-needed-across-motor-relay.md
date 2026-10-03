---
id: emb-elintro-0231
title: "Навіщо потрібен kickback/flyback-діод паралельно мотору або реле?"
description: "Навіщо потрібен kickback/flyback-діод паралельно мотору або реле?"
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
    applicability: "Походження питання: лекція 21, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: ti-inductive-load-clamping
    title: "TI: Switching Inductive Loads with DRV89xx-Q1 Devices"
    url: https://www.ti.com/document-viewer/lit/html/slvaf04
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює викиди напруги під час вимкнення індуктивного навантаження, розсіювання магнітної енергії та компроміс між рівнем clamp і часом спаду струму."
---

## Short answer

Індуктивність протидіє швидкій зміні струму: при вимиканні струм котушки не зникає миттєво, а створює перенапругу, здатну пошкодити ключ. Flyback-діод дає струму шлях циркуляції та обмежує напругу на ключі. Його номінали й схема мають відповідати струму навантаження та допустимій напрузі ключа.[^ti-inductive-load-clamping]

## Detailed explanation

Flyback-діод захищає транзистор або інший ключ від перехідної напруги, що виникає під час вимкнення мотора чи реле. Обмотка є індуктивністю: доки через неї тече струм, у її магнітному полі зберігається енергія, а індуктивність чинить опір швидкій зміні струму. Якщо ключ розриває єдиний шлях, котушка піднімає свою напругу настільки, наскільки потрібно, щоб струм продовжився; у реальному колі межу задають пробій ключа, паразитні ємності та інші захисні елементи.[^ti-inductive-load-clamping]

Діод підключають паралельно котушці й орієнтують так, щоб у нормальному режимі він був закритий. Після вимкнення полярність напруги на котушці змінюється, діод відкривається, і струм проходить замкненим контуром «котушка – діод». Енергія поступово перетворюється на тепло в опорі обмотки та діода, тож напруга на ключі обмежується приблизно рівнем живлення плюс пряме падіння діода для типового low-side кола. Точний перехідний режим залежить від схеми драйвера та вибраного clamp.[^ti-inductive-load-clamping]

Звичайний діод дає невисокий рівень clamp і зазвичай уповільнює спад струму. Для реле це може затримати відпускання контактів; для моторного приводу потрібне рішення, сумісне з режимом перемикання та швидкістю гальмування. TVS або інший clamp з вищою напругою швидше гасить струм, але ключ має витримувати відповідну напругу. Діод також треба вибрати за піковим струмом котушки, зворотною напругою та тепловим режимом, а не лише за середнім струмом живлення.[^ti-inductive-load-clamping]

**Типова помилка:** встановити діод послідовно з мотором або розвернути його так, що він проводить під час нормальної роботи. Перевірте полярність у вимкненому стані ключа й переконайтеся, що захист не створює короткого замикання джерела.

## Sources

<!-- generated from frontmatter -->
