---
id: emb-elintro-0030
title: "Яка різниця між N-типом і P-типом кремнію?"
description: "Яка різниця між N-типом і P-типом кремнію?"
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
    applicability: "Походження питання: лекція 5, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: mit-semiconductor-physics
    title: "MIT OpenCourseWare: 6.012, Lecture 2 – Semiconductor Physics (I)"
    url: https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2005/resources/lec2/
    accessed: 2026-10-04
    kind: book
    version: "Fall 2005"
    applicability: "Університетські конспекти пояснюють донорне й акцепторне легування Si та більшість носіїв заряду; конкретні концентрації залежать від матеріалу."
---

## Short answer

У Si донорні домішки, як-от фосфор, дають матеріал N-типу з електронами як основними носіями; акцепторні домішки, як-от бор, дають P-тип із дірками як основними носіями. У цілому кожен легований кристал залишається електрично нейтральним.[^mit-semiconductor-physics]

## Detailed explanation

N-тип і P-тип кремнію отримують легуванням – контрольованим додаванням домішкових атомів до кристалічної ґратки Si. У донорної домішки з п'ятої групи, наприклад фосфору, чотири валентні електрони беруть участь у зв'язках із сусідніми атомами кремнію, а п'ятий порівняно легко стає рухомим електроном. Тому в N-типі електрони є основними, тобто численнішими, носіями заряду.[^mit-semiconductor-physics]

Акцепторна домішка з третьої групи, наприклад бор, має на один валентний електрон менше, ніж потрібно для повного набору зв'язків із сусідніми атомами Si. Незайняте місце у зв'язку описують як дірку; електрони сусідніх зв'язків можуть переходити на це місце, тож дірка переміщується крізь кристал. У P-типі дірки є основними носіями, хоча невелика кількість електронів також залишається.[^mit-semiconductor-physics]

Літери N і P вказують на знак основних рухомих носіїв – negative electrons або positive holes, а не на сумарний заряд зразка. Іонізовані домішки нерухомі в ґратці й компенсують заряд носіїв, тому обидва матеріали загалом нейтральні. За температури, концентрації легування та інших умов змінюються концентрації основних і неосновних носіїв; твердження «N має лише електрони, P має лише дірки» було б надмірним спрощенням.[^mit-semiconductor-physics]

**Коротке зіставлення:** донор -> N-тип -> основні носії електрони; акцептор -> P-тип -> основні носії дірки.

## Sources

<!-- generated from frontmatter -->
