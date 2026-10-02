---
id: emb-elintro-0026
title: "Як перетворити 3.0 × 10⁴ Вт у кіловати?"
description: "Як перетворити 3.0 × 10⁴ Вт у кіловати?"
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
  - source_id: nist-si-prefixes
    title: "NIST: SP 330, Section 3 – Decimal multiples and sub-multiples of SI units"
    url: https://www.nist.gov/pml/special-publication-330/sp-330-section-3
    accessed: 2026-10-04
    kind: official
    version: "2019 edition, updated 2025-08-18"
    applicability: "Визначає kilo як 10³ і mega як 10⁶; підтримує перерахунок одиниць SI, не конкретний приклад з картки."
---

## Short answer

Оскільки префікс kilo означає 10³, 3.0 × 10⁴ Вт дорівнюють 30 кВт. Це також 0.03 МВт, бо mega означає 10⁶.[^nist-si-prefixes]

## Detailed explanation

Щоб перевести вати у кіловати, поділіть значення у ватах на 1000: префікс kilo означає множник 10³. Тут `3.0 × 10⁴ Вт` – це `30 000 Вт`, тому `30 000 / 1000 = 30 кВт`.[^nist-si-prefixes]

Коефіцієнт 3.0 має дві значущі цифри, тож запис `30 кВт` зберігає точність вихідного числа. Не слід читати kilo як 1024: SI-префікси є десятковими, а для двійкових множників використовують окремі префікси на кшталт kibi.[^nist-si-prefixes]

Той самий перерахунок можна виконати, розклавши степені десяти: `3.0 × 10⁴ Вт = 3.0 × 10 × 10³ Вт`. Оскільки `10³ Вт` становить один кіловат, коефіцієнт перед ним дорівнює 30. Такий спосіб допомагає уникнути помилки на три порядки, коли потрібно перейти від базової одиниці до одиниці з префіксом.[^nist-si-prefixes]

Одиниця Вт не змінює фізичну величину: і вати, і кіловати вимірюють потужність. Змінюється лише масштаб запису, тому значення потрібно ділити на кількість ватів в одному кіловаті, а не множити на 1000.[^nist-si-prefixes]

**Перевірка порядку величини:** `30 кВт = 30 000 Вт`, тож початкові вати та результат кіловатів описують ту саму потужність.

## Sources

<!-- generated from frontmatter -->
