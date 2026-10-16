---
id: emb-elintro-0252
title: "Навіщо MOSFET потрібен pull-down резистор на gate?"
track: electronics
section: introduction
sources:
  - source_id: infineon-gate-drive
    title: "Infineon: Gate drive for power MOSFETs in switching applications"
    url: https://www.infineon.com/assets/row/public/documents/24/42/infineon-gate-drive-for-power-mosfets-in-switchtin-applications-applicationnotes-en.pdf
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Gate ємнісно зберігає заряд, тож коли вихід керування від’єднаний, напруга може стати невизначеною. Резистор між gate і source задає `V_GS ≈ 0` для вимкненого N-channel MOSFET і відводить заряд, зменшуючи ризик випадкового часткового відкриття. Його опір добирають з урахуванням струму витоку та швидкості вимкнення, а не за універсальним номіналом.[^infineon-gate-drive]

## Detailed explanation

Gate MOSFET відділений від каналу ізоляційним шаром і електрично поводиться значною мірою як ємнісне навантаження. Коли GPIO перебуває у high-impedance стані під час reset, запуску або від’єднання, він не задає надійного логічного рівня. Заряд, наведення або струми витоку можуть змінити `V_GS`, тому MOSFET здатен частково відкритися й неочікувано живити навантаження.[^infineon-gate-drive]

Pull-down під’єднують між gate і source N-channel ключа. Він створює визначений стан вимкнення, стягує залишковий заряд gate та дає струмам витоку шлях до source. Для низькобічного ключа з source на землі це зазвичай означає також зв’язок gate із `GND`; для інших топологій важливе саме напруження gate відносно source, а не відносно довільної землі. Виробники драйверів застосовують слабке стягування gate до source, коли вихід драйвера вимкнений.[^infineon-gate-drive]

Номінал резистора є компромісом. Менший опір надійніше утримує gate вимкненим і швидше розряджає його, але збільшує струм, який має віддавати керувальний вихід у ввімкненому стані. Більший опір зменшує цей струм, проте слабше протидіє витокам і наведенням та повільніше розряджає gate. Тому значення на кшталт 10 kΩ може бути лише початковим вибором: перевірте вихідні рівні контролера, витоки за температури й потрібну поведінку при reset.[^infineon-gate-drive]

Приклад: якщо контролер запускається з входом у high-impedance, зовнішній pull-down тримає `V_GS` близько нуля до того, як firmware налаштує pin як output. Для P-channel ключа напрямок логічної дії відрізняється, і потрібен pull-up gate до source, аби забезпечити `V_GS ≈ 0` у вимкненому стані. Не під’єднуйте резистор до source, якщо потрібний стан визначається відносно іншого вузла.[^infineon-gate-drive]
