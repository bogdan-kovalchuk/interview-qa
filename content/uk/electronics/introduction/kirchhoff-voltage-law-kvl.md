---
id: emb-elintro-0108
title: "Що таке закон Кірхгофа для напруги (`KVL`)?"
description: "Що таке закон Кірхгофа для напруги (`KVL`)?"
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
  - source_id: aac-kvl
    title: "All About Circuits: Kirchhoff’s Voltage Law (KVL)"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-6/kirchhoffs-voltage-law-kvl/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Визначає алгебраїчну суму напруг у замкненому контурі та пояснює знаки полярності."
---

## Short answer

Закон Кірхгофа для напруг стверджує, що алгебраїчна сума напруг уздовж замкненого контуру дорівнює нулю. Під час додавання враховують знак і полярність кожної напруги. У простому послідовному колі напруга джерела дорівнює сумі падінь напруг на елементах.[^aac-kvl]

## Detailed explanation

Закон Кірхгофа для напруг (KVL) описує узгодженість різниць потенціалів уздовж будь-якого замкненого обходу схеми: якщо почати в одному вузлі, пройти шлях і повернутися до нього, сумарна зміна потенціалу має дорівнювати нулю. Напруга є різницею потенціалів між двома точками, тому під час обходу важливо не лише перелічити модулі, а й задати напрямок та знаки: перехід від мінуса до плюса джерела є підйомом, а через пасивний елемент за напрямком струму зазвичай є спадом напруги.[^aac-kvl]

Для джерела `V_s` і двох послідовних резисторів падіння напруг `V_1` та `V_2` дають рівняння `V_s - V_1 - V_2 = 0`, звідки `V_s = V_1 + V_2`. Якщо обхід почати в іншому місці або пройти у протилежному напрямку, знаки зміняться, але рівняння залишиться еквівалентним. Негативний результат для невідомої напруги не означає, що закон порушено: він означає, що реальна полярність протилежна до обраної початкової орієнтації.[^aac-kvl]

Приклад: джерело 9 V живить послідовно з’єднані резистори, на яких виміряно падіння 3 V і 6 V. Обхід через джерело від від’ємного до додатного полюса, а потім через обидва резистори назад дає `+9 V - 3 V - 6 V = 0`. Для паралельних гілок KVL так само працює: кожен окремий замкнений шлях має свою алгебраїчну суму нуль, і напруга на гілці узгоджується з напругою джерела. Типова помилка – додавати всі покази вольтметра як додатні; треба зберігати знаки, визначені полярністю щупів та напрямком обходу.[^aac-kvl]

## Sources

<!-- generated from frontmatter -->
