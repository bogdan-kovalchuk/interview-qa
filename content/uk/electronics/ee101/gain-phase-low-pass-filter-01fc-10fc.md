---
id: emb-elee-0092
title: "Які модуль передавання і фаза RC-ФНЧ на 0.1*f_c, f_c і 10*f_c?"
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
  - source_id: aac-rc-low-pass-transfer
    title: "All About Circuits: Understanding Low-Pass Filter Transfer Functions"
    url: https://www.allaboutcircuits.com/technical-articles/understanding-transfer-functions-for-low-pass-filters/
---

## Short answer

Для ненавантаженого RC-ФНЧ першого порядку `|H| = 1/sqrt(1 + (f/f_c)^2)`, а фаза дорівнює `-atan(f/f_c)`. На `0.1*f_c` маємо `|H| ≈ 0.995` і фазу `-5.7°`; на `f_c` – `0.707` і `-45°`; на `10*f_c` – `0.0995` і `-84.3°`.[^aac-rc-low-pass-transfer]

## Detailed explanation

Частотні значення зручно порівнювати через безрозмірне відношення `x = f/f_c`. Для однополюсного RC-ФНЧ модуль передавання становить `1/sqrt(1 + x^2)`, а фазовий зсув виходу відносно входу – `-atan(x)`. Тому ці відповіді не залежать від конкретних `R` і `C`, якщо реальне коло відповідає моделі першого порядку та вихід не навантажений істотно.[^aac-rc-low-pass-transfer]

Коли частота вдесятеро нижча за зріз, `x = 0.1`: знаменник модуля лише трохи більший за одиницю, отже амплітуда майже не змінюється. На зрізі `x = 1`, тому квадрат знаменника дорівнює `2`; модуль `1/sqrt(2) ≈ 0.707` і фаза `-45°`. Коли частота вдесятеро вища, `x = 10`: модуль стає `1/sqrt(101) ≈ 0.0995`, а фаза наближається до граничних `-90°`, але не досягає її за скінченної частоти.[^aac-rc-low-pass-transfer]

**Приклад перевірки:** при `f_c = 1 kHz` три точки відповідають `100 Hz`, `1 kHz` і `10 kHz`. На останній вихідна амплітуда близько десятої частини вхідної, а не нульова. Значення фази є зсувом для усталеного синусоїдального режиму; форма перехідного процесу після стрибка входу описується окремо в часовій області.[^aac-rc-low-pass-transfer]

**Типові помилки:**
- Плутати коефіцієнт амплітуди `0.707` із потужністю `0.707`.
- Вважати, що `10*f_c` дає точно `0.1` і рівно `-90°`; це лише наближення.
- Ставити плюс перед фазою, хоча вихід конденсаторного ФНЧ відстає від входу.
