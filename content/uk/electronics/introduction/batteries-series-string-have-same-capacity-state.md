---
id: emb-elintro-0063
title: "Чому батареї в послідовному ланцюгу бажано мати однакову ємність і стан заряду?"
description: "Чому батареї в послідовному ланцюгу бажано мати однакову ємність і стан заряду?"
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
  - source_id: victron-series
    title: "Victron Lithium Battery Smart – Installation"
    url: https://www.victronenergy.com/media/pg/Lithium_Battery_Smart/en/installation.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Ємність послідовного ланцюга, дисбаланс і сумісність батарей."
  - source_id: panasonic-mixing
    title: "Panasonic eneloop FAQ"
    url: https://www.panasonic.com/global/energy/products/eneloop/en/faq.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Застереження виробника щодо змішування типів, ємностей, марок та віку батарей у пристрої."
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
---

## Short answer

У послідовному ланцюзі через кожну батарею проходить той самий струм, тому загальна напруга додається, а ємність у Ah не додається: її обмежує батарея з найменшою доступною ємністю.[^victron-series] Різний стан заряду чи ємність спричиняють дисбаланс, тож виробники зазвичай вимагають узгоджені батареї та дотримання правил конкретної системи.[^panasonic-mixing]

## Detailed explanation

У послідовному з’єднанні позитивний полюс однієї батареї під’єднаний до негативного полюса наступної. Струм у всіх елементах однаковий, а напруга батарей додається. Ємність у ампер-годинах не додається, бо кожен елемент мусить пропустити той самий заряд; коли найменший елемент вичерпає доступну ємність, розряд усього ланцюга потрібно припинити.[^victron-series]

**Приклад:** якщо послідовно з’єднати батареї 50 Ah і 100 Ah, теоретично весь ланцюг обмежений приблизно 50 Ah, а не 150 Ah. У реальній системі результат може бути гіршим: відмінності характеристик призводять до дисбалансу, і слабший елемент першим досягає межі розряду чи заряду.[^victron-series]

Однаковий початковий стан заряду сам по собі не робить батареї взаємозамінними. Їхня фактична ємність залежить від типу, віку, температури, попередньої експлуатації та режиму навантаження. Виробник Victron рекомендує для послідовної системи батареї однакової ємності й моделі; Panasonic застерігає від змішування типів, ємностей, брендів і віку у пристроях, бо різниці можуть призвести до надмірного розряду й витоку.[^victron-series] [^panasonic-mixing]

Під час заряду проблема теж важлива: елементи в ланцюзі отримують той самий струм, але їхня напруга змінюється нерівномірно. Один елемент може досягти верхньої межі раніше, тоді як інший ще не заряджений; тому акумуляторні батарейні блоки потребують передбаченого виробником зарядного пристрою та, якщо конструкція передбачає, BMS або балансування.[^victron-series]

**Типова помилка:** плутати послідовне й паралельне з’єднання. Послідовне підвищує сумарну напругу, але не додає Ah; паралельне зберігає напругу й може збільшити Ah за сумісних батарей і дозволу виробника.

Перед складанням блока звірте хімію, номінальну ємність, модель і вимоги виробника. Не змішуйте нові та зношені елементи лише тому, що їхня напруга зараз однакова: напруга без навантаження не показує однакової доступної ємності.

## Sources

<!-- generated from frontmatter -->
