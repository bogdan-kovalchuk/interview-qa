---
id: emb-elee-0028
title: "Яку максимальну напругу можна подати на паралельну групу конденсаторів 10 В і 25 В?"
description: "Яку максимальну напругу можна подати на паралельну групу конденсаторів 10 В і 25 В?"
track: electronics
section: ee101
level: junior
type: pitfall
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
    applicability: "Походження питання: лекція 36, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-capacitors-series-parallel
    title: "All About Circuits textbook: Series and Parallel Capacitors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/series-and-parallel-capacitors/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтверджує правила послідовного й паралельного з’єднання та еквівалентної ємності; не задає допуски конкретних компонентів."
---

## Short answer

Для наведеної пари гранична напруга групи – не більше 10 В, бо в паралельному з’єднанні на обох конденсаторах однакова напруга. Це межа за номіналами компонентів; у практичній схемі слід також врахувати допуск джерела, пульсації, перехідні перенапруги й вимоги до derating.[^aac-capacitors-series-parallel]

## Detailed explanation

У паралельному з’єднанні кожний конденсатор підключений до тієї самої пари вузлів, отже напруга на кожному однакова.[^aac-capacitors-series-parallel]

Для конденсаторів із номіналами 10 В і 25 В напруга на обох буде напругою джерела. Якщо джерело перевищить 10 В, елемент із меншим рейтингом опиниться за межами свого номінального режиму, навіть якщо другий конденсатор ще працюватиме в межах 25 В. Тому за самими лише наведеними номіналами верхня межа для групи становить 10 В, а не 25 В і не сума цих значень.[^aac-capacitors-series-parallel]

Це не означає, що 10 В завжди є правильною робочою уставкою. Номінал компонента треба співвіднести з реальною напругою, її пульсаціями та можливими перехідними стрибками; запас визначається типом конденсатора, температурою, надійністю та вимогами виробника. Полярний конденсатор також має бути підключений із правильною полярністю, якщо така вимога є для вибраного типу. Розрахунок за групою не скасовує індивідуальних обмежень найслабшого елемента.[^aac-capacitors-series-parallel]

Приклад перевірки джерела:

```text
V_source_max = 9.0 В + 0.5 В пульсацій + 0.8 В перехідного стрибка
V_source_max = 10.3 В
```

За таких заданих максимумів 10-вольтовий конденсатор уже може бути перенапружений; ця арифметика лише ілюструє перевірку сумарного worst case і не задає універсального запасу. Перед складанням звіряють допустимі умови конкретного компонента.[^aac-capacitors-series-parallel]

**Типова помилка:** орієнтуватися на конденсатор із більшим номіналом або складати номінали. Щоб уникнути цього, спочатку встановлюють топологію, потім порівнюють спільну напругу з рейтингом кожного компонента та перевіряють пікове значення джерела.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
