---
id: emb-elintro-0252
title: "Навіщо MOSFET потрібен pull-down резистор на gate?"
description: "Навіщо MOSFET потрібен pull-down резистор на gate?"
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
  - source_id: infineon-gate-drive
    title: "Infineon: Gate drive for power MOSFETs in switching applications"
    url: https://www.infineon.com/assets/row/public/documents/24/42/infineon-gate-drive-for-power-mosfets-in-switchtin-applications-applicationnotes-en.pdf
    accessed: 2026-10-04
    kind: official
    version: "V1.0, 2022-04-20"
    applicability: "Описує weak pull-down між gate і source для стану вимкненого драйвера; вибір опору залежить від схеми та витоків."
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 23, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
---

## Short answer

Gate ємнісно зберігає заряд, тож коли вихід керування від’єднаний, напруга може стати невизначеною. Резистор між gate і source задає `V_GS ≈ 0` для вимкненого N-channel MOSFET і відводить заряд, зменшуючи ризик випадкового часткового відкриття. Його опір добирають з урахуванням струму витоку та швидкості вимкнення, а не за універсальним номіналом.[^infineon-gate-drive]

## Detailed explanation

Gate MOSFET відділений від каналу ізоляційним шаром і електрично поводиться значною мірою як ємнісне навантаження. Коли GPIO перебуває у high-impedance стані під час reset, запуску або від’єднання, він не задає надійного логічного рівня. Заряд, наведення або струми витоку можуть змінити `V_GS`, тому MOSFET здатен частково відкритися й неочікувано живити навантаження.[^infineon-gate-drive]

Pull-down під’єднують між gate і source N-channel ключа. Він створює визначений стан вимкнення, стягує залишковий заряд gate та дає струмам витоку шлях до source. Для низькобічного ключа з source на землі це зазвичай означає також зв’язок gate із `GND`; для інших топологій важливе саме напруження gate відносно source, а не відносно довільної землі. Виробники драйверів застосовують слабке стягування gate до source, коли вихід драйвера вимкнений.[^infineon-gate-drive]

Номінал резистора є компромісом. Менший опір надійніше утримує gate вимкненим і швидше розряджає його, але збільшує струм, який має віддавати керувальний вихід у ввімкненому стані. Більший опір зменшує цей струм, проте слабше протидіє витокам і наведенням та повільніше розряджає gate. Тому значення на кшталт 10 kΩ може бути лише початковим вибором: перевірте вихідні рівні контролера, витоки за температури й потрібну поведінку при reset.[^infineon-gate-drive]

Приклад: якщо контролер запускається з входом у high-impedance, зовнішній pull-down тримає `V_GS` близько нуля до того, як firmware налаштує pin як output. Для P-channel ключа напрямок логічної дії відрізняється, і потрібен pull-up gate до source, аби забезпечити `V_GS ≈ 0` у вимкненому стані. Не під’єднуйте резистор до source, якщо потрібний стан визначається відносно іншого вузла.[^infineon-gate-drive]

## Sources

<!-- generated from frontmatter -->
