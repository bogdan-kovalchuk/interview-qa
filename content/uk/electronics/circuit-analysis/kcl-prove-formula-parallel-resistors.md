---
id: emb-elcirc-0013
title: "Як KCL доводить формулу паралельного з’єднання резисторів?"
description: "Як KCL доводить формулу паралельного з’єднання резисторів?"
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
  - source_id: aac-parallel-resistors
    title: "All About Circuits: Resistance in Parallel Networks"
    url: https://www.allaboutcircuits.com/technical-articles/resistance-in-parallel-networks
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Однакова напруга паралельних гілок, сума струмів за KCL і формула еквівалентного опору резисторів."
---

## Short answer

Для резисторів, під’єднаних між тими самими двома вузлами, напруга `V` на кожній гілці однакова. За KCL і законом Ома `I_s = V/R_1 + V/R_2`, тому `1/R_eq = 1/R_1 + 1/R_2`; для двох резисторів `R_eq = R_1*R_2/(R_1+R_2)`.[^aac-parallel-resistors]

## Detailed explanation

Паралельно з’єднані резистори мають обидва виводи під’єднаними до тих самих двох вузлів. Через це напруга між вузлами однакова для кожної гілки, хоча струм у гілках може бути різним. Еквівалентний резистор має споживати від вузла той самий сумарний струм, що й усі гілки разом.[^aac-parallel-resistors]

Застосуємо KCL до вузла, де струм джерела розгалужується: `I_s = I_1 + I_2`. За законом Ома `I_1 = V/R_1` та `I_2 = V/R_2`, де `V` – спільна напруга між вузлами. Еквівалентний опір визначений так, щоб для тієї самої напруги `I_s = V/R_eq`. Прирівнюємо обидва вирази й ділимо на ненульову `V`: `1/R_eq = 1/R_1 + 1/R_2`. Для двох скінченних резисторів алгебраїчне перетворення дає добуток, поділений на суму.[^aac-parallel-resistors]

**Приклад розрахунку:**

Нехай `R_1 = 1 kΩ`, `R_2 = 2 kΩ`, а напруга між вузлами дорівнює `6 V`:

```text
I_1 = 6 V / 1 kΩ = 6 mA
I_2 = 6 V / 2 kΩ = 3 mA
I_s = I_1 + I_2 = 9 mA
R_eq = 6 V / 9 mA = 0.667 kΩ
```

Обернена форма також дає `1/R_eq = 1/1 kΩ + 1/2 kΩ`, тобто той самий результат. Еквівалентний опір має бути меншим за кожен опір гілки: додавання паралельного шляху збільшує провідність. Формула передбачає резистивні елементи й справжнє паралельне під’єднання; якщо гілки мають різні кінцеві вузли, спільну напругу підставляти не можна.[^aac-parallel-resistors]

**Типова помилка:**

- Додавати опори паралельних гілок напряму. Складаються провідності `1/R`; сума опорів стосується послідовного з’єднання.[^aac-parallel-resistors]

## Sources

<!-- generated from frontmatter -->
