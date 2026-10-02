---
id: emb-elintro-0104
title: "Для чого призначена \"канавка\" (trench) посередині макетної плати?"
description: "Для чого призначена \"канавка\" (trench) посередині макетної плати?"
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
  - source_id: adafruit-breadboards
    title: "Adafruit Learning System: Breadboards for Beginners"
    url: https://learn.adafruit.com/breadboards-for-beginners?view=all
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Підтверджує типову будову й електричні зв’язки; конкретна реалізація може відрізнятися."
---

## Short answer

Центральна канавка розділяє контактні групи двох боків breadboard, щоб ніжки DIP-мікросхеми могли входити в різні групи й не з’єднувалися між собою. У типовій платі п’ять отворів одного ряду з кожного боку з’єднані між собою, але через канавку ці групи ізольовані.[^adafruit-breadboards]

## Detailed explanation

Центральна канавка відокремлює два поля контактів макетної плати, щоб ніжки корпусу DIP могли розташовуватися по різні її боки без електричного контакту між протилежними виводами. Усередині типової solderless breadboard металеві пружні контакти об’єднують групи отворів: зазвичай п’ять отворів у поперечному ряду з одного боку належать до одного вузла, а п’ять навпроти – до іншого. Канавка залишає ці групи розділеними.[^adafruit-breadboards]

Таке розташування дає змогу вставити DIP-мікросхему так, щоб два ряди її ніжок опинилися в окремих контактних групах. Якби обидва боки одного рядка були з’єднані, ніжки навпроти одна одної виявилися б коротко замкненими, і схема мікросхеми працювала б неправильно. Канавка також полегшує виймання мікросхеми тонким інструментом, але її основна електрична роль – ізоляція половин контактного поля.[^adafruit-breadboards]

**Типові помилки:**
- Не вважайте, що всі отвори на одній горизонтальній лінії з’єднані: центральний розрив ділить її на ліву й праву групи.
- Не переносіть рисунок контактів однієї breadboard на іншу без перевірки: мініплати та окремі моделі можуть мати інший рисунок.
- За сумнівів перевірте сусідні вузли мультиметром у режимі прозвонювання.[^adafruit-breadboards]

## Sources

<!-- generated from frontmatter -->
