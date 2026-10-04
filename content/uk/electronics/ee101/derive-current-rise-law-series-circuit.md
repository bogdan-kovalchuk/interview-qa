---
id: emb-elee-0044
title: "Як вивести закон наростання струму в послідовному RL-колі?"
description: "Як вивести закон наростання струму в послідовному RL-колі?"
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
    applicability: "Походження питання: лекція 39, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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

Для ідеального послідовного RL-кола закон Кірхгофа дає `V_0 = I*R + L*dI/dt`. За сталої напруги `V_0` і початкової умови `I(0) = 0` розв’язок дорівнює `I(t) = (V_0/R)*(1 - e^(-t/τ))`, де `τ = L/R`.[^aac-alternating-current]

## Detailed explanation

Закон наростання струму в послідовному RL-колі отримують із закону Кірхгофа для напруг та співвідношення індуктора `v_L = L*dI/dt`. Розглянемо ідеальні `R` та `L`, підключені до сталої напруги `V_0` у момент `t = 0`; до перемикання струм дорівнює нулю.[^aac-alternating-current]

Падіння напруги на резисторі становить `I*R`, тому сума напруг на резисторі й індукторі дорівнює джерелу: `V_0 = I*R + L*dI/dt`. Переносимо резистивну складову та розділяємо змінні. Інтегрування від початкового стану до часу `t` дає експоненційний перехід від нуля до усталеного струму `V_0/R`; часова стала `τ = L/R` задає характерну тривалість переходу.[^aac-alternating-current]

Приклад виведення для цих початкових умов:

```text
L*dI/dt = V_0 - I*R
dI/(V_0 - I*R) = dt/L
I(t) = (V_0/R)*(1 - e^(-R*t/L))
τ = L/R
```

За `t = τ` струм становить приблизно 63.2% від кінцевого, а за `t = 5τ` – приблизно 99.3%. Це наближення до межі, а не точне досягнення її за скінченний час. Для ненульового початкового струму розв’язок має вигляд `I(t) = I_final + (I(0) - I_final)*e^(-t/τ)`, де `I_final = V_0/R`.[^aac-alternating-current]

**Типові помилки:**

- Підставляти `R*L` замість `L/R` для сталої часу. Перевірка одиниць дає `H/Ω = s`.
- Використовувати цей вираз без припущень про сталу напругу та лінійну індуктивність.
- Забувати початкову умову або включити опір джерела й обмотки неявно: у реальному колі всі послідовні опори входять до повного `R`.[^aac-alternating-current]

## Sources

<!-- generated from frontmatter -->
