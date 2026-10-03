---
id: emb-elintro-0223
title: "Чому LED у колекторній гілці світиться, коли транзистор вимкнений?"
description: "Чому LED у колекторній гілці світиться, коли транзистор вимкнений?"
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
  - source_id: aac-bjt-switch
    title: "All About Circuits: The Bipolar Junction Transistor (BJT) as a Switch"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/transistor-switch-bjt/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтверджує режими cutoff і насичення ключа; висновок про LED справджується лише для описаного шляху струму."
---

## Short answer

Якщо резистор і LED утворюють окремий замкнений шлях від `+V` до `GND`, струм цього шляху не проходить через транзистор, тому LED може світитися в стані `cutoff`. Це залежить від з’єднань конкретної схеми.[^aac-bjt-switch]

## Detailed explanation

LED світиться лише тоді, коли через неї тече прямий струм. У схемі, де її гілка проходить від додатного живлення через обмежувальний резистор і LED до `GND`, цей шлях замкнений незалежно від стану NPN-транзистора, якщо гілка справді не проходить через транзистор. Тому вимкнений транзистор не обов’язково вимикає LED.[^aac-bjt-switch]

Це відрізняється від типового низькобічного ключа, де навантаження стоїть між `V_CC` і колектором, а транзистор замикає шлях до землі. Там у `cutoff` колекторний струм практично відсутній, тож навантаження вимкнене. Визначайте стан LED за повним замкненим шляхом струму, а не лише за тим, що LED названо «колекторною».[^aac-bjt-switch]

**Приклад:** у гілці від `+V` через резистор і LED до `GND` відкритий або знятий NPN не перериває струм, бо жоден із цих елементів не є частиною колекторно-емітерного шляху. Якщо ж LED включено послідовно з колектором, результат інший і треба аналізувати саме ту топологію.[^aac-bjt-switch]

**Типова помилка:** припускати, що будь-який LED біля колектора вимикається разом із транзистором. Простежте струм від джерела до повернення, перевірте полярність LED і наявність резистора, що обмежує струм.[^aac-bjt-switch]

## Sources

<!-- generated from frontmatter -->
