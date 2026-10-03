---
id: emb-elintro-0236
title: "Чим MOSFET принципово відрізняється від BJT у керуванні?"
description: "Чим MOSFET принципово відрізняється від BJT у керуванні?"
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
---

## Short answer

BJT використовує струм бази для керування струмом колектора. MOSFET керується напругою між gate і source; його ізольований затвор споживає лише малий струм витоку в сталому режимі, але потребує струму для заряджання чи розряджання під час перемикання.[^aac-semiconductors]

## Detailed explanation

MOSFET керується електричним полем, створеним напругою між gate і source, тоді як у звичній моделі BJT струм бази керує струмом колектора. У BJT струми пов’язані через напівпровідникові переходи, тож у звичайному режимі підсилення або ключа джерело керування має забезпечити базовий струм. Його потрібне значення залежить від робочого режиму й конкретного транзистора.[^aac-semiconductors]

Затвор MOSFET відділений від каналу ізоляційним шаром і поводиться приблизно як пластина конденсатора. Коли напруга gate стала, ідеальна ємність не споживає постійного струму; реальний компонент має малий leakage current, значення якого обмежує datasheet. Під час переходу між станами через затвор проходить короткий струм, бо драйвер має перемістити заряд ємності.[^aac-semiconductors]

Тому для повільного статичного керування MOSFET може мало навантажувати логічний вихід, але швидке перемикання силового транзистора все одно вимагає врахувати gate charge і спроможність драйвера. Порівнювати ці типи лише за фразами «керування струмом» і «керування напругою» недостатньо: мають значення також витік, швидкодія, межі напруги та втрати.[^aac-semiconductors]

Приклад: увімкнений BJT потребує базового струму, тоді як MOSFET зі сталою напругою gate майже не споживає постійного струму керування. Проте при кожному фронті сигналу вихід мусить зарядити або розрядити затвор.

**Типові помилки:**
- Вважати, що через gate MOSFET ніколи не тече струм.
- Вважати струм бази BJT однаковим за будь-якого навантаження та режиму.
- Ігнорувати gate charge, витік і граничні умови конкретного компонента.

## Sources

<!-- generated from frontmatter -->
