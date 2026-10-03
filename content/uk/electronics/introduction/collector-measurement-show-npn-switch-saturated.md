---
id: emb-elintro-0222
title: "Що показує вимірювання колектора, коли NPN-ключ увімкнений і насичений?"
description: "Що показує вимірювання колектора, коли NPN-ключ увімкнений і насичений?"
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
    applicability: "Походження питання: лекція 21, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-bjt-switch
    title: "All About Circuits: The Bipolar Junction Transistor (BJT) as a Switch"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/transistor-switch-bjt/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює cutoff, насичення та поведінку колекторного вузла; напруга насичення залежить від конкретного транзистора й струму."
---

## Short answer

У насиченому NPN-ключі напруга `V_CE(sat)` мала, але не дорівнює нулю; її конкретне значення залежить від транзистора та струму навантаження. Тому колектор близький до напруги емітера, якщо емітер під’єднаний до `GND`.[^aac-bjt-switch]

## Detailed explanation

Увімкнений NPN-ключ має достатній струм бази, щоб перейти в насичення: обидва переходи транзистора проводять, а напруга між колектором та емітером стає малою. Транзистор нагадує замкнений вимикач, але реальний `V_CE(sat)` не нульовий і залежить від типу компонента та струму колектора.[^aac-bjt-switch]

Якщо емітер під’єднано до `GND`, вимірювання напруги колектора відносно землі дає приблизно `V_CE(sat)`. Не слід плутати її з напругою живлення чи вважати універсальною сталою. У даташитах насичення задають за конкретних умов, зокрема струмів колектора й бази; значення з однієї демонстраційної схеми не переноситься автоматично на іншу.[^aac-bjt-switch]

**Приклад:** у вимірюванні з емітером на землі показ близько 0.1 В означає, що транзистор проводить і на ньому залишається невелика напруга. Показ у кілька вольтів за того самого живлення може означати, що транзистор не насичений, навантаження або з’єднання інше, чи вимірюється не той вузол.[^aac-bjt-switch]

**Типова помилка:** називати `V_CE(sat)` нульовою напругою або гарантованим діапазоном без зазначення моделі та умов. Для розрахунків беріть параметр із даташита транзистора за умов, близьких до вашої схеми.[^aac-bjt-switch]

## Sources

<!-- generated from frontmatter -->
