---
id: emb-elintro-0235
title: "Що розшифровує абревіатура `MOSFET`?"
description: "Що розшифровує абревіатура `MOSFET`?"
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
  - source_id: adi-mosfet-basics
    title: "Analog Devices University: Transistors, Chapter 8"
    url: https://wiki.analog.com/university/courses/electronics/text/chapter-8
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює структуру MOSFET і ізольований oxide-шар затвора; назва розшифровується як Metal-Oxide-Semiconductor Field-Effect Transistor."
---

## Short answer

`Metal-Oxide-Semiconductor Field-Effect Transistor` – польовий транзистор із затвором, відділеним від напівпровідника ізоляційним шаром oxide. Напруга затвора керує каналом між source і drain через електричне поле; у сталому режимі ідеальний ізольований затвор не потребує постійного струму, хоча реальний затвор має ємність і струм витікає в межах специфікації компонента.[^adi-mosfet-basics]

## Detailed explanation

Абревіатура `MOSFET` означає `Metal-Oxide-Semiconductor Field-Effect Transistor`. Назва описує конструкцію та принцип дії: у класичній структурі є gate, шар ізолятора на основі oxide і semiconductor, у якому формується керований провідний канал. У сучасних компонентах матеріали gate stack можуть відрізнятися від буквального металу та діоксиду кремнію, але історична назва збереглася.[^adi-mosfet-basics]

У MOSFET керувальна напруга прикладається між затвором і витоком (`V_GS`). Електричне поле змінює концентрацію носіїв під ізолятором і таким чином впливає на провідність каналу між drain і source. Це пояснює слова «field-effect»: керувальний електрод впливає на канал полем, не будучи з’єднаним із ним провідним переходом у звичайному режимі.[^adi-mosfet-basics]

У спрощеній схемній моделі струм затвора після заряджання ємностей дуже малий. Проте затвор не є нескінченним опором у всіх режимах: під час перемикання драйвер мусить подати або забрати заряд, а перевищення максимальної напруги затвор-витік може пошкодити тонкий ізоляційний шар. Тому для швидкого перемикання важливі заряд затвора й імпеданс драйвера, а не лише твердження «струм затвора нульовий».[^adi-mosfet-basics]

**Типова помилка:** розшифрувати MOSFET правильно, але зробити висновок, що він зовсім не споживає струму керування. У сталому стані струм невеликий, однак при зміні стану затвор заряджається й розряджається. Також не плутайте порогову напругу `V_GS(th)` із напругою, за якої силовий MOSFET гарантовано має потрібний `R_DS(on)` – останню перевіряють у datasheet для фактичного режиму.[^adi-mosfet-basics]

## Sources

<!-- generated from frontmatter -->
