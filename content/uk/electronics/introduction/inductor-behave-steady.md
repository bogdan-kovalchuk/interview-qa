---
id: emb-elintro-0142
title: "Як індуктор поводиться при постійному струмі `DC`?"
description: "Як індуктор поводиться при постійному струмі `DC`?"
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
    applicability: "Походження питання: лекція 14, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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

За сталого `DC` ідеальна індуктивність має нульову напругу, бо `di/dt = 0`. Реальна котушка також має опір обмотки `R_wire`, на якому виникає падіння `V = I*R_wire`.[^aac-direct-current]
## Detailed explanation

За сталого постійного струму магнітне поле індуктора вже не змінюється, тому ідеальна індуктивна складова не створює напруги на своїх виводах. Це випливає з `v = L*(di/dt)`: якщо струм незмінний, його похідна за часом дорівнює нулю. Саме тому ідеальний індуктор у усталеному режимі `DC` еквівалентний короткому замиканню, а не розімкненому колу.[^aac-direct-current]

Реальна котушка зроблена з дроту, що має опір, і може мати додаткові втрати в осерді. Тож після завершення перехідного процесу її можна наближено подати як ідеальну індуктивність послідовно з опором обмотки. За законом Ома на цьому опорі залишається напруга `V = I*R_wire`; вона не зникає лише через те, що струм став сталим. Для котушки з опором обмотки `10 Ω`, через яку тече `0.2 A`, спад становить `2 V` за умови, що опір не змінюється від нагрівання.[^aac-direct-current]

Одразу після прикладання джерела поведінка інша: індуктивність протидіє швидкій зміні струму, тож струм зростає поступово. У простому послідовному колі `RL` стала часу дорівнює `τ = L/R`; через кілька сталих часу перехідний процес практично завершується, хоча математично струм наближається до усталеного значення асимптотично.[^aac-direct-current]

**Типова помилка:** казати, що будь-який індуктор після усталення має нульовий опір. Нульова напруга стосується ідеальної індуктивної складової; омметр на реальній котушці вимірює насамперед опір її дроту, а вимірювання в схемі може включати паралельні шляхи.[^aac-direct-current]

## Sources

<!-- generated from frontmatter -->
