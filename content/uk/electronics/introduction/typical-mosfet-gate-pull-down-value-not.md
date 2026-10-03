---
id: emb-elintro-0261
title: "Яке типове значення pull-down резистора між gate і source N-channel MOSFET та чому не варто брати надто малий?"
description: "Яке типове значення pull-down резистора між gate і source N-channel MOSFET та чому не варто брати надто малий?"
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
  - source_id: infineon-mosfet-gate-drive
    title: "Infineon: Gate drive for power MOSFETs in switching applications"
    url: https://www.infineon.com/assets/row/public/documents/24/42/infineon-gate-drive-for-power-mosfets-in-switchtin-applications-applicationnotes-en.pdf
    accessed: 2026-10-04
    kind: official
    version: "V1.0, 2022-04-20"
    applicability: "Рекомендація RGS між gate і source у діапазоні кОм, типово 10 кОм, щоб розряджати gate при від’єднаному драйвері; не задає універсального номіналу для кожної схеми."
---

## Short answer

Для N-channel MOSFET часто починають із 10 кОм між gate і source, але це орієнтир, а не універсальна вимога.[^infineon-mosfet-gate-drive] Резистор утримує gate біля потенціалу source, коли вихід драйвера від’єднаний або має високий імпеданс, і допомагає прибрати залишковий заряд. Менший номінал сильніше задає вимкнений стан, але споживає більше струму від драйвера, коли той вмикає транзистор.[^infineon-mosfet-gate-drive]

## Detailed explanation

Pull-down резистор потрібен тому, що gate MOSFET має ємність і може залишитися зарядженим, коли керувальний вихід переходить у високий імпеданс. Для N-channel ключа резистор між gate і source задає `V_GS` близьке до нуля в такому стані; без нього наведення або витік можуть спричинити ненавмисне часткове ввімкнення. Infineon рекомендує резистор RGS у діапазоні кОм і наводить 10 кОм як типовий вибір, але потрібний номінал залежить від схеми та драйвера.[^infineon-mosfet-gate-drive]

Цей резистор не тотожний послідовному gate resistor. Послідовний резистор обмежує імпульсний струм заряджання ємності gate та впливає на швидкість перемикання; pull-down під’єднаний між gate і source і задає вимкнений стан, коли драйвер не керує лінією. Під час нормального активного вимкнення драйвер зазвичай сам стягує gate до source, тому pull-down не завжди визначає основну швидкість перемикання.[^infineon-mosfet-gate-drive]

Надто малий pull-down може навантажити GPIO або драйвер: коли вихід подає логічну одиницю, через резистор тече струм. Наприклад, при 3.3 V і 10 кОм він становить `I = V/R = 0.33 mA`; при 1 кОм це було б 3.3 mA. Це оцінка для прямого керування виходом, без урахування інших опорів. Водночас в умовах сильного наведення, великої паразитної ємності або вимог до швидкого вимкнення потрібен аналіз конкретного кола, а не механічне застосування 10 кОм.[^infineon-mosfet-gate-drive]

Приклад вибору: якщо ключ перемикає повільно і GPIO напряму керує gate, 10 кОм є обґрунтованою початковою точкою для pull-down до source. Перевірте, що pin може віддавати додатковий струм у ввімкненому стані, а `V_GS` лишається в дозволених межах. Для P-channel MOSFET у типовому вимкненому стані gate підтягують до source, тобто це pull-up відносно землі, тому назва «pull-down» не універсальна для всіх полярностей.[^infineon-mosfet-gate-drive]

## Sources

<!-- generated from frontmatter -->
