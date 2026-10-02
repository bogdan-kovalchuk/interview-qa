---
id: emb-elintro-0055
title: "Що таке мА·год і що вона означає?"
description: "Що таке мА·год і що вона означає?"
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
    applicability: "Походження питання: лекція 7, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: analog-ampere-hour
    title: "Analog Devices: Ampere-hour"
    url: https://www.analog.com/en/resources/glossary/amp-hour-ampere-ah-mah.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Визначає Ah і mAh як заряд, пов'язаний із добутком струму на час; наведені приклади не гарантують фактичний час роботи конкретної батареї."
  - source_id: doe-battery-capacity-rate
    title: "U.S. Department of Energy: Primer on Lead-Acid Storage Batteries"
    url: https://www.energy.gov/documents/doe-hdbk-1084-95
    accessed: 2026-10-04
    kind: official
    version: "DOE-HDBK-1084-95"
    applicability: "Пояснює, що номінальна ємність задається для умов і швидкості розряду та змінюється зі струмом; кількісні приклади документа стосуються свинцево-кислотних батарей."
---

## Short answer

мА·год (mAh) – одиниця електричного заряду, яку використовують для позначення ємності батареї: `Q = I*t`.[^analog-ampere-hour] Теоретично 2400 мА·год відповідають 240 мА протягом 10 годин, але фактичний час залежить від струму розряду та умов роботи батареї.[^doe-battery-capacity-rate]

## Detailed explanation

мА·год означає міліампер-годину: добуток струму в міліамперах на час у годинах. Це одиниця кількості електричного заряду, а не напруги й не енергії. Один ампер-година дорівнює 1000 мА·год; у SI один ампер-година відповідає 3600 кулонам заряду.[^analog-ampere-hour]

Якщо батарея віддає сталий струм, просте наближення для заряду має вигляд `Q = I*t`. Наприклад, для номіналу 2400 мА·год і струму 240 мА ідеальний розрахунок дає `t = Q/I = 2400 mAh/240 mA = 10 h`. Це оцінка за припущення сталого струму й доступності всієї номінальної ємності, а не гарантія часу до вимкнення пристрою.[^analog-ampere-hour]

Реальна ємність залежить від хімії батареї, температури, струму розряду, кінцевої напруги та інших умов. Для деяких батарей більший струм означає меншу доступну ємність, а номінальне значення в документації вказують разом із тестовими умовами. Крім того, мА·год не дозволяють порівнювати запас енергії батарей із різною напругою без урахування напруги: енергія приблизно пов’язана з добутком заряду на напругу.[^doe-battery-capacity-rate]

Приклад: ідеальні 2400 мА·год можна поділити на 120 мА й отримати 20 годин, або на 480 мА й отримати 5 годин. У реальному виробі ці результати можуть відрізнятися, бо струм може змінюватися, а доступна ємність залежить від швидкості розряду та порогу вимкнення. Типова помилка – вважати mAh безпосередньою мірою енергії або обіцяним часом роботи.[^analog-ampere-hour][^doe-battery-capacity-rate]

## Sources

<!-- generated from frontmatter -->
