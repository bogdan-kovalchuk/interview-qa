---
id: emb-elee-0078
title: "Як обчислити імпеданс і струм послідовного RL-кола?"
description: "Як обчислити імпеданс і струм послідовного RL-кола?"
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
    applicability: "Походження питання: лекція 45, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
---

## Short answer

Для послідовного RL-кола на частоті `f` індуктивний опір дорівнює `X_L = 2π*f*L`, а повний імпеданс – `Z = R + jX_L`. Струм-фазор обчислюють як `I = V/Z`; його модуль `V/√(R² + X_L²)`, а струм відстає від напруги джерела на `atan2(X_L,R)`.[^aac-alternating-current]

## Detailed explanation

У синусоїдальному усталеному режимі резистор ідеально моделюють дійсним опором `R`, а котушку – реактивним опором `jX_L`, де `X_L = 2π*f*L`. Оскільки компоненти з’єднані послідовно, їхні комплексні імпеданси додаються: `Z = R + jX_L`. Модуль дорівнює `√(R² + X_L²)`, а кут – `atan2(X_L,R)`. Комплексна форма потрібна, бо напруги на R і L мають різні фази.[^aac-alternating-current]

За законом Ома для фазорів `I = V_in/Z`. Якщо задані RMS напруга джерела й лінійні компоненти, результатом буде RMS-фазор струму. Його модуль становить `V_in/|Z|`, а фаза відстає від напруги джерела на кут імпедансу. Напруга на котушці `V_L = I*jX_L` випереджає струм на 90°, тоді як напруга на резисторі збігається з фазою струму.[^aac-alternating-current]

Приклад розрахунку для `R = 40 Ω`, `L = 79.58 mH`, `f = 60 Hz` і `V_in = 10 V RMS`:
```text
X_L = 2π*60*0.07958 ≈ 30 Ω
Z = 40 + j30 Ω; |Z| = 50 Ω; angle(Z) ≈ 36.87°
|I| = 10/50 = 0.20 A RMS; angle(I) ≈ -36.87°
```
Ці значення узгоджуються з трикутником імпедансу: `R`, `X_L` та `|Z|` утворюють прямокутний трикутник.[^aac-alternating-current]

**Типові помилки:**
- Додавати `R + X_L` як звичайні числа, ігноруючи фазу.
- Підставляти мілігенрі без перетворення в henry.
- Плутати RMS і peak значення джерела.

Модель припускає ідеальну індуктивність і лінійний режим. Реальна котушка має опір обмотки й паразитні параметри; її індуктивність може змінюватися з частотою та струмом. Тому для точного вимірювання використовуйте модель компонента або його datasheet.[^aac-alternating-current]

## Sources

<!-- generated from frontmatter -->
