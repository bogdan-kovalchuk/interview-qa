---
id: emb-elintro-0033
title: "Скільки електронів міститься в 1 Кулоні?"
description: "Скільки електронів міститься в 1 Кулоні?"
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
    applicability: "Походження питання: лекція 5, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: nist-elementary-charge
    title: "NIST CODATA: elementary charge"
    url: https://physics.nist.gov/cuu/Constants/Value/e.html
    accessed: 2026-10-04
    kind: official
    version: "2022 CODATA"
    applicability: "Надає точне значення елементарного заряду; модуль заряду електрона дорівнює цьому значенню."
---

## Short answer

Приблизно `6.24 × 10¹⁸` електронів мають сумарний заряд за модулем `1 C`, оскільки модуль заряду одного електрона точно дорівнює `1.602176634 × 10⁻¹⁹ C`. За струму `1 mA` протягом `1 s` через переріз проходить приблизно `6.24 × 10¹⁵` електронів.[^nist-elementary-charge][^aac-direct-current]

## Detailed explanation

Модуль заряду електрона дорівнює елементарному заряду `e = 1.602176634 × 10⁻¹⁹ C`; це значення точне в SI. Заряд самого електрона від’ємний, `−e`, а в задачі «скільки електронів відповідають одному кулону» зазвичай питають кількість частинок для такого самого модуля заряду, а не знак сумарного заряду.[^nist-elementary-charge]

Кількість частинок знаходять діленням модуля сумарного заряду на модуль заряду одного носія: `N = |Q|/e`. Оскільки електронні заряди дискретні, результат для довільного `Q` може бути не цілим, якщо йдеться про виміряне середнє значення або округлення; для підрахунку фактичних окремих електронів кількість ціла. У практичних електричних величинах таке округлення не змінює корисної точності відповіді.[^nist-elementary-charge]

Для сталого струму діє `Q = I*t`: `1 mA` протягом `1 s` переносить `0.001 C`, що відповідає приблизно `6.24 × 10¹⁵` електронів за модулем. Це кількість заряду, яка пройшла крізь обраний поперечний переріз за цей час, а не загальна кількість електронів у дроті. За змінного струму або змінного в часі сигналу для заряду треба врахувати весь часовий перебіг струму, а не множити довільне миттєве значення на інтервал.[^nist-elementary-charge][^aac-direct-current]

## Sources

<!-- generated from frontmatter -->
