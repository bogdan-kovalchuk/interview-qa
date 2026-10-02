---
id: emb-elintro-0066
title: "Закон Фарадея – що відбувається, коли провідник рухається в магнітному полі?"
description: "Закон Фарадея – що відбувається, коли провідник рухається в магнітному полі?"
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
    applicability: "Походження питання: лекція 8, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: openstax-faraday
    title: "OpenStax University Physics Volume 2: Faraday's Law"
    url: https://openstax.org/books/university-physics-volume-2/pages/13-1-faradays-law
    accessed: 2026-10-04
    kind: book
    version: "University Physics Volume 2"
    applicability: "Закон Фарадея, магнітний потік і наведена ЕРС у контурі; не задає параметри конкретної машини."
  - source_id: openstax-motional-emf
    title: "OpenStax University Physics Volume 2: Motional Emf"
    url: https://openstax.org/books/university-physics-volume-2/pages/13-3-motional-emf
    accessed: 2026-10-04
    kind: book
    version: "University Physics Volume 2"
    applicability: "Формула motional EMF для рухомого провідника та залежність від геометрії."
---

## Short answer

Коли магнітний потік через замкнений контур змінюється, у ньому індукується ЕРС; для рухомого провідника вона виникає через дію магнітної сили на заряди.[^openstax-faraday] Зміна потоку може відбутися через рух, зміну поля або поворот контуру.[^openstax-faraday]

## Detailed explanation

Закон Фарадея описує індуковану ЕРС як наслідок зміни магнітного потоку через контур. Потік залежить від магнітного поля, площі контуру та його орієнтації, тому змінити його можна рухом провідника або магніту, зміною поля чи поворотом контуру.[^openstax-faraday]

Для котушки з `N` витками внесок кожного витка додається: `EMF = -N*dΦ/dt`. Знак мінус виражає правило Ленца: індукований струм створює поле, яке протидіє зміні потоку, що його спричинила. Напрям струму залежить від того, як саме змінюється потік.[^openstax-faraday]

Якщо прямий провідник довжини `L` рухається зі швидкістю `v` у сталому полі `B`, а рух, провідник і поле взаємно перпендикулярні, модуль motional EMF дорівнює `EMF = B*L*v`. Заряди зазнають сили Лоренца й розділяються вздовж провідника. За іншої геометрії враховують перпендикулярні компоненти; сам рух у полі не гарантує ЕРС, якщо провідник рухається паралельно полю.[^openstax-motional-emf]

Приклад: провідник довжиною `0.2 m` рухається зі швидкістю `3 m/s` перпендикулярно до поля `0.5 T`; за ідеалізованих умов `EMF = 0.5*0.2*3 = 0.3 V`. У генераторі обертання змінює потік і створює вихідну ЕРС. У трансформаторі потік змінює струм у первинній обмотці, тому провідники не мусять рухатися.[^openstax-faraday]

**Типова помилка:** вважати, що для індукції обов’язковий рух провідника. Вирішальною умовою є зміна потоку через контур; нерухома котушка також має індуковану ЕРС у змінному полі.[^openstax-faraday]

## Sources

<!-- generated from frontmatter -->
