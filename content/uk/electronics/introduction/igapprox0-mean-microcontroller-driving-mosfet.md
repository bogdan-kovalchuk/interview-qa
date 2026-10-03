---
id: emb-elintro-0248
title: "Що означає `I_G ≈ 0` для мікроконтролера, який керує MOSFET?"
description: "Що означає IG приблизно 0 для мікроконтролера, який керує MOSFET?"
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
    applicability: "Походження питання: лекція 22, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: infineon-gate-driver-working-principle
    title: "Infineon: How Does a Gate Driver Work?"
    url: https://www.infineon.com/product-information/how-does-a-gate-driver-work
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює заряджання gate, параметри gate charge та вплив струму драйвера на час перемикання; конкретні значення залежать від MOSFET і режиму."
---

## Short answer

Струм gate переважно потрібен короткочасно, щоб зарядити або розрядити його ємності.[^infineon-gate-driver-working-principle] Середній струм керування зростає зі збільшенням gate charge та частоти перемикання.[^infineon-gate-driver-working-principle]

## Detailed explanation

Gate MOSFET відокремлений від каналу ізоляційним шаром, тому в усталеному режимі ідеальної моделі не потрібен безперервний струм для підтримання стану. Реальний компонент має витік, а його вхід також містить паразитні ємності, тож твердження `I_G ≈ 0` є наближенням, а не обіцянкою нульового струму в усіх умовах. У datasheet зазвичай наводять leakage та gate charge окремими параметрами.[^infineon-gate-driver-working-principle]

Під час перемикання вихід мікроконтролера подає або відводить заряд. Час зміни стану залежить від сумарного заряду gate та доступного пікового струму: груба оцінка – `t ≈ Q_g/I_g`. Наприклад, при `Q_g = 20 nC` і середньому струмі `10 mA` ця оцінка дає близько `2 µs`; реальна форма сигналу, Miller plateau, напруга живлення й вихідний опір змінюють результат. Повторне заряджання на кожному циклі створює середнє навантаження на живлення, навіть якщо статичний струм малий.[^infineon-gate-driver-working-principle]

Чи вистачить GPIO, визначають не лише за піковим струмом у таблиці MCU. Перевірте граничний струм виводу, рівень `V_GS`, потрібну швидкість перемикання, gate charge конкретного MOSFET і втрати в перехідному режимі. Gate driver може джерелити та стікати більший струм, щоб зменшити час перемикання; для повільного реле чи LED та сама затримка може бути прийнятною, а для високої частоти – спричинити надмірний нагрів.[^infineon-gate-driver-working-principle]

**Типова помилка:** вважати, що майже нульовий DC струм означає, що gate можна перемикати миттєво або без навантаження на GPIO. Оцінюйте заряд за умовами застосування та перевіряйте, чи забезпечує керувальна напруга достатнє відкриття каналу.

Приклад: якщо MOSFET має `Q_g = 20 nC` і перемикається `10 kHz`, на кожен цикл треба подати заряд; простий добуток `Q_g*f = 200 µA` оцінює середню складову заряду на одному фронті, але не піковий струм і не повну потужність драйвера. Враховуйте обидва фронти та реальний профіль керування.[^infineon-gate-driver-working-principle]

## Sources

<!-- generated from frontmatter -->
