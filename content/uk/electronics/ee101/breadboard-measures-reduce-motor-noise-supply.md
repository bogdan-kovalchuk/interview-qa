---
id: emb-elee-0185
title: "Які заходи на макеті зменшують завади від двигуна в живленні?"
description: "Які заходи на макеті зменшують завади від двигуна в живленні?"
track: electronics
section: ee101
level: junior
type: concept
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Походження питання: лекція 66, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: ti-slva959b-motor-driver-layout
    title: "TI: Best Practices for Board Layout of Motor Drivers (SLVA959B)"
    url: https://www.ti.com/lit/an/slva959b/slva959b.pdf
    accessed: 2026-10-13
    kind: official
    version: "SLVA959B, revised October 2021"
    applicability: "Рекомендації TI з розводки плати для драйверів двигунів: bulk-конденсатори біля входу живлення, блокувальні конденсатори якомога ближче до виводів, мала петля сильного струму, одноточкове розведення живлення й спільний імпеданс землі. Правила для друкованої плати з драйвером, не для макета."
  - source_id: ti-slvaft0-bulk-capacitor-sizing
    title: "TI: Bulk Capacitor Sizing for DC Motor Drive Applications (SLVAFT0)"
    url: https://www.ti.com/lit/an/slvaft0/slvaft0.pdf
    accessed: 2026-10-13
    kind: official
    version: "SLVAFT0, July 2024"
    applicability: "Bulk-конденсатор як резервуар заряду для стрибків струму двигуна та формула C > ΔI·T_PWM/ΔV з прикладом 200 мА, 50 мкс і 100 мВ (100 мкФ). Ідеалізована оцінка без ESR; для конкретного драйвера й плати потрібна перевірка."
---

## Short answer

Основні заходи: накопичувальна ємність (bulk) для низькочастотних стрибків струму двигуна, локальна кераміка біля мікросхем, короткі силові петлі й окремий зворотний шлях струму двигуна, дрібна кераміка біля силових ключів (power stage).[^ti-slva959b-motor-driver-layout] Окремий шлях зменшує зміну потенціалу спільного проводу чутливих каскадів.[^ti-slva959b-motor-driver-layout]

## Detailed explanation

Двигун забирає від джерела живлення великий струм стрибками при кожному перемиканні ШІМ. Провідники мають індуктивність, тож швидка зміна струму дає стрибок напруги на виводах живлення, який потрапляє в сусідні каскади. Заходи працюють на різних масштабах часу: низькочастотні стрибки гасить bulk-конденсатор, швидкі фронти – кераміка.

Bulk-конденсатор стоїть біля входу живлення плати й віддає великі струми драйверу під час перемикання. За TI, такі конденсатори зазвичай понад 10 мкФ і мають малий ESR.[^ti-slva959b-motor-driver-layout] Розмір можна оцінити за формулою C > ΔI·T_PWM/ΔV: при ΔI = 200 мА, T_PWM = 50 мкс і ΔV = 0,1 В маємо C ≥ 0,2 А · 50 мкс / 0,1 В = 100 мкФ. Це ідеалізована оцінка без ESR, тож реальну ємність беруть із запасом.[^ti-slvaft0-bulk-capacitor-sizing]

Кераміка для швидких фронтів стоїть якомога ближче до виводів: TI радить відстань менше 0,5 см і без перехідних отворів між конденсатором і виводом. Менший конденсатор ставлять ближче, ніж більший. Індуктивність доріжки на високих частотах дає дзвін (ringing) напруги на виводі живлення, а він стає джерелом EMI.[^ti-slva959b-motor-driver-layout] На макеті та сама причина: довгі перемички теж мають індуктивність.

Петля сильного струму йде від плюса живлення через верхній ключ, обмотку двигуна і нижній ключ назад до мінуса. При перемиканні її індуктивність дає викиди напруги, тож доріжки мають бути короткими й широкими.[^ti-slva959b-motor-driver-layout] Повернення струму двигуна має йти окремим шляхом: спільний імпеданс землі створює падіння напруги, яке чутливі каскади бачать як синфазну заваду (ground bounce). Одноточкове розведення живлення дає кожному споживачу власний шлях до джерела.[^ti-slva959b-motor-driver-layout] Для силового каскаду TI радить дрібну керамічну ємність, яка гасить високочастотні струми від перемикання MOSFET-ів.[^ti-slva959b-motor-driver-layout]

**Типові помилки:**
- Вважати, що одна велика електролітична ємність замінює кераміку біля мікросхеми: bulk-конденсатор працює з низькочастотними стрибками, а швидкі фронти потребують короткого з’єднання з керамікою.[^ti-slva959b-motor-driver-layout]
- Вести живлення двигуна тією самою доріжкою, що й сигнали логіки: спільний імпеданс переносить завади у чутливі входи.[^ti-slva959b-motor-driver-layout]
- Ставити конденсатор на довгій перемичці або через перехідний отвір: він малоефективний на високих частотах.[^ti-slva959b-motor-driver-layout]

## Sources

<!-- generated from frontmatter -->
