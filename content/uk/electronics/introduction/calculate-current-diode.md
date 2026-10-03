---
id: emb-elintro-0167
title: "Розрахуйте струм: V = 9 V, R = 330 Ω, діод Si (`V_f` = 0.7 V)?"
description: "Розрахуйте струм за джерела 9 V, резистора 330 Ω і `V_f` діода 0.7 V."
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
    applicability: "Походження питання: лекція 16, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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

За припущення `V_f = 0.7 V` на резисторі буде `V_R = 9 V - 0.7 V = 8.3 V`, тому струм становитиме `I = V_R/R = 8.3 V/330 Ω ≈ 25 mA`. Це оцінка для заданої моделі; реальне `V_f` залежить від струму й конкретного діода, тож для точнішого розрахунку перевіряють даташит.[^aac-direct-current]

## Detailed explanation

Струм послідовного кола з джерела, резистора й діода визначають за законом Ома та законом напруг Кірхгофа. Умова задачі задає джерело 9 V і резистор 330 Ω, а значення `V_f = 0.7 V` є прийнятим наближенням для прямозміщеного кремнієвого діода, а не точною сталою для всіх струмів.[^aac-direct-current] [^aac-semiconductors]

Спершу напруга джерела розподіляється між діодом і резистором. Якщо в цій моделі на діоді 0.7 V, на резисторі залишається різниця 8.3 V. Оскільки елементи з’єднані послідовно, той самий струм проходить крізь діод і резистор; опір резистора задає основне обмеження струму.[^aac-direct-current]

Приклад розрахунку для ідеального джерела 9 V, резистора 330 Ω і фіксованого падіння діода 0.7 V:

```text
V_R = 9 V - 0.7 V = 8.3 V
I = 8.3 V / 330 Ω = 0.02515 A ≈ 25 mA
```

Відповідь приблизно 25 mA є наближенням, а не точним прогнозом реального компонента. У справжнього діода `V_f` змінюється зі струмом і температурою; після першої оцінки можна звірити робочу точку з графіком або таблицею даташиту й перерахувати струм.[^aac-semiconductors]

Типова помилка – ділити всі 9 V на 330 Ω і отримувати приблизно 27 mA, ігноруючи падіння напруги на діоді. Інша помилка – вважати 0.7 V гарантованим значенням у будь-якому режимі; це спрощення, придатне для оцінки, але граничні струм і потужність резистора також потрібно перевірити.[^aac-direct-current]

## Sources

<!-- generated from frontmatter -->
