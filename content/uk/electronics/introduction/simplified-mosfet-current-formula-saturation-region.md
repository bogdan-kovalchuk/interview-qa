---
id: emb-elintro-0240
title: "Яка спрощена формула струму MOSFET у saturation region?"
description: "Яка спрощена формула струму MOSFET у saturation region?"
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
    applicability: "Походження питання: лекція 22, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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

Для ідеального long-channel NMOS у saturation region `I_D = K*(V_GS - V_th)^2`, де `K` охоплює параметри процесу й геометрії та залежить від домовленості щодо коефіцієнта `1/2`. Модель вимагає `V_GS > V_th` і `V_DS >= V_GS - V_th`; реальний струм також залежить від неідеальностей приладу.[^aac-semiconductors]

## Detailed explanation

Для довгоканального enhancement NMOS у спрощеній square-law моделі saturation region струм задають як `I_D = K*(V_GS - V_th)^2`. Тут `V_GS - V_th` – overdrive voltage, а `K` об’єднує mobility, oxide capacitance і відношення ширини каналу до його довжини. У поширеному виведенні коефіцієнт дорівнює `K = μ*C_ox*(W/L)/2`; в інших джерелах множник `1/2` можуть включити в саме визначення `K`, тому формулу треба читати разом із цим визначенням.[^aac-semiconductors]

Для NMOS умова saturation приблизно має вигляд `V_DS >= V_GS - V_th` за `V_GS > V_th`. У цій області канал біля drain затискається, а ідеальна модель вважає `I_D` незалежним від подальшого зростання `V_DS`. Реальний транзистор має channel-length modulation та інші неідеальності, тому струм не є абсолютно сталим.[^aac-semiconductors]

Приклад: якщо overdrive `V_GS - V_th` подвоїти, ідеальна формула прогнозує збільшення `I_D` у чотири рази за незмінного `K` і за умови, що прилад лишається в saturation. Це не універсальна формула для силового MOSFET як ключа: у його on-state зазвичай користуються специфікацією `R_DS(on)`, а не екстраполюють square-law модель.[^aac-semiconductors]

**Типові помилки:**
- Не уточнювати, чи множник `1/2` уже входить у `K`.
- Застосовувати формулу в triode region або нижче порога.
- Вважати струм реального MOSFET незалежним від `V_DS`.

## Sources

<!-- generated from frontmatter -->
