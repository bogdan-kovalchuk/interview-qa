---
id: emb-elintro-0089
title: "Закон Ома – три форми. Яку ви знаєте напам'ять?"
description: "Закон Ома – три форми. Яку ви знаєте напам'ять?"
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
    applicability: "Походження питання: лекція 10, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-ohm
    title: "All About Circuits: Ohm’s Law - How Voltage, Current, and Resistance Relate"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/voltage-current-resistance-relate/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтверджує закон Ома для провідника за заданої температури та його алгебраїчні форми; нелінійні компоненти потребують інших моделей."
---

## Short answer

Закон Ома для омічного резистора має три алгебраїчно еквівалентні форми: `V = I*R`, `I = V/R` і `R = V/I`. Вони дають змогу знайти невідому величину, якщо відомі дві інші; наприклад, `5 V` на `1 kΩ` дають `5 mA`.[^aac-ohm]

## Detailed explanation

Закон Ома пов’язує напругу між виводами резистора, струм через нього та його опір. Умова суттєва: співвідношення `V = I*R` описує омічний елемент за заданих умов, коли його опір можна вважати сталим. Для лампи розжарювання опір змінюється з температурою, а для діода залежність струму від напруги нелінійна, тому не можна беззастережно застосовувати одну сталу величину `R` до будь-якого компонента.[^aac-ohm]

Три записи отримують звичайним алгебраїчним перетворенням тієї самої рівності. Якщо відомі напруга та опір, струм дорівнює їх частці; якщо відомі струм та опір, можна знайти напругу. Стежте за одиницями: вольти ділені на оми дають ампери, а `1 kΩ` потрібно перетворити на `1000 Ω`, якщо використовуєте базові одиниці.[^aac-ohm]

**Приклад розрахунку:** резистор `1 kΩ` під’єднаний до джерела `5 V`. За ідеального джерела й сталого опору струм становить `5 V / 1000 Ω = 0.005 A = 5 mA`. Якщо переплутати `kΩ` з `Ω`, результат відрізнятиметься у тисячу разів. Реальний струм також залежить від допуску резистора та внутрішнього опору джерела.[^aac-ohm]

**Типова помилка:** обирати формулу за пам’яттю, не перевіряючи одиниці й модель компонента. Спершу визначте, які дві величини задані, переведіть їх в сумісні одиниці та перевірте, що компонент справді поводиться як резистор у цьому режимі.[^aac-ohm]

## Sources

<!-- generated from frontmatter -->
