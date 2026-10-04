---
id: emb-elcirc-0014
title: "Як KVL доводить формулу послідовного з’єднання резисторів?"
description: "Як KVL доводить формулу послідовного з’єднання резисторів?"
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
    applicability: "Походження питання: лекція 28, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-series-circuits
    title: "All About Circuits: Series Circuits and the Application of Ohm’s Law"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-5/simple-series-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Однаковий струм у послідовному шляху, KVL, закон Ома й сума послідовних опорів."
---

## Short answer

У послідовному колі через усі резистори тече той самий струм `I`. За KVL напруга джерела дорівнює сумі спадів: `V_s = I*R_1 + I*R_2 + ...`; отже, для резисторів `R_eq = R_1 + R_2 + ...`.[^aac-series-circuits]

## Detailed explanation

У послідовному з’єднанні елементи утворюють один шлях без розгалужень, тому через кожен резистор проходить той самий струм `I`. Еквівалентний резистор визначають як один елемент, який за того самого струму створює сумарне падіння напруги на всьому ланцюжку.[^aac-series-circuits]

Обійдімо замкнений контур і застосуймо KVL: алгебраїчна сума напруг дорівнює нулю. Якщо підйом напруги джерела позначити `V_s`, а падіння на резисторах – `V_1`, `V_2` тощо, отримаємо `V_s = V_1 + V_2 + ...`. Закон Ома для кожного резистора дає `V_i = I*R_i`. Підстановка винесе спільний струм за дужки: `V_s = I*(R_1 + R_2 + ...)`. Оскільки для еквівалентного резистора `V_s = I*R_eq`, сума опорів і є еквівалентним значенням.[^aac-series-circuits]

**Приклад:**

Для `R_1 = 1 kΩ` і `R_2 = 2 kΩ`, під’єднаних послідовно до ідеального джерела `6 V`, маємо `R_eq = 3 kΩ` та струм `I = 6 V / 3 kΩ = 2 mA`. Падіння напруг становлять `2 V` і `4 V`; їхня сума відтворює напругу джерела. Це узгоджується з KVL і законом Ома.[^aac-series-circuits]

У реальній схемі правило стосується компонентів у тому самому нерозгалуженому шляху; при паралельному відгалуженні струми різних гілок уже не рівні. Опір провідників або внутрішній опір джерела враховуйте окремо, якщо вони істотні для потрібної точності. Не плутайте суму опорів у послідовному колі з оберненою сумою для паралельного.[^aac-series-circuits]

**Типова помилка:**

- Підставляти різні струми в послідовні елементи. Спершу переконайтеся, що між ними немає вузла відгалуження, а потім застосовуйте один струм до всіх падінь напруги.[^aac-series-circuits]

## Sources

<!-- generated from frontmatter -->
