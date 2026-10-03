---
id: emb-elintro-0128
title: "Як вибрати допустиму потужність резистора із запасом?"
description: "Як вибрати допустиму потужність резистора із запасом?"
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
    applicability: "Походження питання: лекція 13, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: ti-resistor-derating
    title: "Texas Instruments: SBAA460, Design Considerations for Isolated Current Sensing"
    url: https://www.ti.com/document-viewer/lit/html/SBAA460
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Самонагрівання резистора, залежність меж від тепловідведення та перевірка power derating curve і температури; приклади стосуються shunt resistors."
---

## Short answer

Спершу обчисліть максимальну потужність резистора, наприклад за `P = I^2*R` або `P = V^2/R`, для найгіршого штатного режиму.[^aac-direct-current] Потім виберіть номінал за datasheet з урахуванням температурного derating, монтажу й охолодження; універсального правила «взяти рівно вдвічі більше» немає.[^ti-resistor-derating]

## Detailed explanation

Допустима потужність резистора – це межа для визначених виробником умов, а не гарантована потужність за будь-якого монтажу. Спершу оцініть найбільшу потужність, яку схема розсіює в резисторі у нормальних робочих режимах. Для резистора її можна знайти через `P = I^2*R` або `P = V^2/R`, використовуючи струм через нього або напругу на ньому.[^aac-direct-current]

Після розрахунку звірте результат із datasheet конкретної серії. Допустима потужність може зменшуватися зі зростанням температури довкілля, а температура компонента залежить від площі мідних доріжок, корпусу, повітряного потоку та сусідніх джерел тепла. Texas Instruments для shunt resistor окремо радить враховувати самонагрівання, перевіряти криву derating у datasheet і оцінювати температуру за максимального штатного навантаження.[^ti-resistor-derating]

Практичний запас корисний, бо розрахунок може не врахувати розкид режиму, температуру або короткочасне перевантаження. Проте співвідношення на кшталт «номінал має бути вдвічі більшим за розраховану потужність» є початковою евристикою, а не загальним правилом для всіх корпусів і температур. Переконайтеся, що після застосування derating крива ще дозволяє розраховане навантаження, а допустиме короткочасне перевантаження не перевищується.[^ti-resistor-derating]

Приклад розрахунку:

```text
I = 0.10 A, R = 25 Ω
P = I^2*R = 0.10^2*25 = 0.25 W
```

Ці 0.25 W – навантаження в заданому прикладі, а не автоматична рекомендація щодо номіналу. Далі виберіть конкретний резистор і перевірте його криву зменшення потужності та теплові умови плати. Резистори з однаковим номіналом потужності можуть мати різні корпуси й умови монтажу, тому маркування саме по собі не доводить безпечність конкретного режиму.[^ti-resistor-derating]

**Типові помилки:**

- Застосувати множник 2 як обов’язкове правило без перевірки datasheet.
- Розрахувати лише середній режим і пропустити максимальний струм або короткочасне перевантаження.
- Не врахувати, що висока температура чи слабке тепловідведення зменшують допустиме навантаження.[^ti-resistor-derating]

## Sources

<!-- generated from frontmatter -->
