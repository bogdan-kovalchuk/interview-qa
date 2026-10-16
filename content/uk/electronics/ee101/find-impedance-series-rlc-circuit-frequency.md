---
id: emb-elee-0063
title: "Як знайти імпеданс послідовного RLC-кола на заданій частоті?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: aac-series-rlc
    title: "All About Circuits: Series R, L, and C"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-5/series-r-l-and-c/
---

## Short answer

Для заданої частоти обчисліть `X_L = 2π*f*L` і `X_C = 1/(2π*f*C)`, а потім `Z = R + j*(X_L - X_C)`. Модуль дорівнює `|Z| = sqrt(R² + (X_L - X_C)²)`, а кут – `atan2(X_L - X_C, R)`; у послідовному колі струм є `I = V/Z` у фазорній формі.[^aac-series-rlc]

## Detailed explanation

Імпеданс послідовного RLC-кола знаходять, додаючи комплексні імпеданси його елементів на заданій частоті. Спершу перетворіть частоту `f` на кутову частоту `ω = 2π*f`, після чого розрахуйте індуктивну реактивність `X_L = ω*L` та ємнісну `X_C = 1/(ω*C)`. Опір резистора залишається дійсною складовою.[^aac-series-rlc]

Оскільки індуктивність і ємність мають протилежні знаки уявної складової, сумарний імпеданс дорівнює `Z = R + j*(X_L - X_C)`. Звідси модуль `|Z| = sqrt(R² + (X_L - X_C)²)`, а фаза `φ = atan2(X_L - X_C, R)`. Функція `atan2` зберігає правильний квадрант; для пасивного послідовного кола з `R > 0` це кут від -90° до +90°.[^aac-series-rlc]

Коли `X_L = X_C`, реактивні складові взаємно компенсуються, тому імпеданс дорівнює лише `R` і має нульовий кут. Нижче цієї частоти коло має ємнісний характер, а вище – індуктивний. Якщо одного з компонентів у схемі немає, відповідну складову не додають: для RC-кола лишається `-j*X_C`, для RL-кола – `+j*X_L`.[^aac-series-rlc]

Щоб знайти струм, треба ділити фазор напруги джерела на комплексний імпеданс: `I = V/Z`. Ділення лише на `|Z|` дає величину струму, але не його фазу відносно напруги. Аналогічно, напруги на компонентах складаються фазорно, хоча їхні модулі можуть арифметично не давати модуль джерела.[^aac-series-rlc]

**Типова помилка:** відняти реактивності без урахування знаків або взяти квадратний корінь тільки з `R² + X_L² + X_C²`. Спершу складіть уявні складові зі знаками, а вже потім визначайте модуль і кут комплексного результату.[^aac-series-rlc]
