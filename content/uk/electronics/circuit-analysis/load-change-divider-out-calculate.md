---
id: emb-elcirc-0032
title: "Як навантаження R_L змінює V_out подільника і як це розрахувати?"
description: "Як навантаження R_L змінює V_out подільника і як це розрахувати?"
track: electronics
section: circuit-analysis
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
    applicability: "Походження питання: лекція 30, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-voltage-divider
    title: "All About Circuits: Voltage Divider Circuits"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-6/voltage-divider-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює розподіл напруги в послідовному колі; навантаження слід врахувати окремо."
---

## Short answer

Навантаження `R_L` підключається паралельно `R_2`, зменшуючи ефективний нижній опір: `R_2,eff = R_2*R_L/(R_2+R_L)`. Підставте `R_2,eff` замість `R_2` у формулу подільника. Що менший `R_L`, то нижчі ефективний опір і `V_out`.[^aac-direct-current]

## Detailed explanation

Навантаження підключене між виходом подільника та спільним проводом, тобто паралельно `R_2`. Для паралельних опорів еквівалент менший за кожен із них: `R_2,eff = R_2*R_L/(R_2+R_L)`. Цей еквівалент стає новим нижнім плечем, а верхнє `R_1` залишається послідовним із ним. Після підключення навантаження змінюється співвідношення опорів, а отже й напруга виходу.[^aac-direct-current]

Інший спосіб побачити той самий ефект – подати ненавантажений подільник як еквівалент Тевенена. Його напруга дорівнює попередньому `V_out`, а послідовний вихідний опір дорівнює `R_1` паралельно `R_2`. Струм навантаження створює спад на цьому внутрішньому опорі. Ця модель зручна, коли треба порівняти кілька різних навантажень, не перераховуючи схему з нуля.[^aac-direct-current]

Приклад розрахунку:

Нехай `V_in = 12 V`, `R_1 = 10 kΩ`, `R_2 = 10 kΩ`, а `R_L = 10 kΩ`. Паралель нижніх резисторів дорівнює `5 kΩ`, тому `V_out = 12 V*5 kΩ/(10 kΩ+5 kΩ) = 4 V`. Без навантаження вихід був би `6 V`; підключений резистор удвічі зменшив нижній еквівалент, і вихід просів.

**Типові помилки:**

- Підставляти `R_L` послідовно з `R_2`, хоча вони під’єднані до тих самих двох вузлів.
- Вважати, що формула ненавантаженого подільника залишається точною для будь-якого входу наступного каскаду; вплив визначається співвідношенням `R_L` з опорами подільника.

## Sources

<!-- generated from frontmatter -->
