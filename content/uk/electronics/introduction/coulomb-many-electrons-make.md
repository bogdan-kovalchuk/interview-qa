---
id: emb-elintro-0021
title: "Що таке кулон і скільки електронів відповідає 1 Кл?"
description: "Що таке кулон і скільки електронів відповідає 1 Кл?"
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
  - source_id: nist-elementary-charge
    title: "NIST: CODATA Value – elementary charge"
    url: https://physics.nist.gov/cuu/Constants/Value/e.html
    accessed: 2026-10-04
    kind: official
    version: "CODATA 2018"
    applicability: "Точне значення елементарного заряду; кількість зарядів у кулоні обчислюється як обернена величина."
---

## Short answer

Кулон (Кл; міжнародне позначення C) – одиниця електричного заряду. Заряд електрона дорівнює `−1.602176634 × 10⁻¹⁹ C`, тому за модулем 1 Кл відповідає приблизно `6.24 × 10¹⁸` електронам.[^nist-elementary-charge]

## Detailed explanation

Кулон вимірює заряд, а не кількість частинок. Елементарний заряд `e` визначений точно: його модуль дорівнює `1.602176634 × 10⁻¹⁹ C`; електрон має заряд `−e`, а протон – `+e`.[^nist-elementary-charge]

Щоб оцінити кількість електронів, треба поділити модуль сумарного заряду на модуль заряду одного електрона. Отже, один кулон за модулем відповідає приблизно `6.24 × 10¹⁸` електронам. Значення приблизне лише через округлення результату; сам елементарний заряд у SI точний.[^nist-elementary-charge]

Це співвідношення описує чистий заряд. У звичайному провіднику електрони рухаються в обох напрямках і можуть бути дуже численними, але їхній внесок у вимірюваний заряд визначається надлишком або нестачею електронів, а не загальною кількістю електронів у матеріалі.

Знак заряду теж не можна ігнорувати: надлишок електронів дає від’ємний заряд, а їхня нестача відносно нейтрального стану – додатний. Формула для кількості частинок використовує модуль заряду, бо кількість електронів не може бути від’ємною. Якщо обчислення дає неціле число, це зазвичай наслідок округлення або означає, що задано середнє значення для потоку чи вимірювання, а не точну кількість окремих електронів.[^nist-elementary-charge]

**Типова помилка:** називати кулон одиницею кількості електронів. Кулон є одиницею заряду; кількість електронів отримують з заряду лише за умови, що йдеться про заряд, перенесений електронами.

## Sources

<!-- generated from frontmatter -->
