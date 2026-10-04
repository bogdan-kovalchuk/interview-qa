---
id: emb-elee-0096
title: "Що змінює навантаження, підключене до виходу RC-ФНЧ?"
description: "Що змінює навантаження, підключене до виходу RC-ФНЧ?"
track: electronics
section: ee101
level: junior
type: pitfall
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
    applicability: "Походження питання: лекція 48, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-low-pass-filters
    title: "All About Circuits: Low-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/low-pass-filters/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтверджує вплив паралельного навантаження на частотну характеристику простого RC-ФНЧ і межі ненавантаженої формули."
---

## Short answer

За ідеального джерела навантаження `R_L`, підключене паралельно C, змінює gain у смузі пропускання та частоту зрізу. Для резистивного навантаження ефективний опір у часовій сталі дорівнює `R||R_L`, тому `f_c = 1/(2π*C*(R||R_L))`; звична формула `1/(2π*R*C)` стосується ненавантаженого виходу.[^aac-low-pass-filters]

## Detailed explanation

Навантаження на виході простого RC-ФНЧ утворює додатковий шлях струму паралельно конденсатору й змінює подільник напруги. Розгляньмо ідеальне джерело, послідовний резистор `R`, а на вихідному вузлі – `C` паралельно з резистивним навантаженням `R_L`. На постійному струмі конденсатор розімкнений, тож вихідне відношення напруг дорівнює `R_L/(R+R_L)`, а не одиниці. Отже, навіть у смузі пропускання реальне навантаження може послабити сигнал.[^aac-low-pass-filters]

Для змінної складової конденсаторний імпеданс залежить від частоти, а опір, який бачить конденсатор після занулення ідеального джерела, становить `R||R_L`. Тому полюс першого порядку задається `τ = (R||R_L)*C`, а частота зрізу – `f_c = 1/(2π*(R||R_L)*C)`. Оскільки `R||R_L` менше за `R`, підключення скінченного `R_L` зазвичай підвищує частоту зрізу відносно ненавантаженого випадку та знижує низькочастотний gain. Формула `1/(2π*R*C)` без урахування навантаження тут не дає повної характеристики.[^aac-low-pass-filters]

**Приклад:** якщо `R = 10 kΩ`, `R_L = 10 kΩ` і `C = 10 nF`, то `R||R_L = 5 kΩ`, а `f_c ≈ 3.18 kHz`; для ненавантаженого виходу було б близько `1.59 kHz`. Низькочастотне відношення напруг у цьому навантаженому прикладі дорівнює `10/(10+10) = 0.5`. Це розрахунок для ідеального джерела та ідеальних R і C; ненульовий вихідний опір джерела додається до послідовного опору, а реактивне або складніше навантаження потребує аналізу повного імпедансу.[^aac-low-pass-filters]

**Типові помилки:**

- Використовувати тільки `R` у формулі зрізу, ігноруючи паралельний `R_L`.
- Припускати, що навантаження може лише зменшити амплітуду й не впливає на частоту переходу.
- Застосовувати цю просту формулу до навантаження з істотною частотною залежністю без аналізу його імпедансу.[^aac-low-pass-filters]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
