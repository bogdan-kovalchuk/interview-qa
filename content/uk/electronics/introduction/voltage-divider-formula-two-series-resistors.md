---
id: emb-elintro-0109
title: "Формула подільника напруги для двох послідовних резисторів?"
description: "Формула подільника напруги для двох послідовних резисторів?"
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
    applicability: "Походження питання: лекція 11, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-voltage-divider
    title: "All About Circuits: Voltage Dividers: What They Are and What They Do"
    url: https://www.allaboutcircuits.com/technical-articles/voltage-and-current-dividers-what-they-are-and-what-they-do/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює формулу подільника як поділ напруги пропорційно опорам; базова формула стосується незавантаженого подільника."
---

## Short answer

Для `R1` між `V_in` і виходом, а `R2` між виходом і спільним проводом, незавантажена напруга дорівнює `V_out = V_in*R2/(R1 + R2)`. Формула випливає з того, що в послідовному колі струм однаковий, а напруга на кожному резисторі пропорційна його опору. Підключене навантаження змінює результат, якщо його опір не набагато більший за `R2`.[^aac-voltage-divider]

## Detailed explanation

Подільник напруги з двох послідовних резисторів створює на середньому вузлі частину вхідної напруги. Якщо `R1` стоїть між входом і виходом, а `R2` – між виходом і спільним проводом, через обидва резистори протікає однаковий струм. За законом Ома загальний струм дорівнює `V_in/(R1 + R2)`, а напруга на нижньому резисторі є добутком цього струму на `R2`. Звідси отримуємо `V_out = V_in*R2/(R1 + R2)`. Ця формула передбачає, що вихід нічим не навантажений, крім самого `R2`.[^aac-voltage-divider]

Приклад: для `V_in = 9 V`, `R1 = 3 kΩ` і `R2 = 6 kΩ` струм дорівнює `9 V/(3 kΩ + 6 kΩ) = 1 mA`, тому вихід становить `1 mA*6 kΩ = 6 V`. Резистори можна поміняти місцями, але тоді вихід береться з іншого вузла і частка напруги змінюється. Формула також не є регулятором напруги: вихід залежить від вхідної напруги та номіналів резисторів.[^aac-voltage-divider]

Якщо під’єднати споживач між виходом і спільним проводом, він з’єднається паралельно з `R2`; для розрахунку замість `R2` використовують еквівалентний опір `R2` паралельно навантаженню. Малий опір навантаження зменшує цей еквівалент і знижує вихідну напругу. Типова помилка – застосувати формулу незавантаженого подільника до схеми з під’єднаним споживачем або вважати подільник здатним віддавати великий струм без зміни напруги. Для значного навантаження зазвичай потрібен буфер або стабілізатор, а не лише пара резисторів.[^aac-voltage-divider]

## Sources

<!-- generated from frontmatter -->
