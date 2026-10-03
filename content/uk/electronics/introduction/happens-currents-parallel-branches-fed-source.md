---
id: emb-elintro-0117
title: "Що відбувається зі струмами у паралельних гілках від одного джерела?"
description: "Що відбувається зі струмами у паралельних гілках від одного джерела?"
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
    applicability: "Походження питання: лекція 12, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-parallel-branches
    title: 'All About Circuits: Resistors in Parallel'
    url: https://www.allaboutcircuits.com/technical-articles/resistors-in-parallel-circuit-analysis-with-parallel-resistance/
    accessed: '2026-10-04'
    kind: book
    version: null
    applicability: 'Пояснює однакову напругу на паралельних гілках, струми за законом Ома та суму гілкових струмів; числові приклади стосуються резистивних кіл.'
---

## Short answer

У паралельних гілках між тими самими двома вузлами однакова напруга, але струм кожної гілки залежить від її опору чи навантаження.[^aac-parallel-branches] У вузлі струм джерела дорівнює сумі струмів гілок: `I_total = I_1 + I_2 + ...`.[^aac-parallel-branches]

## Detailed explanation

У паралельному колі кожна гілка під’єднана до тієї самої пари вузлів, тому напруга на гілках однакова; струм джерела розподіляється між гілками й дорівнює їхній сумі.[^aac-parallel-branches]

Розподіл струму визначає поведінка кожного навантаження. Для резистивної гілки закон Ома дає `I = V/R`: за однакової напруги гілка з меншим опором споживає більший струм. Для нелінійного навантаження, наприклад лампи чи `LED`, просте ділення на один сталий опір не описує роботу; струм задає його вольт-амперна характеристика разом із зовнішніми компонентами.[^aac-parallel-branches]

Перший закон Кірхгофа є наслідком збереження заряду: у вузлі заряд не накопичується нескінченно, тому сума струмів, що входять, дорівнює сумі струмів, що виходять. Для джерела, яке подає струм у розгалуження, це записують як суму гілкових струмів. Знак струму залежить від обраного напрямку відліку, тому в рівнянні важливо послідовно домовитися, які струми вважаються вхідними та вихідними.[^aac-parallel-branches]

Приклад: до ідеального джерела `6 V` паралельно під’єднано резистори `1 kΩ` і `2 kΩ`. Напруга на кожному дорівнює напрузі джерела. Перший резистор проводить `6 mA`, другий – `3 mA`, отже джерело віддає `9 mA`. Реальне джерело має внутрішній опір і межу струму, тому напруга може просідати, коли сумарне навантаження зростає.[^aac-parallel-branches]

**Типова помилка:** вважати, що паралельні гілки ділять струм порівну або що струм у кожній гілці дорівнює струму джерела. Порівну він розподіляється лише за відповідних однакових характеристик гілок; загальний струм завжди знаходять як алгебраїчну суму струмів у вузлі. У практичній схемі також треба перевірити, чи здатне джерело витримати цю суму.[^aac-parallel-branches]

## Sources

<!-- generated from frontmatter -->
