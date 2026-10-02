---
id: emb-elintro-0022
title: "Що таке ампер?"
description: "Що таке ампер?"
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
    applicability: "Походження питання: лекція 4, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: nist-sp330-section2
    title: "NIST Special Publication 330: The International System of Units, Section 2"
    url: https://www.nist.gov/pml/special-publication-330/sp-330-section-2
    accessed: 2026-10-04
    kind: official
    version: "2019"
    applicability: "Визначення ампера через елементарний заряд і секунду та похідні одиниці SI."
---

## Short answer

Ампер (A) – одиниця електричного струму; `1 A = 1 C/s`. Це означає, що через переріз провідника за секунду проходить заряд величиною один кулон.[^nist-sp330-section2]

## Detailed explanation

Ампер вимірює швидкість перенесення електричного заряду. Один ампер відповідає потоку одного кулона за секунду, що записують як `I = Q/t` для сталого струму.[^nist-sp330-section2]

У сучасному SI ампер визначено через фіксоване значення елементарного заряду та секунду. Тому твердження про кулон за секунду є узгодженим зі сучасним визначенням одиниці, а не лише побутовою аналогією.[^nist-sp330-section2]

Напрям умовного струму визначають як напрям руху позитивного заряду. У металевому дроті носіями зазвичай є електрони, що рухаються в протилежному напрямку; це не змінює показу струму за модулем.[^aac-direct-current]

Для струму, що змінюється, відношення повного заряду до тривалості інтервалу дає середнє значення. Миттєвий струм описує швидкість перенесення заряду саме в цей момент, тому його не завжди можна відновити лише з кінцевого сумарного заряду. Це розрізнення корисне, наприклад, коли вимірюють імпульсний сигнал або заряджають конденсатор.[^nist-sp330-section2]

**Приклад:** якщо через поперечний переріз за `2 s` переноситься `6 C`, середній струм дорівнює `I = Q/t = 6 C/2 s = 3 A`.

**Типова помилка:** плутати струм із самим зарядом. Заряд вимірюють у кулонах, а струм – у амперах, тобто в кулонах за секунду.

## Sources

<!-- generated from frontmatter -->
