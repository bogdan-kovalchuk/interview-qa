---
id: emb-elee-0069
title: "Знайдіть струм, якщо `Z` = 3 + j4 Ω, а джерело має значення 10∠0° V RMS."
description: "Знайдіть струм за імпедансом 3 + j4 Ω і напругою джерела 10∠0° V RMS."
track: electronics
section: ee101
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
    applicability: "Походження питання: лекція 43, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-ac-complex-ohms
    title: "All About Circuits: R, L and C Summary"
    url: https://www.allaboutcircuits.com/TEXTBOOK/alternating-current/chpt-5/r-l-and-c-summary/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Закон Ома для комплексних фазорів, інтерпретація полярних модуля та кута; числовий приклад у поясненні незалежно перерахований."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

Імпеданс `Z = 3 + j4 Ω` має модуль `5 Ω` і кут `53.13°`. За законом Ома для фазорів струм дорівнює `2∠-53.13° A`, або `1.2 - j1.6 A RMS`; знак кута означає, що струм відстає від напруги.[^aac-ac-complex-ohms]

## Detailed explanation

Фазорний закон Ома має ту саму структуру, що й звичайний, але напруга, струм та імпеданс є комплексними величинами: `I = V/Z`. Знаменник треба розуміти як модуль і кут, а не просто як скалярний опір. Оскільки джерело задано як `10∠0° V RMS`, результат струму також буде RMS.[^aac-ac-complex-ohms]

Спочатку переведемо імпеданс `3 + j4 Ω` у полярну форму. Його модуль – гіпотенуза прямокутного трикутника з катетами 3 і 4; кут визначається відношенням уявної складової до дійсної з урахуванням квадранта. Оскільки обидві складові додатні, кут лежить у першому квадранті.[^aac-ac-complex-ohms]

При діленні комплексних чисел у полярній формі модулі діляться, а кут знаменника віднімається від кута чисельника. Тому фаза струму є `0° - 53.13°`: для цього пасивного імпедансу струм відстає від напруги. Після обчислення можна повернути результат у прямокутну форму, щоб побачити його дві координати.[^aac-ac-complex-ohms]

Приклад розрахунку:

```text
|Z| = sqrt(3^2 + 4^2) = 5 Ω
angle(Z) = atan2(4, 3) ≈ 53.13°
I = (10∠0° V)/(5∠53.13° Ω) = 2∠-53.13° A RMS
I ≈ 1.2 - j1.6 A RMS
```

Перевірка множенням повертає вихідну напругу: `(1.2 - j1.6)*(3 + j4) = 10 + j0 V`. Якщо пропустити мінус у фазі струму або переплутати віднімання кутів, ця перевірка не зійдеться. Число тут наведене для ідеального лінійного імпедансу з заданим значенням на частоті джерела; реальна схема може мати інші параметри.[^aac-ac-complex-ohms]

**Типові помилки:**

- Ділити лише на дійсну частину `3 Ω`, ігноруючи реактивну складову.
- Ділити модулі, але додавати замість віднімати кут знаменника.
- Повідомляти результат у peak, хоча джерело задане в RMS.[^aac-ac-complex-ohms]

## Sources

<!-- generated from frontmatter -->
